from fastapi import FastAPI

app = FastAPI()
##########################3
@app.get("/abc")
def root1():
    return {"status1": " Hii Sam"}
#######################
@app.get("/items/{item_id}")
def read_item(item_id : int, q: str | None = None):
    return {"item_id": item_id, "q": q}
###############################

@app.get("/name")
def add(f_name : str, last_name):
    #return {'f_name' : f_name , "l_name": last_name}
    return f_name +" " + last_name

f_name = "sam"
last_name = "xyz"

name =  add(f_name , last_name)
print(name)
#######################################


