from tinydb import TinyDB, Query

class Pydb:

    def __init__(self, db_path='Tinydb/db.json'):
        self._db = TinyDB(db_path, sort_keys=True, indent=4, separators=(',', ': '))
        self._user = Query()
        self._default_data = {"1": "##", "2" : "##"}

    def _get_table_list(self):
        return self._db.tables()

    def _create_table(self, table_name):
        table = self._db.table(table_name)
        if table_name not in self._get_table_list():
            table.insert(self._default_data)
            print(f'Successfully create {table_name}\n')
        else:
            raise NameError(f"Table '{table_name}' already exist.")

    def _insert_data(self, table_name, data):
        self._check_table(table_name)
        table = self._db.table(table_name)
        table.insert(data)

    def _extract_row(self, table_name):
        self._check_table(table_name)      
        return self._db.table(table_name).all()
    
    def _delete_table(self, table_name):
        self._check_table(table_name) 
        self._db.drop_table(table_name)
        print(f'Successfully deleted {table_name}\n')

    def _query_data_table(self, table_name, name, attribute):
        self._check_table(table_name)
        table = self._db.table(table_name)
        return table.search(self._user.name == attribute)

    def _check_table(self, table_name):
        if table_name not in self._get_table_list():
            raise NameError(f"Table '{table_name}' does not exist.")
        else:
            return
        
# Example Usage
if __name__ == "__main__":
    Database = Pydb()
    Data = {"BTC": "BITCOIN"}
    #Database._create_table("Test2")
    #Database._insert_data("Test1", Data)
    #print(Database._extract_row("Test1"))
    #Database._delete_table("Test1")
    print(Database._query_data_table('Test1', 'name', 'BTC'))