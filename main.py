#Application-Vault Copyright Mallard-Dash 2025

import sqlite3
from colorama import Fore, init
import datetime

class Main():
    def __init__ (self, name = None, contact=None, email=None, note=None, phone_number = 0):
        self.name = name
        self.contact = contact
        self.email = email
        self.phone_number = phone_number
        self.note = note
    
    def new_company(self):
        self.name = input("Write the name of the company: ")
        self.contact = input("Write the name of the contact: ")
        self.email = input("Add contact email: ")
        self.phone_number = input("Add contact phone_number: ")
        self.note = input("Add a note for this company: ")

        self.data = (self.name, self.contact, self.email, self.phone_number, self.note)
        print("New company created: ")
        for values in self.data:
            print(f"--{values}--")
        self.save_to_database()


    def database_connection(self):
        self.con = sqlite3.Connection("LIA.db")
        self.cur = self.con.cursor()
        return self.con, self.cur

    def close_database(self):
        return con.close()

    def save_to_database(self):
        advance = input("Save to database? (Y/N): ")
        if advance.upper() == "Y":
            sql = """
            INSERT INTO Companies (name, contact, email, phone_number, note) 
            VALUES (?, ?, ?, ?, ?)
            """
            self.database_connection()
            self.cur.execute(sql, self.data)
            self.con.commit()
            print ("Successfully saved!")
        elif advance.upper() == "N":
            return

    def search_for_company(self):
        self.database_connection()
        company_to_find = input("Enter a company name to search for: ")
        query = "SELECT * FROM Companies WHERE name LIKE ?"
        self.cur.execute(query, (company_to_find,))
        results = self.cur.fetchall()
        if not results:
            return (f"No companies found matching '{company_to_find}'.")
        else:
            print(f"Found {len(results)} matching companies (Press ENTER to go back):")
            for row in results:
                print (f"  - ID: {row[0]}, Name: {row[1]}, Contact: {row[2]}, Email: {row[3]}, Phone_number: {row[4]}, Note: {row[5]}")
                input()

    def show_spreadsheet(self):
        self.database_connection()
        query = "SELECT * FROM Companies"
        self.cur.execute(query)
        results = self.cur.fetchall()
        if not results:
            return (f"The table is empty")
        else:
            print(f"Found {len(results)} matching companies (Press ENTER to go back):")
            for row in results:
                print (f"  - ID: {row[0]}, Name: {row[1]}, Contact: {row[2]}, Email: {row[3]}, Phone_number: {row[4]}, Note: {row[5]}")
                input()


    def main_menu(self):
        while True:
            print(f"***Main-Menu***\n",
            "1. Look at the spreadsheet\n",
            "2. Search for a specific company\n",
            "3. Add new company\n",
            "4. Change specific values\n",
            "5. Exit")
            try:
                menu_choice = int(input("Please choose a choice from 1-5: "))
            except ValueError:
                print("Wrong value! Only integers are allowed!")
            if menu_choice == 1:
                self.show_spreadsheet()
            elif menu_choice == 2:
                self.search_for_company()
            elif menu_choice == 3:
                self.new_company()
            elif menu_choice == 4:
                self.sub_menu()
            elif menu_choice == 5:
                print("Logging off...")
                self.close_database()
                break
            else:
                print("Wrong input-choice, try again!")
                continue

    def sub_menu(self):
        while True:
            print(f"***Database-Menu***\n",
            "1. Update contact\n",
            "2. Update email\n",
            "3. Update phone-number\n",
            "4. Update note\n",
            "5. Back to main-menu")
            try:
                menu_choice = int(input("Please choose a choice from 1-5: "))
            except ValueError:
                print("Wrong value! Only integers are allowed!")
            if menu_choice == 1:
                pass
            elif menu_choice == 2:
                pass
            elif menu_choice == 3:
                pass
            elif menu_choice == 4:
                pass
            elif menu_choice == 5:
                print("Back to main-menu...")
                break
            else:
                print("Wrong input-choice, try again!")
                continue

test = Main()
test.main_menu()
