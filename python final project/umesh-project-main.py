import sqlite3


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

# Admin class inherits DB base for Execution of sql queries.


class Admin(DBbase):
    def __init__(self):
        super().__init__("inventory_db.sqlite")

# Admin login method performs the admin login

    def admin_login(self, username, password):
        try:
            super().connect()
            super().get_cursor.execute("""insert or ignore into admin(uname, pwd) values (?,?);""",
                                       (username, password))
            super().get_connection.commit()
            print("Admin account created successfully")
        except Exception as e:
            print("An error has occurred : {}".format(e))
        finally:
            super().close_db()

    # login auth method performs the  login authentication

    def login_auth(self, username=None, password=None):
        try:
            super().connect()
            if uname is not None and pwd is not None:
                return super().get_cursor.execute("""SELECT * FROM admin WHERE uname = ? and pwd = ? ;""",
                                                  (username, password,)).fetchone()
            else:
                return super().get_cursor.execute("""SELECT * FROM admin;""").fetchall()
        except Exception as e:
            print("An error has occurred : {}".format(e))
        finally:
            super().close_db()

    # Below method used to perform reset database

    def reset_database(self):
        sql = """
        DROP TABLE IF EXISTS admin;
        CREATE TABLE admin (
            uname   varchar(5) NOT NULL PRIMARY KEY,
            pwd varchar(5)
        );
        """
        super().execute_script(sql)

# Admin options inheritance from DB base


class AdminOptions(DBbase):
    def __init__(self):
        super().__init__("inventory_db.sqlite")

# Below methods to perform  CRUD operations from Admin perspective update accommodation

    def update_accommodation(self, accommodation_id, accommodation_name, penthouse_suite_price, general_suite_price):
        try:
            super().connect()
            super().get_cursor.execute(
                """update accommodation set accommodation_name = ?, penthouse_suite_price = ?, general_suite_price = ?
             WHERE accommodation_id = ?;""", (accommodation_name, penthouse_suite_price, general_suite_price,
                                              accommodation_id))
            super().get_connection.commit()
            print("Updated accommodation successfully")
        except Exception as e:
            print("An error has occurred : {}".format(e))
        finally:
            super().close_db()

    # Below methods to perform add accommodation

    def add_accommodation(self, accommodation_name, penthouse_suite_price, general_suite_price):
        try:
            super().connect()
            super().get_cursor.execute(
                """insert or ignore into accommodation(accommodation_name, penthouse_suite_price, general_suite_price) 
                values (?,?,?);""",
                (accommodation_name, penthouse_suite_price, general_suite_price))
            super().get_connection.commit()
            print("Added accommodation successfully")
        except Exception as e:
            print("An error has occurred : {}".format(e))
        finally:
            super().close_db()

# Below methods to perform delete accommodation

    def delete_accommodation(self, accommodation_id):
        try:
            super().connect()
            super().get_cursor.execute("""delete FROM accommodation WHERE accommodation_id = ?;""", (accommodation_id,))
            super().get_connection.commit()
            print("Deleted accommodation successfully")
            return True
        except Exception as e:
            print("An error has occurred : {}".format(e))
            return False
        finally:
            super().close_db()

# Below method to perform fetch accommodation

    def fetch_accommodation(self, accommodation_id=None):
        # if Id is null (or None), then get everything, else get by id
        try:
            super().connect()
            if accommodation_id is not None:
                return super().get_cursor.execute("""SELECT * FROM accommodation WHERE accommodation_id = ? ;""",
                                                  (accommodation_id,)).fetchone()
            else:
                return super().get_cursor.execute("""SELECT * FROM accommodation;""").fetchall()
        except Exception as e:
            print("An error has occurred : {}".format(e))
        finally:
            super().close_db()

# Below method used to perform reset the accommodation table

    def reset_accommodation_table(self):
        sql = """
        DROP TABLE IF EXISTS accommodation;
        CREATE TABLE accommodation (
            accommodation_id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            accommodation_name varchar(50) not null,
            penthouse_suite_price float not null, 
            general_suite_price float not null
        );
        """
        super().execute_script(sql)
        print("Reset accommodation Data successfully")

# AdminMenu inherits from AdminOptions to perform CRUD operations Add,update,Delete,Fetch


class AdminMenu(AdminOptions):
    def admin_option_menu(self):
        accommodation_admin_option = {
            "1": "Add accommodation",
            "2": "Update accommodation",
            "3": "Delete accommodation",
            "4": "Fetch accommodation",
            "5": "Fetch accommodation By ID",
            "exit": "exit to Main Menu"
        }
        accommodation_admin_selection = ""
        while accommodation_admin_selection != "exit":
            print("********* Admin Menu *********")
            for option in accommodation_admin_option.items():
                print(option)
            accommodation_admin_selection = input("Select an option: ")

            admin_options = AdminOptions()
            if accommodation_admin_selection == '1':
                accommodation_name = input("Enter the accommodation name: ")
                penthouse_suite_price = input("Enter penthouse suite price: ")
                general_suite_price = input("Enter General suite price: ")
                super().add_accommodation(accommodation_name, penthouse_suite_price, general_suite_price)
            elif accommodation_admin_selection == '2':
                accommodation_id = input("Enter accommodation id: ")
                cas = super().fetch_accommodation(accommodation_id)
                if cas is not None:
                    accommodation_name = input("Enter accommodation name: ")
                    penthouse_suite_price = input("Enter penthouse suite price: ")
                    general_suite_price = input("Enter General suite price: ")
                    super().update_accommodation(accommodation_id, accommodation_name, penthouse_suite_price, general_suite_price)
                else:
                    print("Accommodation Id not found")
            elif accommodation_admin_selection == '3':
                accommodation_id = input("Enter accommodation ID: ")
                cas = super().fetch_accommodation(accommodation_id)
                if cas is not None:
                    super().delete_accommodation(accommodation_id)
                else:
                    print("Accommodation Id not found")
            elif accommodation_admin_selection == '4':
                accommodation = super().fetch_accommodation()
                if len(accommodation) != 0:
                    for i in accommodation:
                        print(i)
                else:
                    print("No accommodations")
            elif accommodation_admin_selection == '5':
                accommodation_id = input("Enter the Accommodation ID: ")
                cas = super().fetch_accommodation(accommodation_id)
                if cas is not None:
                    accommodation = super().fetch_accommodation(accommodation_id)
                    print(accommodation)
                else:
                    print("Accommodation Id not found")
            elif accommodation_admin_selection == '6':
                super().reset_accommodation_table()
            else:
                if accommodation_admin_selection != 'exit':
                    print("Invalid selection. Please try again.")

# Customer options inherits from DB base
# it has 6 methods with different functionalities add,update,fetch,delete


class CustomerOptions(DBbase):
    def __init__(self):
        super().__init__("inventory_db.sqlite")

# Below method to perform update reservation

    def update_reservation(self, reservation_id, first_name, last_name, email, reservation_type, no_of_persons,
                           total_price):
        try:
            super().connect()
            super().get_cursor.execute("""update reservation set first_name = ?, last_name = ?, email = ?,
             reservation_type = ?,no_of_persons = ?,total_price = ? WHERE reservation_id = ?;""", (first_name, last_name, email, reservation_type, no_of_persons, total_price, reservation_id,))
            super().get_connection.commit()
            print("Your Reservation is updated sucessfully")
        except Exception as e:
            print("An error has occurred : {}".format(e))
        finally:
            super().close_db()

# Below method to perform add reservation

    def add_reservation(self, first_name, last_name, email, reservation_type, no_of_persons, total_price):
        try:
            super().connect()
            super().get_cursor.execute("""insert or ignore into reservation(first_name, last_name, email, 
            reservation_type, no_of_persons, total_price) values (?,?,?,?,?,?);""", (first_name, last_name, email, reservation_type, no_of_persons, total_price,))
            super().get_connection.commit()
            print("Your reservation is sucessfully added")
        except Exception as e:
            print("An error has occurred : {}".format(e))
        finally:
            super().close_db()

# Below method to perform delete reservation

    def delete_reservation(self, reservation_id):
        try:
            super().connect()
            super().get_cursor.execute("""delete FROM reservation WHERE reservation_id = ?;""", (reservation_id,))
            super().get_connection.commit()
            print("Your reservation deleted successfully")
            return True
        except Exception as e:
            print("An error has occurred : {}".format(e))
            return False
        finally:
            super().close_db()

# Below method to perform fetch reservation

    def fetch_reservation(self, reservation_id=None):
        # if Id is null (or None), then get everything, else get by id
        try:
            super().connect()
            if reservation_id is not None:
                return super().get_cursor.execute("""SELECT * FROM reservation WHERE reservation_id = ? ;""", (reservation_id,)).fetchone()
            else:
                return super().get_cursor.execute("""SELECT * FROM reservation;""").fetchall()
        except Exception as e:
            print("An error has occurred : {}".format(e))
        finally:
            super().close_db()

# Below method to calculate the price

    def reservation_price_cal(self, accommodation_id, no_of_persons):

        admin_options = AdminOptions()
        accommodation_by_id = admin_options.fetch_accommodation(accommodation_id)

        class_option = {
            "1": "Penthouse Suite",
            "2": "General Suite"
        }
        for opt in class_option.items():
            print(opt)
        class_selection = input("Select an option: ")
        if class_selection == "1":
            reservation_type = "penthouse_suite"
            penthouse_suite_price = accommodation_by_id[2]
            total_price = int(no_of_persons) * penthouse_suite_price
            reservation_price = [reservation_type, total_price]
            return reservation_price
        elif class_selection == "2":
            reservation_type = "General_suite"
            general_suite_price = accommodation_by_id[3]
            total_price = int(no_of_persons) * general_suite_price
            reservation_price = [reservation_type, total_price]
            return reservation_price
        else:
            print("Invalid selection. Please try again.")

# Below method to reset reservation table

    def reset_reservation_table(self):
        sql = """
        DROP TABLE IF EXISTS reservation;
        CREATE TABLE reservation (
            reservation_id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            first_name varchar(50) not null,
            last_name varchar(50) not null,
            email varchar(50) not null,
            reservation_type varchar(50) not null,
            no_of_persons INTEGER not null,
            total_price float not null
        );
        """
        super().execute_script(sql)

# Reservation Menu inherits from Customer options
# and perform CRUD operations from the user perspective, Book , update, cancel, Fetch


class ReservationMenu(CustomerOptions):
    def reservation_option_menu(self):
        accommodation_reservation_option = {
            "1": "Book a accommodation",
            "2": "update reservation",
            "3": "Cancel reservation",
            "4": "Fetch reservation",
            "5": "Fetch reservation By ID",
            "exit": "exit to Main Menu"
        }
        accommodation_reservation_selection = ""
        while accommodation_reservation_selection != "exit":
            print("********* reservation Menu *********")
            for option in accommodation_reservation_option.items():
                print(option)
            accommodation_reservation_selection = input("Select an option: ")

            if accommodation_reservation_selection == '1':
                admin_options = AdminOptions()
                accommodation = admin_options.fetch_accommodation()
                if len(accommodation) != 0:
                    for i in accommodation:
                        print(i)
                else:
                    print("No accommodations")
                    break
                accommodation_id = input("Enter accommodation ID to proceed reservation: ")
                cas = admin_options.fetch_accommodation(accommodation_id)
                if cas is not None:
                    first_name = input("Enter First Name: ")
                    last_name = input("Enter Last Name: ")
                    email = input("Enter Email: ")
                    no_of_persons = input("Enter Number Of Persons: ")
                    reservation_price = reservation_options.reservation_price_cal(accommodation_id, no_of_persons)
                    reservation_type = reservation_price[0]
                    total_price = reservation_price[1]
                    super().add_reservation(first_name, last_name, email, reservation_type, no_of_persons, total_price)
                else:
                    print("accommodation_id not found")
            elif accommodation_reservation_selection == '2':
                reservation_id = input("Enter reservation Id to update: ")
                cas = super().fetch_reservation(reservation_id)
                if cas is not None:
                    accommodation = admin_options.fetch_accommodation()
                    if len(accommodation) != 0:
                        for i in accommodation:
                            print(i)
                    else:
                        print("No accommodations")
                    accommodation_id = input("Enter accommodation ID to update reservation: ")
                    cas = admin_options.fetch_accommodation(accommodation_id)
                    if cas is not None:
                        first_name = input("Enter First Name: ")
                        last_name = input("Enter Last Name: ")
                        email = input("Enter your Email: ")
                        no_of_persons = input("Enter the Number of Persons : ")
                        reservation_price = reservation_options.reservation_price_cal(accommodation_id, no_of_persons)
                        reservation_type = reservation_price[0]
                        total_price = reservation_price[1]
                        super().update_reservation(reservation_id, first_name, last_name, email, reservation_type, no_of_persons, total_price)
                    else:
                        print("Accommodation Id not found")
                else:
                    print("No reservations")

            elif accommodation_reservation_selection == '3':
                reservation_id = input("Enter reservation ID: ")
                cas = super().fetch_reservation(reservation_id)
                if cas is not None:
                    super().delete_reservation(reservation_id)
                else:
                    print("reservation_id not found")

            elif accommodation_reservation_selection == '4':
                reservation = super().fetch_reservation()
                if len(reservation) != 0:
                    for i in reservation:
                        print(i)
                else:
                    print("No reservations")
            elif accommodation_reservation_selection == '5':
                reservation_id = input("Enter reservation ID: ")
                reservation = super().fetch_reservation(reservation_id)
                if reservation is not None:
                    print(reservation)
                else:
                    print("reservation ID not found")
            else:
                if accommodation_reservation_selection != 'exit':
                    print("Invalid selection. Please try again.")


admin = Admin()
admin.reset_database()
admin.admin_login('admin', 'admin')
admin_menu = AdminMenu()
admin_menu.reset_accommodation_table()
reservation_options = CustomerOptions()
reservation_options.reset_reservation_table()

# Login is based on the role Admin and customer

customer_option = {
    "1": "Admin",
    "2": "customer",
    "exit": "exit the program"
}
accommodation_selection = ""

while accommodation_selection != "exit":
    print("********* accommodation  reservation System *********")
    for option in customer_option.items():
        print(option)
    accommodation_selection = input("Select an option: ")

    admin = Admin()
    admin_menu = AdminMenu()
    reservation_menu = ReservationMenu()
    if accommodation_selection == '1':
        uname = input("username: ")
        pwd = input("Password : ")
        auth = admin.login_auth(uname, pwd)
        if auth is not None:
            print("Login Successful")
        else:
            print("Login UnSuccessful")
            break
        admin_menu.admin_option_menu()
    elif accommodation_selection == '2':
        reservation_menu.reservation_option_menu()
    else:
        if accommodation_selection != 'exit':
            print("Invalid selection. Please try again.")



