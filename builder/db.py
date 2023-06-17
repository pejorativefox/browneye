import os
import logging
import sqlite3 as sql


DEFAULT_DATABASE_PATH = "./.package.sqlite"

SQL_CREATE_TABLES = """
CREATE TABLE package (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            built BOOL DEFAULT FALSE
        );
"""

SQL_CHECK_PACKAGE_EXISTS = """
SELECT * from package WHERE name="{}" LIMIT 1;
"""

SQL_ADD_PACKAGE = """
INSERT INTO package (name)
    VALUES("{}");
"""

SQL_IS_BUILT = """
SELECT built FROM package WHERE name="{}" LIMIT 1;
"""

SQL_SET_BUILT = """
UPDATE package SET built = TRUE WHERE name="{}";
"""

SQL_SET_UNBUILT = """
UPDATE package SET built = FALSE WHERE name="{}";
"""

class PackageDatabase(object):
    def __init__(self, path=DEFAULT_DATABASE_PATH):
        self._path = path
        if os.path.isfile(path) == False:
            print("Creating database @", self._path)
            self._create_package_database(self._path)
        else:
            print("Aldeady have a database @", self._path)
        
        self._connection = sql.connect(self._path)

    def _create_package_database(self, path=DEFAULT_DATABASE_PATH):
        connection = sql.connect(path)
        with connection:
            connection.execute(SQL_CREATE_TABLES)
        connection.close()
    
    def _check_package_exists(self, package_name):
        cur = self._connection.cursor()
        cur.execute(SQL_CHECK_PACKAGE_EXISTS.format(package_name))
        rows = cur.fetchall()
        if len(rows) > 0:
            return True
        return False

    def add_package(self, name):
        if self._check_package_exists(name) is False:
            print("new package: ", name)
            self._connection.execute(SQL_ADD_PACKAGE.format(name))
            self._connection.commit()
            return True
        else:
            print("Already exists: ", name)
            return False

    def is_built(self, name):
        cur = self._connection.cursor()
        cur.execute(SQL_IS_BUILT.format(name))
        row = cur.fetchone()
        if row[0] == 1:
            return True
        return False

    def set_built(self, name):
        cur = self._connection.cursor()
        cur.execute(SQL_SET_BUILT.format(name))
        self._connection.commit()

    def set_unbuilt(self, name):
        cur = self._connection.cursor()
        cur.execute(SQL_SET_UNBUILT.format(name))
        self._connection.commit()

if __name__ == "__main__":
    import package
    db = PackageDatabase()
    for p in package.discover_packages():
        db.add_package(p.name)
