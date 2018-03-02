# author Mahmud Ahsan
# ----------------------------------
# Working with Database : SQLite
# ----------------------------------

from database import mydatabase

# Program entry point
def main():
    dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='mydb.sqlite')

    # Create Tables
    dbms.create_db_tables()
    # dbms.insert_single_data()
    dbms.print_all_data(mydatabase.USERS)
    dbms.print_all_data(mydatabase.ADDRESSES)

    dbms.sample_query() # simple query
    dbms.sample_delete() # delete data
    dbms.sample_insert() # insert data
    dbms.sample_update() # update data


# run the program
if __name__ == "__main__": main()
