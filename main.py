#Application-Vault Copyright Mallard-Dash 2025

import sqlite3
from colorama import Fore, init
# No need to import Style and init separately
init(autoreset=True)

class Main():
    def __init__ (self, name = None, contact=None, email=None, note=None, phone_number = None):
        self.name = name
        self.contact = contact
        self.email = email
        self.phone_number = phone_number
        self.note = note
        # These are not needed for every method, so we initialize them here
        self.con = None
        self.cur = None
    
    def new_company(self):
        self.name = input("Write the name of the company: ")
        self.contact = input("Write the name of the contact: ")
        self.email = input("Add contact email: ")
        self.phone_number = input("Add contact phone_number: ")
        self.note = input("Add a note for this company: ")

        self.data = (self.name, self.contact, self.email, self.phone_number, self.note)
        print(Fore.GREEN + "New company created: ")
        for value in self.data:
            print(f"--{value}--")
        self.save_to_database()


    def database_connection(self):
        # Corrected to sqlite3.connect and using a consistent DB name
        self.con = sqlite3.connect("LIA.db", timeout=10)
        self.cur = self.con.cursor()

    def close_database(self):
        # Check if a connection exists before trying to close it
        if self.con:
            self.con.close()

    def save_to_database(self):
        advance = input(Fore.YELLOW + "Save to database? (Y/N): ")
        if advance.upper() == "Y":
            sql = """
            INSERT INTO Companies (name, contact, email, phone_number, note) 
            VALUES (?, ?, ?, ?, ?)
            """
            try:
                self.database_connection()
                self.cur.execute(sql, self.data)
                self.con.commit()
                print (Fore.GREEN + "Successfully saved!")
            except sqlite3.Error as e:
                print(Fore.RED + f"Database error: {e}")
            finally:
                self.close_database()
        elif advance.upper() == "N":
            return

    def search_for_company(self):
        try:
            self.database_connection()
            company_to_find = input("Enter a company name to search for: ")
            # Use LIKE for a more flexible search
            query = "SELECT * FROM Companies WHERE name LIKE ?"
            self.cur.execute(query, ('%' + company_to_find + '%',))
            results = self.cur.fetchall()
            if not results:
                print (Fore.RED + f"No companies found matching '{company_to_find}'.")
            else:
                print(f"Found {len(results)} matching companies:")
                # Loop to print all results first
                for row in results:
                    print (f"  - ID: {row[0]}, Name: {row[1]}, Contact: {row[2]}, Email: {row[3]}, Phone_number: {row[4]}, Note: {row[5]}")
                input("Press ENTER to go back...")
        except sqlite3.Error as e:
            print(Fore.RED + f"Database error: {e}")
        finally:
            self.close_database()


    def show_spreadsheet(self):
        try:
            self.database_connection()
            query = "SELECT * FROM Companies"
            self.cur.execute(query)
            results = self.cur.fetchall()
            if not results:
                print (Fore.YELLOW + "The table is empty")
            else:
                print(f"Showing all {len(results)} companies:")
                # Loop to print all results first
                for row in results:
                    print (f"  - ID: {row[0]}, Name: {row[1]}, Contact: {row[2]}, Email: {row[3]}, Phone_number: {row[4]}, Note: {row[5]}")
                input("Press ENTER to go back...")
        except sqlite3.Error as e:
            print(Fore.RED + f"Database error: {e}")
        finally:
            self.close_database()


    def update_company_record(self): # CHANGED: Added 'self' to make it a class method
        """
        Safely updates a single company record by first identifying its unique rowid.
        """
        try:
            # CHANGED: Uses the class's connection method
            self.database_connection()

            # --- PART 1: Find the specific company record ---
            search_name = input("What company do you want to edit? ")
            if not search_name:
                print(Fore.YELLOW + "Search cancelled.")
                return

            # Search for the company and get its unique rowid
            self.cur.execute("SELECT rowid, name, contact FROM Companies WHERE Name LIKE ?", ('%' + search_name + '%',))
            results = self.cur.fetchall()
            
            target_row_id = None

            if not results:
                print(Fore.YELLOW + f"Sorry, no company found with a name like '{search_name}'.")
                return
            elif len(results) == 1:
                target_row_id = results[0][0] # The 'rowid'
                print(Fore.CYAN + f"Found one match: {results[0][1]} (Contact: {results[0][2]})")
            else:
                print(Fore.CYAN + "Found multiple matches. Please choose the specific one to edit:")
                for row in results:
                    print(f"  ID: {row[0]} -> Name: {row[1]}, Contact: {row[2]}")
                
                try:
                    choice = int(input("Enter the ID of the exact company you want to edit: "))
                    if choice in [row[0] for row in results]:
                        target_row_id = choice
                    else:
                        print(Fore.RED + "Invalid ID selected.")
                        return
                except ValueError:
                    print(Fore.RED + "Invalid input. Please enter a numerical ID.")
                    return

            # --- PART 2: Get user's desired change ---
            # Corrected to 'phone_number' to match your schema
            allowed_columns = ["name", "contact", "email", "phone_number", "note"]
            
            user_choice = input(f"What field to edit? ({', '.join(allowed_columns)}): ")
            
            column_to_edit = user_choice.lower()
            if column_to_edit not in allowed_columns:
                print(Fore.RED + f"Error: Invalid field '{user_choice}'.")
                return

            new_value = input(f"Enter the new value for {column_to_edit}: ")

            # --- PART 3: Execute the safe update using the unique ID ---
            sql_query = f"UPDATE Companies SET {column_to_edit} = ? WHERE rowid = ?"
            self.cur.execute(sql_query, (new_value, target_row_id))
            
            self.con.commit()
            print(Fore.GREEN + f"\nSuccess! Record {target_row_id} has been updated.")

        except sqlite3.Error as e:
            print(Fore.RED + f"A database error occurred: {e}")
            if self.con:
                self.con.rollback()
        finally:
            # CHANGED: Uses the class's close method
            self.close_database()


    def main_menu(self):
        while True:
            print(f"\n***Main-Menu***\n",
            "1. Look at the spreadsheet\n",
            "2. Search for a specific company\n",
            "3. Add new company\n",
            "4. Change specific values\n",
            "5. Exit")
            try:
                menu_choice = int(input("Please choose a choice from 1-5: "))
            except ValueError:
                print(Fore.RED + "Wrong value! Only integers are allowed!")
                continue # Use continue to re-run the loop

            if menu_choice == 1:
                self.show_spreadsheet()
            elif menu_choice == 2:
                self.search_for_company()
            elif menu_choice == 3:
                self.new_company()
            elif menu_choice == 4:
                self.update_company_record()
            elif menu_choice == 5:
                print("Logging off...")
                # No need to close DB here, each function handles its own connection
                break
            else:
                print(Fore.RED + "Wrong input-choice, try again!")
                continue

test = Main()
test.main_menu()
