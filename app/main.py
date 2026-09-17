from fastapi import FastAPI
from sqlalchemy import text
from app.database.connection import engine

app = FastAPI(
    title='Home App Core',
    version='0.1.0',
)

@app.get('/')
def root():
    return{
        'name': 'Home App Core',
        'version': '0.1.0',
    }

@app.get('/health')
def health():
    try:
        with engine.connect() as connection:
            connection.execute(text('SELECT 1'))
            return {'status': 'ok', 'database': 'connected'}
    except Exception as e:
        return {'status': 'error', 'database': str(e)}