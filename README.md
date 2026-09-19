# Library-Management-System
Python CLI library manager with persistent JSON file storage. Supports book additions, stock checking, member profiles, and dynamic book tracking features.
# Library Management System

A lightweight, terminal-based **Library Management System** built with Python. The application uses localized JSON files for data persistence, ensuring that your library's inventory and registered members are securely saved even after the application closes.

## 🚀 Features

- **User Authentication:** Automatically greets existing members or creates a new member profile on login.
- **Inventory Management:** Add new titles to the library collection without duplicate entries.
- **Real-Time Tracking:** Dynamically updates book availability as titles are checked out.
- **Persistent Storage:** Keeps records of both available stock (`Books.json`) and individual member loan logs (`members.json`).
- **Comprehensive Dashboard:** View a list of all current books or check which member has borrowed which titles.

## 🛠️ Tech Stack

- **Language:** Python  3.14.7 
- **Storage:** JSON ( `json` module)

## 📁 File Structure

```text
├── library.py          # Main application source code
├── Books.json          # Holds the list of books available to borrow
└── members.json        # Holds registered members and their borrowed titles
```


