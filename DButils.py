import sqlite3
import json
from datetime import datetime
import os

class DBUtils:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db()

    def get_connection(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        return sqlite3.connect(self.db_path)

    def init_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Create conversations table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS conversations (
                    id TEXT PRIMARY KEY,
                    user_id TEXT,
                    timestamp TEXT
                )
            ''')

            # Create conversation_turns table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS conversation_turns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    conversation_id TEXT,
                    role TEXT,
                    content TEXT,
                    timestamp TEXT,
                    FOREIGN KEY (conversation_id) REFERENCES conversations (id)
                )
            ''')

            # Create users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    age_range TEXT,
                    technical_proficiency TEXT,
                    learning_preferences TEXT
                )
            ''')

            # Create metadata table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS metadata (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    conversation_id TEXT,
                    metadata_json TEXT,
                    FOREIGN KEY (conversation_id) REFERENCES conversations (id)
                )
            ''')

            conn.commit()

    def update_user_profile(self, user_profile):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO users (id, age_range, technical_proficiency, learning_preferences)
                VALUES (?, ?, ?, ?)
            ''', (
                user_profile['user_id'],
                user_profile['age_range'],
                user_profile['technical_proficiency'],
                user_profile['learning_preferences']
            ))
            conn.commit()

    def get_conversation_history(self, conversation_id):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT role, content FROM conversation_turns
                WHERE conversation_id = ? ORDER BY timestamp
            ''', (conversation_id,))
            return [{"role": row[0], "content": row[1]} for row in cursor.fetchall()]

    def add_conversation_turn(self, conversation_id, role, content):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            timestamp = datetime.utcnow().isoformat()
            
            # Ensure the conversation exists
            cursor.execute('''
                INSERT OR IGNORE INTO conversations (id, user_id, timestamp)
                VALUES (?, ?, ?)
            ''', (conversation_id, 'default_user', timestamp))
            
            # Add the turn
            cursor.execute('''
                INSERT INTO conversation_turns (conversation_id, role, content, timestamp)
                VALUES (?, ?, ?, ?)
            ''', (conversation_id, role, content, timestamp))
            conn.commit()
    def save_metadata(self, conversation_id, metadata):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO metadata (conversation_id, metadata_json)
                VALUES (?, ?)
            ''', (conversation_id, json.dumps(metadata)))
            conn.commit()

    def export_to_jsonl(self, output_file):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT c.id, c.timestamp, u.id, u.age_range, u.technical_proficiency, u.learning_preferences,
                       m.metadata_json, ct.role, ct.content, ct.timestamp
                FROM conversations c
                LEFT JOIN users u ON c.user_id = u.id
                LEFT JOIN metadata m ON c.id = m.conversation_id
                LEFT JOIN conversation_turns ct ON c.id = ct.conversation_id
                ORDER BY c.id, ct.timestamp
            ''')
            
            current_conversation = None
            entry = None
            with open(output_file, 'w') as f:
                for row in cursor.fetchall():
                    conversation_id, conv_timestamp, user_id, age_range, tech_prof, learn_pref, metadata_json, role, content, turn_timestamp = row
                    
                    if current_conversation != conversation_id:
                        if entry is not None:
                            f.write(json.dumps(entry) + '\n')
                        
                        current_conversation = conversation_id
                        metadata = json.loads(metadata_json) if metadata_json else {}
                        metadata.update({
                            "timestamp": conv_timestamp,
                            "conversation_id": conversation_id,
                            "user_id": user_id,
                            "context": {
                                "user_profile": {
                                    "user_id": user_id,
                                    "age_range": age_range,
                                    "technical_proficiency": tech_prof,
                                    "learning_preferences": learn_pref
                                }
                            }
                        })
                        entry = {
                            "conversation_id": conversation_id,
                            "metadata": metadata,
                            "turns": []
                        }
                    
                    if entry is not None:
                        entry["turns"].append({
                            "role": role,
                            "content": content,
                            "timestamp": turn_timestamp
                        })
                
                if entry is not None:
                    f.write(json.dumps(entry) + '\n')        
