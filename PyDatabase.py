# PyDatbase.py
# This is a simple database to store and query the data for our program
# Taewoo Kim
# data: Jan 17, 2025

from tinydb import TinyDB, Query

## \class Pydb
#  \brief A class for managing a TinyDB instance with convenience methods
#         to create tables, insert/query data, and more.
class Pydb:
    ## \brief Class constructor to initialize the TinyDB database.
    #  \param db_path The path to the TinyDB JSON file. Defaults to 'Tinydb/db.json'.
    def __init__(self, db_path='Tinydb/db.json'):
        self._db = TinyDB(db_path, sort_keys=True, indent=4, separators=(',', ': '))
        self._user = Query()
        self._default_data = {"1": "##", "2": "##"}

    ## \brief Retrieve a list of all table names in the TinyDB database.
    #  \return A list of table names available in the database.
    def _get_table_list(self):
        return self._db.tables()

    ## \brief Create a new table with a default record, if it does not already exist.
    #  \param table_name The name of the table to create.
    #  \exception NameError If the table already exists.
    def _create_table(self, table_name):
        table = self._db.table(table_name)
        if table_name not in self._get_table_list():
            table.insert(self._default_data)
            print(f'Successfully create {table_name}\n')
        else:
            raise NameError(f"Table '{table_name}' already exist.")

    ## \brief Insert a new record into the specified table.
    #  \param table_name The name of the table into which data should be inserted.
    #  \param data       A dictionary representing the record to insert.
    #  \exception NameError If the specified table does not exist.
    def _insert_data(self, table_name, data):
        self._check_table(table_name)
        table = self._db.table(table_name)
        table.insert(data)

    ## \brief Retrieve all rows (documents) from the specified table.
    #  \param table_name The name of the table from which to extract rows.
    #  \return A list of dictionaries, each representing a document in the table.
    #  \exception NameError If the specified table does not exist.
    def _extract_row(self, table_name):
        self._check_table(table_name)
        return self._db.table(table_name).all()

    ## \brief Delete an existing table from the database entirely.
    #  \param table_name The name of the table to delete.
    #  \exception NameError If the specified table does not exist.
    def _delete_table(self, table_name):
        self._check_table(table_name)
        self._db.drop_table(table_name)
        print(f'Successfully deleted {table_name}\n')

    ## \brief Query a table for all documents where field \p name matches \p attribute.
    #  \param table_name The name of the table to query.
    #  \param name       The field name to match.
    #  \param attribute  The value that the field \p name should match.
    #  \return A list of all matching documents.
    #  \exception NameError If the specified table does not exist.
    def _query_data_table(self, table_name, name, attribute):
        self._check_table(table_name)
        table = self._db.table(table_name)
        return table.search(self._user[name] == attribute)

    ## \brief Verify that a table exists in the database.
    #  \param table_name The name of the table to check.
    #  \exception NameError If the specified table does not exist.
    def _check_table(self, table_name):
        if table_name not in self._get_table_list():
            raise NameError(f"Table '{table_name}' does not exist.")
        return

## \brief Example usage of the Pydb class.
#  Demonstrates how to create a Pydb instance, optionally create a table, insert data,
#  and then query it.
if __name__ == "__main__":
    Database = Pydb()
    Data = {
        'id': 'bitcoin', 
        'name': 'Bitcoin', 
        'api_symbol': 'bitcoin', 
        'symbol': 'BTC', 
        'market_cap_rank': 1, 
        'thumb': 'https://coin-images.coingecko.com/coins/images/1/thumb/bitcoin.png', 
        'large': 'https://coin-images.coingecko.com/coins/images/1/large/bitcoin.png'
    }

    #Database._create_table("Test1")
    #Database._insert_data("Test1", Data)
    #print(Database._extract_row("Test1"))
    #Database._delete_table("Test1")
    print(Database._query_data_table('Test1', 'id', 'bitcoin'))
