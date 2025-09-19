import sqlite3 as Sq3

def inittilazer():
    Con = Sq3.connect("namecheapBlog.db")
    cur = Con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ExtractModel(_id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,author TEXT,_url TEXT)")
    Con.commit()
    Con.close()
    
def AddToTable(title,author,_url):
    inittilazer()
    Con = Sq3.connect("namecheapBlog.db")
    cur = Con.cursor()
    cur.execute("INSERT INTO ExtractModel (title, author,_url) VALUES (?, ?,?)", (title, author,_url))
    Con.commit()
    Con.close()

