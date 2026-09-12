SpeedWearz Inventory Management System

A Python-based inventory management system built for CC4059NI/CS4051NI - Fundamentals of Computing coursework. The system manages shoe inventory data, handles buying (restocking) and selling operations, and generates invoices for both vendors and customers.

Overview

SpeedWearz reads shoe inventory data (Shoe ID, Name, Brand, Stock, Price, Origin) from a text file and allows users to either restock products from vendors or sell products to customers. The system validates all user input, updates stock levels in real-time, and generates timestamped invoice files for every transaction.

Features
Read and display shoe inventory from Information.txt
Buy (Restock) – Add stock from vendors with quantity and product validation
Sell – Process customer sales with stock availability checks
Automatic discount calculation on sales
Invoice generation saved as separate timestamped .txt files
Persistent stock updates written back to the inventory file
Input validation using try/except (numeric checks, phone number length, positive quantities, etc.)
Technologies Used
Python – core programming language
IDLE – development and testing environment
Text files – for data storage (inventory and invoices)
draw.io – used for flowchart design during planning
Data Structure

The project primarily uses Lists (a list of lists) to store and manage shoe inventory data. Each shoe record is split into a list of its attributes, and all records are stored inside one main list for easy looping, searching, and updating.

How to Run
Make sure Information.txt is in the same directory as the script, formatted as: ID,Name,Brand,Stock,Price,Origin
Run the main Python file:
   python main.py
Choose an option from the menu:
1 — Buy (Restock)
2 — Sell
3 — Quit Program
Follow the on-screen prompts to complete a transaction.
Invoices are automatically saved as text files (e.g., buy_invoice_<date>.txt, sale_invoice_<date>.txt).
Testing

The system was tested for:

Invalid (non-numeric) input handling
Invalid product ID and negative quantity handling
Multi-product purchase and bill generation
Multi-product sale and bill generation
Stock updates persisting correctly in the inventory file
Author

Diya Maharjan
