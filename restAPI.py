from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)

class Pass(Resource):
    def get(self):
        file = open("db.json","r")
        passwords = json.loads(file.read())
        file.close()
        return passwords, 200
    def post(self):
        file = open("db.json","r")
        passwords = json.loads(file.read())
        file.close()

        for key, value in request.args.items():
            passwords["{}".format(key)] = value
        with open("db.json", "w") as outfile:
            json.dump(passwords, outfile)
        outfile.close()    
        return passwords, 200
        
api.add_resource(Pass, "/pass")

if __name__ == "__main__":
    app.run()


