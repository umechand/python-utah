
# Assignment: HW9

import sqlite3
from enum import Enum


class Inventory_Col(Enum):
    INVENTORY_ID = 0
    PART_ID = 1


class Part_Col(Enum):
    PART_ID = 0
    PART_NAME = 1


class DBbase:
    _conn = None
    _cursor = None

    def __init__(self, db_name):
        self._db_name = db_name
        self.connect()

    def connect(self):
        self._conn = sqlite3.connect(self._db_name)
        self._cursor = self._conn.cursor()

    def execute_script(self, sql_string):
        self._cursor.executescript(sql_string)

    @property
    def get_cursor(self):
        return self._cursor

    @property
    def get_connection(self):
        return self._conn

    def close_db(self):
        self._conn.close()

    def reset_database(self):
        raise NotImplementedError("Must be implemented in the derived class")


class Parts(DBbase):
    def __init__(self):
        super().__init__("dbinventory.sqlite")

    def update(self, id, name):
        try:
            super().connect()
            super().get_cursor.execute("""update Parts set name = ? WHERE id = ?;""", (name, id,))
            super().get_connection.commit()
            print("Updated part successfully")
        except Exception as e:
            print("An error has occurred : {}".format(e))
        finally:
            super().close_db()

    def add(self, name):
        try:
            super().connect()
            super().get_cursor.execute("""insert or ignore into Parts(name) values (?);""", (name,))
            super().get_connection.commit()
            print("Added part successfully")
        except Exception as e:
            print("An error has occurred : {}".format(e))
        finally:
            super().close_db()

    def delete(self, id):
        try:
            super().connect()
            super().get_cursor.execute("""delete FROM Parts WHERE id = ?;""", (id,))
            super().get_connection.commit()
            print("Deleted part successfully")
            return True
        except Exception as e:
            print("An error has occurred : {}".format(e))
            return False
        finally:
            super().close_db()

    def fetch(self, id=None, part_name=None):
        # if Id is null (or None), then get everything, else get by id
        try:
            super().connect()
            if id is not None:
                return super().get_cursor.execute("""SELECT * FROM Parts WHERE id = ? ;""", (id,)).fetchone()
            elif part_name is not None:
                return super().get_cursor.execute("""SELECT id FROM Parts WHERE name = ? ;""", (part_name,)).fetchone()
            else:
                return super().get_cursor.execute("""SELECT * FROM Parts;""").fetchall()
        except Exception as e:
            print("An error has occurred : {}".format(e))
        finally:
            super().close_db()

    def reset_database(self):
        sql = """
        DROP TABLE IF EXISTS Parts;
        CREATE TABLE Parts (
            id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name varchar(50) UNIQUE
        );
        """
        super().execute_script(sql)


parts = Parts()
parts.reset_database()
parts.add('mobiles')
parts.add('laptops')
parts.add('bottle')
parts.add('bag')
parts.add('filter')
parts.delete(3)
result = parts.fetch()
print(result)


class Inventory(Parts):
    # def __init__(self):
    #     super().__init__("inventory.sqlite")

    def update(self, id, quantity, current_price):
        try:
            super().connect()
            super().get_cursor.execute("""update Inventory set quantity = ?, current_price = ? WHERE  id= ?;""",
                                       (quantity, current_price, id,))
            super().get_connection.commit()
            print("Updated inventory successfully")
            return True
        except Exception as e:
            print("An error has occurred : {}".format(e))
            return False
        finally:
            super().close_db()

    def add(self, name, part_id, quantity, current_price):
        try:
            super().add(name)
        except Exception as e:
            print("An error has occurred in the part class: {}".format(e))
        else:
            try:
                # get part id from parts table
                p_id = super().fetch(part_name=name)
                if p_id is not None:
                    super().connect()
                    super().get_cursor.execute(
                        """insert or ignore into Inventory(part_id, quantity, current_price) values (?, ? , ?);""",
                        (p_id[Part_Col.PART_ID.value], quantity, current_price,))
                    super().get_connection.commit()
                    print("Added inventory successfully")
                else:
                    raise Exception("An id of this part name not found!")
            except Exception as e:
                print("An error has occurred : {}".format(e))
            finally:
                super().close_db()

    def delete(self, inventory_id):
        part_id = -1
        try:
            # retrieve part id based from the Inventory id
            rval = self.fetch(inventory_id)
            if rval is not None:
                # Set the part_id and delete from Parts
                part_id = rval[Inventory_Col.PART_ID.value]
                rsts = super().delete(part_id)
                if rsts is False:
                    raise Exception("Delete method inside parts failed. Delete action is aborted")
        except Exception as e:
            print("An error occurred when fetching from parts: {}".format(e))
        else:
            try:
                super().connect()
                super().get_cursor.execute("""delete FROM Inventory WHERE id = ?;""", (inventory_id,))
                super().get_connection.commit()
                print("Deleted inventory successfully")
            except Exception as e:
                print("An error has occurred : {}".format(e))
            finally:
                super().close_db()

    def fetch(self, id=None):
        # if Id is null (or None), then get everything, else get by id
        try:
            super().connect()
            if id is not None:
                # return super().get_cursor.execute("""SELECT * FROM Inventory WHERE id = ? ;""", (id,)).fetchall()
                return super().get_cursor.execute("""SELECT Inventory.id, part_id, p.name,quantity, current_price
                                                     FROM Inventory
                                                     INNER JOIN Parts as p
                                                     ON Inventory.part_id = p.id
                                                     WHERE Inventory.id = ?;
                                                     """, (id,)).fetchone()
            else:
                # return super().get_cursor.execute("""SELECT * FROM Inventory;""").fetchall()
                return super().get_cursor.execute("""SELECT part_id, p.name,quantity, current_price 
                                         FROM Inventory 
                                         INNER JOIN Parts as p 
                                         ON Inventory.part_id = p.id;
                                         """).fetchall()
        except Exception as e:
            print("An error has occurred : {}".format(e))
        finally:
            super().close_db()

    def reset_database(self):
        sql = """
        DROP TABLE IF EXISTS Inventory;

        CREATE TABLE Inventory  (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            part_id  INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            current_price varchar(20)
        );
        """
        super().execute_script(sql)


inventory = Inventory()
inventory.reset_database()
inventory.delete(3)
inventory.add('pepsi', 3, 12, '2.99')
inventory.add('Desktop', 4, 4, '5.34')
inventory.update(2, 2, '43.56')
inventory.delete(3)
result = inventory.fetch(3)
# print(len(result))
print(result)

inv_option = {
    "get": "Get all inventory",
    "getby": "Get inventory by Id",
    "update": "Update inventory",
    "add": "Add inventory",
    "delete": "delete inventory",
    "exit": "exit the program"
}

user_selection = ""
while user_selection != "exit":
    print("********* Option List *********")
    for option in inv_option.items():
        print(option)
    user_selection = input("Select an option: ")
    inventory = Inventory()

    if user_selection == 'get':
        my_inventory = inventory.fetch()
        for item in my_inventory:
            print(item)
        print("********* Done! *********\n")
    elif user_selection == 'getby':
        inv_id = input("Enter inventory id: ")
        my_inventory = inventory.fetch(inv_id)
        print(my_inventory)
        print("\n")
    elif user_selection == 'update':
        inv_id = input("Enter inventory id: ")
        quantity = input("Enter quantity amount: ")
        price = input("Enter selling price: ")
        inventory.update(inv_id, quantity, price)
        print(inventory.fetch(inv_id))
        print("********* Done! *********\n")
    elif user_selection == 'add':
        name = input("Enter part name: ")
        part_id = input("Enter the part_id:")
        quantity = input("Enter quantity amount: ")
        price = input("Enter selling price: ")
        inventory.add(name, part_id, quantity, price)
        print("********* Done! *********\n")
    elif user_selection == 'delete':
        inv_id = input("Enter inventory id: ")
        inventory.delete(inv_id)
        print("********* Done! *********\n")
    else:
        if user_selection != 'exit':
            print("Invalid selection. Please try again.")
