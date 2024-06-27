import sqlite3

class Database():

    def __init__(self, dbname) -> None:
        self.__dbname = dbname

    def dbGetData(self, sql) -> list:
        returnData = None
        try:
            with sqlite3.connect(self.__dbname) as conn:
                # Indicate we want column names returned
                conn.row_factory = sqlite3.Row
                # Execute query and fetch all rows back and store data in the returnData variable
                returnData = conn.cursor().execute(sql).fetchall()
        except sqlite3.Error as e:
            print(f"Game Database problem. Error: {e}")
            returnData = None
        return returnData

    def dbPutData(self, sql) -> int | None:
        '''Insert SQL command - returns new Id'''
        newId = None
        try:
            with sqlite3.connect(self.__dbname) as conn:
                # Indicate we want column names returned
                cursor = conn.cursor()
                cursor.execute(sql)
                newId = cursor.lastrowid
                cursor.close()
        except sqlite3.Error as e:
            print(f"Game Database problem. Error: {e}")
        finally:
            if conn:
                conn.commit()
        return newId

    def dbChangeData(self, sql) -> None:
        '''Change data with SQL command - e.g. Update or Delete commands'''
        try:
            with sqlite3.connect(self.__dbname) as conn:
                # Indicate we want column names returned
                cursor = conn.cursor()
                cursor.execute(sql)
                cursor.close()
        except sqlite3.Error as e:
            print(f"Game Database problem. Error: {e}")
        finally:
            if conn:
                conn.commit()


# Test harness - calls all the methods above to see if they work
def main():
    pass

if __name__=="__main__":
    main()