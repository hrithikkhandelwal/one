from flask import *
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb+srv://demo1:demo111@cluster0.lcb6k.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.one

app = Flask(__name__)

@app.route('/')
def grid():
    return render_template("main.html");

@app.route("/savedetails",methods = ["POST","GET"]) 
def savedetails(): 
    details = db.details
    name = ""
    titletext = ""
    contenttext = ""  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            titletext = request.form["titletext"]  
            contenttext = request.form["contenttext"]  
            print(titletext,contenttext,name)
            personDocument={
            "name": name,
            "titletext": titletext,
            "contenttext": contenttext,
           }

            details.insert_one(personDocument)
            print("Details Saved")
        except:  
            msg = "We can not add the Student to the list"  
        finally:  
            return render_template("s.html",name = name,titletext = titletext,contenttext = contenttext)
      

if __name__ == "__main__":  
    app.run(debug = True)

