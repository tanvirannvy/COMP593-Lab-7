"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import inspect
import sqlite3
from faker import Faker

def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE people
                 (id INTEGER PRIMARY KEY,
                  first_name TEXT,
                  last_name TEXT,
                  email TEXT,
                  city TEXT,
                  state TEXT)''')
    conn.commit()
    conn.close()

def populate_people_table():
    """Populates the people table with 200 fake people"""
    fake = Faker()
    people = []
    for i in range(200):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        city = fake.city()
        state = fake.state_abbr()
        people.append((first_name, last_name, email, city, state))
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.executemany('INSERT INTO people (first_name, last_name, email, city, state) VALUES (?, ?, ?, ?, ?)', people)
    conn.commit()
    conn.close()

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()
