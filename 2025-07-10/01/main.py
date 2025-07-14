import sqlite3
def create_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    conn.commit()
    conn.close()
    print("Database and table created successfully.")
def insert_user(name, age):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
    print(f"User {name} inserted successfully.")
def fetch_users():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return users
def main():
    create_database()
    insert_user("Alice", 30)
    insert_user("Bob", 25)
    users = fetch_users()
    print("Users in the database:")
    for user in users:
        print(user)
if __name__ == "__main__":
    main()
# This code creates a SQLite database, inserts some user data, and fetches it to display
# the users in the database. It uses the sqlite3 module to handle database operations.
# The database is named 'users.db' and contains a table 'users' with columns for id, name, and age.
# The main function orchestrates the creation of the database, insertion

def modify_user(user_id, name, age):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, user_id))
    conn.commit()
    conn.close()
    print(f"User with ID {user_id} updated successfully.")
# of users, and fetching of user data.
# The modify_user function allows updating an existing user's information
# by specifying the user ID, new name, and new age.
def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f"User with ID {user_id} deleted successfully.")
# The delete_user function allows deleting a user from the database by specifying the user ID.
# The code is structured to be run as a script, with the main function being called when
# the script is executed directly. This allows for easy testing and modification of the database.
delete_user(1)  # Example of deleting a user with ID 1
modify_user(2, "Bob Smith", 26)  # Example of modifying user with ID 2

print("Database operations completed successfully.")
print("Current users after modifications:")
users = fetch_users()
for user in users:
    print(user)


