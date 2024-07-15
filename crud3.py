import sqlite3


def createTable():
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name  TEXT,
        cost FLOAT,
        price  FLOAT
        );
        """
    )
    conn.commit()
    conn.close()

def insertItem():
    conn=sqlite3.connect('books.db')
    cursor =conn.cursor()
    cursor.execute(

        """
        INSERT  INTO books (name,cost,price)
        VALUES(?,?,?)
        """,('A biblioteca da meia noite',60,80)
    )
    conn.commit()
    conn.close()


def readItems():
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()
    rows= cursor.execute(
    """
        SELECT * FROM books

    """
    )
    for row in rows:
        print(row)

    conn.commit()
    conn.close()

def updateItem():
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()
    cursor.execute(
        """   
            UPDATE books
            SET name = 'IKGAI'
            WHERE id = 5;          
        
        """
    )
    conn.commit()
    conn.close()

def deleteItem():
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()

    cursor.execute(
        """           
                DELETE FROM books WHERE id= 2;
    """
    )
    conn.commit()
    conn.close()


createTable()
insertItem()
#updateItem()
#deleteItem()
readItems()



