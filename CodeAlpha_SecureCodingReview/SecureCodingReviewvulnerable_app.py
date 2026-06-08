
# vulnerable_app.py
# Intentionally Vulnerable Application for Security Review

import sqlite3

print("=== Vulnerable Login System ===")

username = input("Username: ")
password = input("Password: ")

# SQL Injection Vulnerability
query = (
    "SELECT * FROM users WHERE username='"
    + username
    + "' AND password='"
    + password
    + "'"
)

print("\nGenerated SQL Query:")
print(query)

# Hardcoded credentials
admin_user = "admin"
admin_pass = "admin123"

if username == admin_user and password == admin_pass:
    print("Login Successful")
else:
    print("Access Denied")

# XSS Vulnerability Example
print("\n=== Comment Section ===")

comment = input("Enter your comment: ")

print("\nUser Comment Displayed:")
print(comment)

# Example malicious payload:
# <script>alert('XSS')</script>
