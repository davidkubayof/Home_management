from DB.database import DatabaseManager

import sqlite3
import csv


class SoldierManagementSystem:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.db_manager.create_tables()
    

                
if __name__ == "__main__":
    SoldierManagementSystem()
