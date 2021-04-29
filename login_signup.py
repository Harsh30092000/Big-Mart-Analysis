def check_member(cur,user_name,password):
    data = cur.execute(f"SELECT * from users where username='{user_name}'").fetchall()
    try:
        if(data[0][2]==password):
            return True
        else:
            return False
    except:
        return False

def add_new_user(conn,cur,email,user_name,password):
    cur.execute(f"INSERT into users values('{email}','{user_name}','{password}')")
    #conn.commit()