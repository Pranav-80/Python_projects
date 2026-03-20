# 🐍 Python Projects Portfolio

A collection of console-based Python applications showcasing a range of software engineering skills, including Object-Oriented Programming (OOP), relational database management (MySQL), file I/O, and rule-based logic. 

## 📝 About the Repository
This repository contains three distinct Python projects built to demonstrate backend logic and data manipulation. They utilize external libraries like `tabulate` for clean console UI and `mysql-connector-python` for persistent data storage.

---

## 🛒 Project 1: E-Commerce Management System (`E-Commerce.py`)
A comprehensive storefront simulator that handles product querying, shopping cart state management, and basic checkout logic.

### ✨ Features
* **Inventory Management:** Browse all products or filter by Category, Price Range, and Rating.
* **Search Functionality:** Uses SQL `LIKE` queries to find products by partial name matches.
* **Cart System:** Add or remove items from a persistent shopping cart, complete with out-of-stock validation.
* **Dynamic Billing:** Calculates the total bill based on cart contents and simulates a checkout process.

---

## 📋 Project 2: SQL-Backed To-Do List (`ToDoList.py`)
A task management application that relies on a MySQL database to securely store, update, and track daily tasks and deadlines.

### ✨ Features
* **CRUD Operations:** Create, Read, Update, and Delete tasks directly from the database.
* **Smart Updating:** Users don't need exact task names to make edits; the program uses substring mapping to find and update tasks based on partial word matches.
* **Timestamping:** Automatically logs the exact date and time a task was modified using Python's `datetime` module.
* **Basic Authentication:** Requires a database username and password on startup to establish the connection.

---

## 🧬 Project 3: Organism Trait Selector (`Traits_selection.py`)
A rule-based text game and educational tool where users build a custom biological organism by selecting various evolutionary traits.

### ✨ Features
* **Interactive Data Collection:** Guides the user through selecting habitats, nutrient modes, reproduction types, and body structures using nested dictionaries.
* **Algorithmic Comparisons:** Compares the user's selected combination of traits against a hardcoded rule engine to find similar real-world organisms.
* **File Handling (I/O):** Automatically generates a text report (`NewOrganism.txt`) saving the custom organism's name and full biological breakdown.

---

## 📂 Repository Structure
```text
Python_projects/
├── E-Commerce.py          # E-commerce store and cart logic
├── ToDoList.py            # Database-driven task manager
├── Traits_selection.py    # Biological trait selection game
├── Ecommerce.sql          # DB schema and 90 mock products for E-Commerce app
├── TodoList.sql           # DB schema and structure for ToDoList app
└── README.md              # Project documentation and setup guide
```

---

## 🛠️ Tech Stack & Prerequisites
To run these scripts, you need Python 3.x and the following external libraries:
* `mysql-connector-python` (For database connections)
* `tabulate` (For formatting console tables)

---


