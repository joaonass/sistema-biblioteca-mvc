import mysql.connector
from config.config import HOST, USER, PASSWORD, DATABASE

def conectar():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
