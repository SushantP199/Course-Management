import sqlite3 as sql


# functionality
class DatabaseManage(object):

    def __init__(self):
        global con
        try:
            con = sql.connect('courses.db')
            with con:
                cur = con.cursor()
                query = "CREATE TABLE IF NOT EXISTS course(ID integer PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)"
                cur.execute(query)
        except Exception:
            print("\n\nXXX Database connection failed... XXX")

    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                query = "INSERT INTO course(name, description, price, is_private) \
                    VALUES (?, ?, ?, ? )"
                cur.execute(query, data)
                return True
        except Exception:
            return False

    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False

    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                query = "DELETE FROM course WHERE id = ?"
                cur.execute(query, [id])
                return True
        except Exception:
            return False


# User Interface
def main():
    db = DatabaseManage()
    if not db:
        return
    print("#" * 55)
    print("\n\t\t:: COURSE MANAGEMENT LAB:: \n")
    print("#" * 55)
    print("*" * 55)
    print("\t\t  :: User Manual :: \n")
    print("\t\t1] Insert a new course")
    print("\t\t2] Show all courses")
    print("\t\t3] Delete a new course")
    print("\t\t4] Exit the lab")
    print("*" * 55)
    ch = input("\n Enter your choice : ")
    if ch == "1":
        name = input("\n Enter course name : ")
        description = input(" Enter course description : ")
        price = input(" Enter course price : ")
        private = input(" Is this course private (0 / 1): ")
        data = [name, description, price, private]

        if db.insert_data(data):
            print("*** Course inserted successfully...")
        else:
            print("XXX Something went wrong... XXX")
    elif ch == "2":
        print("\n ### COURSES ###")
        print("*" * 55)
        for index, item in enumerate(db.fetch_data()):
            print(f"\nSR. NO. : {index + 1} =>")
            print(f"COURSE ID   : {item[0]}")
            print(f"NAME        : {item[1]}")
            print(f"DESCRIPTION : {item[2]}")
            print(f"PRICE       : ${item[3]}")
            private = 'YES' if item[4] else 'NO'
            print(f"PRIVATE     : {private}")
            print("\n")
    elif ch == "3":
        record_id = input("\n Enter course id : ")
        if db.delete_data(record_id):
            print("*** Course deleted successfully...")
        else:
            print("XXX Something went wrong... XXX")
    elif ch == "4":
        print("*"*55)
        print("\t\t\t\t\t---Thanking you")
        exit()
    else:
        print("\n INVALID CHOICE (VALID CHOICES ARE 1, 2, 3 & 4)")
        ch = input("\n Enter your choice : ")


if __name__ == '__main__':
    while True:
        main()
