from ..db_conf import DataBase

db = DataBase()

if __name__ == '__main__':
    db.create_tables()
