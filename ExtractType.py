import sqlite3 as Sq3

class ExtractModel:
    def __init__(self):
        Con = Sq3.connect("namecheapBlog.db")
        cur = Con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS ExtractModel(_id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,author_name TEXT)")
        Con.commit()
        Con.close()
    def AddToTable(self,title,author_name):
        Con = Sq3.connect("namecheapBlog.db")
        cur = Con.cursor()
        cur.execute("INSERT INTO ExtractModel (title, author_name) VALUES (?, ?)", (title, author_name))
        Con.commit()
        Con.close()