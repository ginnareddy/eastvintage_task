from fastapi import FastAPI
import uvicorn
import mysql.connector
# creating appp and object to the FastApi
app=FastAPI()

'''
#download mysql enter this command i will create the table Address_Book
create database abhi;
use abhi; 
create table Address_Books(id int unique auto_increment primary key ,name varchar(25),ph_no varchar(20),street varchar(50),city varchar(15),state varchar(20),zip_code int);

'''


# i am giving mysql database connection to do this connection  
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Abhinav@369",
  database="sushi"
)

# @app.get('/ind/{name}')
# def index(name:str):
#     return name

@app.get("/alladresses")
def all_addresses():
    cursor=mydb.cursor()
    cursor.execute("select * from Address_Books;")
    result=cursor.fetchall()
    return {"address":result}


@app.get("/person/address/{id}")
def person_address(id:int):
    cursor = mydb.cursor()
    cursor.execute(f"select * from Address_Books WHERE id = {id};")
    result = cursor.fetchone()
    # fetchone is used to featch only perticuler value
    return {"addresses":result}


@app.post("/Address_bar")
def add_Address(name: str, ph_no: str,street:str,city:str,state:str,zip_code:int):
    cursor = mydb.cursor()
    querie = "INSERT INTO Address_Books(name,ph_no,street,city,state,zip_code) VALUES (%s, %s,%s,%s,%s,%s);"
    val = (name,ph_no,street,city,state,zip_code)
    cursor.execute(querie, val)
    # execute will take two parameters one is query and another is veriables
    mydb.commit()
    return {"message": "Person Address added successfully"}

@app.put("/update_address/{id}")
def update_Address(name: str, ph_no: str,street:str,city:str,state:str,zip_code:int,id=int):
    cursor=mydb.cursor()
    querie="UPDATE Address_Books SET name = %s, ph_no = %s,street = %s, city=%s,state=%s,zip_code=%s WHERE id=%s;"
    val = (name,ph_no,street,city,state,zip_code,id)
    cursor.execute(querie, val)
    mydb.commit()
    return {"message": "Person Address updated successfully"}


@app.delete("/Adress_bar/{id}")
def delete_Address(id: int):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM Address_Books WHERE id = {id}")
    mydb.commit()
    # commit is used to store data in database if u wont commit it wont store 
    return {"message": "person address deleted successfully"}


if __name__=='__main__':
    uvicorn.run(app,host='localhost',port=8001)


