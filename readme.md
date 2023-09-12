# --> first install virtualenv after that activate virtualenv

# --> after activating the virtualenv we have to download "fastapi" using
#             python3 -m pip install fastapi

# --> install uvicone also 
#             pip install uvicone 
#              --> in django we have inbuilt server automatically it will work
#                but in fastapi we have to use the uvicone
# --> install mysql-connector also to store data in databse permanently 
#          --> python3 -m pip install mysql-connector

# --> In fastapi we will use http methods like [GET,POST,PUT,DELETE] 
#     GET--> it is used to retrive the data(like app.get("hear creat url"))
#             >url end points we will create inside
#     post--> it is used to create the data
#     put--> it is used to update the data
#     delete--> delete the data 
#     all above act like CURD operations


# --> to run server
#         --> uvicone address_book:app --reload
#                        modulename
#         after enter the server
#         enter the swagger-->http://localhost:8001/docs
#         app will create the obeject of fastapi


