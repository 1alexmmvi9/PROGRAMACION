import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_path="data/database.db"):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def init_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Таблица задач
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'pending',
                priority INTEGER DEFAULT 1,
                due_date TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                ai_generated INTEGER DEFAULT 0
            )
        ''')
        
        # Таблица документов
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                filepath TEXT NOT NULL,
                category TEXT,
                tags TEXT,
                upload_date TEXT DEFAULT CURRENT_TIMESTAMP,
                ai_summary TEXT
            )
        ''')
        
        # Таблица шаблонов
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                content TEXT NOT NULL,
                type TEXT,
                variables TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    # CRUD для задач
    def create_task(self, title, description="", priority=1, due_date=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (title, description, priority, due_date)
            VALUES (?, ?, ?, ?)
        ''', (title, description, priority, due_date))
        conn.commit()
        task_id = cursor.lastrowid
        conn.close()
        return task_id
    
    def get_all_tasks(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks ORDER BY priority DESC, created_at DESC')
        tasks = cursor.fetchall()
        conn.close()
        return tasks
    
    def update_task_status(self, task_id, status):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (status, task_id))
        conn.commit()
        conn.close()
    
    def delete_task(self, task_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()