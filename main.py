#Application-Vault Copyright Mallard-Dash 2025

import sqlite3
from colorama import Fore, init

class Main():
    def __init__ (self, name, contact, email, note, phone_number = 0):
        self.name = name
        self.contact = contact
        self.email = email
        self.phone_number = phone_number
        self.note = note

    def new_company(self):

        self.data = (self.name, self.contact, self.email, self.phone_number, self.note)
        print("New company created: ")
        for values in data:
            print(f"--{values}--")

    def database_connection(self):
        self.con = sqlite3.Connection("LIA.db")
        self.cur = con.cursor()
        return con, cur

    def close_database(self):
        return con.close()

    def save_to_database(self):
        advance = input("Save to database? (Y/N): ")
        if advance.lower() == "Y":
            self.database_connection()
            self.cur.executemany("INSERT INTO movie VALUES(?, ?, ?, ?, ?)", self.data)
            self.con.commit()
        elif advance.lower == "N":
            pass    

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
                pass
            elif menu_choice == 2:
                pass
            elif menu_choice == 3:
                pass
            elif menu_choice == 4:
                self.sub_menu()
            elif menu_choice == 5:
                print("Logging off...")
                break
            else:
                print("Wrong input-choice, try again!")
                continue

    def sub_menu(self):
        while True:
            print(f"***Database-Menu***\n",
            "1. Change/Add contact\n",
            "2. Change/Add email\n",
            "3. Change/Add phone-number\n",
            "4. Change/Add note\n",
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

name = input("Write the name of the company: ")
contact = input("Write the name of the contact: ")
email = input("Add contact email: ")
phone_number = input("Add contact phone_number: ")
note = input("Add a note for this company: ")

test = Main(name=name, contact=contact, email=email, phone_number=phone_number, note=note)
test.new_company()