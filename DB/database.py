import sqlite3 
from classes.house import House
from classes.soldier import Soldier

class DatabaseManager:
    def __init__(self, db_name='HOME_MANGEMENT.db'):
        """Initialize database connection"""
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        
    def create_tables(self):
        try:    
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS soldier(
            PersonalId INTEGER PRIMARY KEY,
            firstName TEXT NOT NULL,
            lestName TEXT NOT NULL,
            Gender TEXT NOT NULL,
            city TEXT NOT NULL,                                        
            farKL INTEGER NOT NULL
            )""")
           
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS rooms(
            room_id INTEGER PRIMARY KEY,
            soldier TEXT NOT NULL,
            numRoom INTEGER NOT NULL ,
            numRoomId INTEGER,
            FOREIGN KEY (numRoom_id) REFERENCES persons(PersonalId)
            )""")
            self.connection.commit()
            print("Tables created successfully")
        except sqlite3.Error as e:
            print(f"Error while creating tables: {e}")

    def insert_soldier(self, soldier):
        self.cursor.execute(f"""
        INSERT INTO soldier(firstName,lestName,Gender,city,farKL)
        VALUES(?,?,?,?,?,?)""",(soldier.firstName , soldier.lestName,soldier.Gender,soldier.city,soldier.farKL))
        
        self.connection.commit()
  
    def insert_rooms(self, rooms):
        """Insert a rooms into database"""
        self.cursor.execute(f"""
        INSERT INTO rooms(,,)
        VALUES(?,?,?)""",(rooms., rooms., rooms.))
        
        self.connection.commit()
    
 
    
DatabaseManager().create_tables()
    


    




# car1 = Car(None, "Toyota", "Corolla", 2022, "Red", pers1.person_id)  # p1.person_id = 1
# db.insert_car(car1)


# 3. שמור הכל במסד נתונים SQLite3
