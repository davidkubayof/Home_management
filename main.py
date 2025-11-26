from DB.database import DatabaseManager

import sqlite3
import csv


class SoldierManagementSystem:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.db_manager.create_tables()
    

    def add_Soldier(self,Soldier: Soldier):
        """Add new Soldier"""
        self.db_manager.insert_Soldier(Soldier)
           
    def add_House(self,House: House):
        """Add new House"""
        self.db_manager.insert_House(House)
    
 
                
if __name__ == "__main__":
    SoldierManagementSystem()
