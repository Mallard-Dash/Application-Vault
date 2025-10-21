# Application-Vault

A lightweight, terminal-based contact manager designed for tracking companies and contacts during internship or job searches.  
Built with **SQLite** and **Colorama** for colored terminal output.

---

## 🧭 Overview

**Application-Vault** allows you to:
- Add companies with contact details and notes  
- Search for companies using flexible `LIKE` queries  
- View all stored companies in a simple "spreadsheet" view  
- Update specific fields for a chosen company safely via its `rowid`  
- Navigate everything through a clean, menu-driven interface

---

## 🗄️ Database Schema

- Database file: `LIA.db`  
- Table name: `Companies`  
- Uses SQLite’s internal `rowid` for secure record updates  

Before running the program for the first time, make sure the database table exists.  
You can create it manually with this SQL command:

```sql
CREATE TABLE IF NOT EXISTS Companies (
  name TEXT NOT NULL,
  contact TEXT,
  email TEXT,
  phone_number TEXT,
  note TEXT
);
'''
Mallard-Dash © 2025

Developed by Vincent — designed as a practical tool for organizing internship applications and company contacts.
