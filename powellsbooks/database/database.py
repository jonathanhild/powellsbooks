# -*- coding: utf-8 -*-

"""
powellsbooks.Database
~~~~~~~~
This module provides a data management object to SQLite3 database for Powell's 
Books recommender system.
"""

import os
import sqlite3
import datetime as dt

DEFAULT_DB_PATH = os.path.join('.', 'db', 'powells.db')
SQL_SCRIPTS = os.path.join('.', 'powellsbooks', 'database', 'sql')


class Database:
    """A Database management session.

    Provides database connection, creation, SELECT, UPDATE, and INSERT query
    support.

    Attributes:
        db_path (str): Path to database file.

    Basic Usage:
        >>> from powellsbooks.database import Database
        >>> db = Database('path/to/file')
        >>> db.select()
    """

    def __init__(self, db_path=DEFAULT_DB_PATH):
        self.db_path = db_path

        # Open a connection and cursor to the SQLite database.
        self.__conn = sqlite3.connect(self.db_path)
        self.__cursor = self.__conn.cursor()

    def create_tables(self):
        """
        Create tables in the Powell's database.

        Args:
            db_file (str): Path to SQLite database
        """

        # f requires CREATE IF NOT EXISTS
        f = open(os.path.join(SQL_SCRIPTS, 'create_db.sql'))
        create_sql = f.read()
        self.__cursor.executescript(create_sql)
        f.close()

    def schema_doc(self, docs, title):
        """
        Generate documentation of a SQLite database in Markdown format. Adapted
        from: https://gist.github.com/kumom/f238e401f419c1032d94f3b05b791df7

        Args:
            docs (str): File path to output Markdown file
            title (str): Heading for Markdown documentation

        Usage:
            >>> db = Database('path/to/file)
            >>> db.schema_docs('/path/to/db_name.md', 'Powell's Books')
        """
        # Open schema document Markdown file.
        f = open(docs, "w+")
        f.write(f'# {title} Database Schema\n\n')

        timestamp = dt.datetime.now()
        f.write(f'Document created on: {timestamp}\n\n')
        self.__cursor.execute('PRAGMA database_list')
        rows = self.__cursor.fetchall()
        for row in rows:
            f.write(f'Database path: {row[2]}\n\n')

        # Define the template.
        header_template = \
            '| ID | Name | Type | Not Null | Default Value | Primary Key |\n'
        spacer_template = '| --- | --- | --- | --- | --- | --- |\n'

        # Get list of tables from database.
        self.__cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.__cursor.fetchall()

        for table in tables:
            table_name = table[0].upper()
            f.write(f'## {table_name}\n\n')
            f.write(header_template)
            f.write(spacer_template)

            # Get table_info for each table.
            self.__cursor.execute(f'PRAGMA table_info({table_name});')
            columns = self.__cursor.fetchall()

            for column in columns:
                cid = str(column[0])
                name = str(column[1])
                dtype = str(column[2])
                if column[3] == 1:
                    notnull = 'Yes'
                else:
                    notnull = 'No'
                defval = str(column[4])
                if column[5] == 1:
                    pkey = 'Yes'
                else:
                    pkey = 'No'
                f.write(
                    f'| {cid} | {name} | {dtype} | {notnull} | {defval} | {pkey} |\n')
        f.close()

    def close(self):
        self.__conn.close()

    def __del__(self):
        pass


if __name__ == '__main__':
    db = Database('./db/powells.db')
    db.create_tables()
    db.schema_doc('./db/powells.md', 'Powells Books')
    db.close()
