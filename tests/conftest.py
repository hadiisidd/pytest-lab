import sqlite3, pytest
from bank import BankAccount

@pytest.fixture
def account():
    return BankAccount("Ayesha", balance=1000)

@pytest.fixture
def db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE accounts (owner TEXT, balance REAL)")
    yield conn
    conn.close()
