import logging
import time
from typing import List

import psycopg2

USER = "Benny"
PASSWORD = "1234"
HOST = "db"
PORT = "5432"


class DataBaseForRandoms:
    def __init__(self):
        db_ready = False
        while not db_ready:
            try:
                self.conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT)
                db_ready = True
                logging.info("Connection to DataBase succeeded")
            except psycopg2.OperationalError:
                logging.info("Waiting for the database to be ready...")
                time.sleep(1)
        self.cursor = self.conn.cursor()
        self.conn.autocommit = True
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self) -> bool:
        try:
            self.cursor.execute("""
                   CREATE TABLE IF NOT EXISTS random_numbers (
                       id SERIAL PRIMARY KEY,
                       number INTEGER
                   );
               """)
            logging.info(f"Create table for random_numbers on DataBase")
            return True
        except psycopg2.Error as e:
            logging.error(f"Error creating table: {e}")
            return False

    def store_random_number(self, random_number: int) -> bool:
        try:
            self.cursor.execute("INSERT INTO random_numbers (number) VALUES (%s)", (random_number,))
            logging.info(f"Add random number to DataBase: {random_number}")
            return True
        except psycopg2.Error as e:
            logging.error(f"Error storing random number: {e}")
            return False

    def get_all_numbers(self) -> List:
        try:
            self.cursor.execute("SELECT * FROM random_numbers")
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            logging.error(f"Error fetching all numbers: {e}")
            return []
