from flask import Flask
from flask_cors import CORS
import json

app = Flask("List of Universities")
CORS(app)

with open("UK_Universities.json", "r") as unifile:
    data = json.load(unifile)


@app.route("/colleges")
def getCollegesList():
    colleges = []
    for college in data:
        colleges.append(college["name"])
    return json.dumps({"Colleges": colleges},indent=4)


@app.route("/colleges/<name>")
def getCollegesListByName(name):
    colleges = []
    for college in data:
        if college["name"].__contains__(name):
            colleges.append(college["name"])
    return json.dumps({"Colleges": colleges},indent=4)

# Update the listings microservices to retrieve the list of universities in a 
# case-insensitive manner. Verify the same passing “TriniTY”, as a parameter. If 
# successfully updated, the endpoint should return all the universities with the word 
# ‘Trinity’.

@app.route("/colleges/<name>")
def getCollegesListByName(name):
     name = name.lower()  # Convert the search parameter to lowercase
     colleges = []
     for college in data:
        if name in college["name"].lower(): # Convert university name to lowercase for case-insensitive comparison
            colleges.append(college["name"])
    return json.dumps({"Colleges": colleges},indent=4)

if __name__ == "__main__":
    app.run(debug=True)
