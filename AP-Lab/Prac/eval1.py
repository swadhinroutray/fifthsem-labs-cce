import sqlite3

conn = sqlite3.connect("eval.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS persons(
    name varchar(30) primary key,
    password varchar(30),
    phone int(10),
    region varchar(30)
)''')
c.execute("Insert into  persons values('swadhin','123',9561097210,'pune');")
c.execute("Insert into  persons values('swadh','123',9561097210,'pune');")
c.execute("Insert into  persons values('swadhi','123',9561097210,'pune');")
c.execute("Insert into  persons values('swa','123',9561097210,'mumbai');")
c.execute("Insert into  persons values('swadin','123',9561097210,'mumbai');")

def checkLogin(name,pwd):
    namecheck = c.execute("Select * from persons where name = ?",[name])
    l =namecheck.fetchall()
    if len(l) ==0:
        print("User doesn't exist")
        return
    passcheck = c.execute("Select password from persons where name = ?",[name])
    for i in passcheck:
        if i==pwd:
            print("Hello", name)
            return
    print("Password incorrect")

def getRegion():
    data = c.execute("Select region,count(region) from persons group by region;")
    for  i in data:
        print(i)
def main():
    name = input("Input name: ")
    password = input("Input Password: ")
    x = (password,)
    checkLogin(name,x)
    # region = input("Input region: ")
    getRegion()


if __name__ == "__main__":
    main()