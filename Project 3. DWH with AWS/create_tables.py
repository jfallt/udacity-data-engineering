# Import Required Libriaries
import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

# Define Functions to Drop Tables (if they exist) and Create Tables for ETL
def drop_tables(cur, conn):
    """
    Drops all tables of interest
    
    params
    cur: cursor
    conn: connection
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates tables of interest
    
    params
    cur: cursor
    conn: connection
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
     """
    Drop and Create Tables
    
    params
    cur: cursor
    conn: connection
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()