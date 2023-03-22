"""
Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.

Usage:
 python old_people.py
"""
import os
import inspect 
import sqlite3
import csv

def main():
    global db_path
    script_dir = get_script_dir()
    db_path = os.path.join(script_dir, 'social_network.db')

    # Get the names and ages of all old people
    old_people_list = get_old_people()

    # Print the names and ages of all old people
    print_name_and_age(old_people_list)

    # Save the names and ages of all old people to a CSV file
    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''SELECT first_name, last_name, age
                 FROM people
                 WHERE age >= 50''')
    old_people_list = c.fetchall()
    conn.close()
    return old_people_list

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    print("Old people:")
    for name, last_name, age in name_and_age_list:
        print(f"{name} {last_name}, age {age}")

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list to a CSV file

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
        writer.writerows([(name + ' ' + last_name, age) for name, last_name, age in name_and_age_list])

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()
