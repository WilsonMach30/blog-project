import sqlite3

DB_FILE = "data.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)

def start():
    c = db.cursor()
    c.execute("create TABLE if not exists USER(username, password)")
    c.execute("create TABLE if not exists BLOG(blog_id, title, author, content, last_modified)")    
    c.close()

def check_user_exist(username):
    c = db.cursor()
    c.execute("select USERNAME from USER where USERNAME = ?", (username,))
    username_status = c.fetchone()
    c.close()
    return username_status

def check_credentials(username, password):
    c = db.cursor()
    c.execute("select * from USER where USERNAME = ?", (username,))
    data = c.fetchone()
    c.close()

    if data == None or password != data[1]:
        return False
    return True

def create_new_user(username, password):
    c = db.cursor()
    c.execute("insert into USER values(?, ?)", (username, password))
    
    db.commit()
    c.close()
    return True

def get_blogs(username):
    c = db.cursor()
    c.execute("select * from BLOG where AUTHOR = ?", (username))
    data = c.fetchall()
    c.close()
    return data

def get_last_blog_id():
    c = db.cursor()    
    c.execute("select COUNT(blog_id) from BLOG")
    data = c.fetchone()
    c.close()
    return data[0]

def create_new_blog(last_value, title, author, content, last_modified):
    c = db.cursor()    
    c.execute("insert into BLOG values(?,?,?,?,?)", (last_value, title, author, content, last_modified))
    
    db.commit()
    c.close()
    return True

def restart():
    c = db.cursor()
    c.execute("drop table if exists USER")
    # c.execute("drop table if exists BLOG")

    db.commit()
    c.close()
    return True

start()
# restart()
