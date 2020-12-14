from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@localhost:5432/marvel_api_dev')

def select_characters():
    with engine.connect() as conn:
        return conn.execute('SELECT * FROM characters')
        

