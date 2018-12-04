import flask
from flask import Flask
from flask_pymongo import PyMongo
from datetime import date
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost:27017/BankDatabase"
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

@app.route("/getInfo/<accountnum>")
def TransactionSummary():
    account_info = mongo.db.users.find({"AccountID": accountnum})
    amount = account_info['Balance']
    return str(amount)
    
@app.route("/addBeneficiary/<accountid>/<accountname>/<balance>")
def AddBeneficiary():
    try:
        account_info = mongo.db.users.insert({"AccountID": accountid,"AccountName":accountname,"Balance":balance})
        return "Beneficiary Added"
    except Exception as e:
        return "Unable to Add Beneficiary"
        
@app.route("/deleteBeneficiary/<accountid>")
def DeleteBeneficiary():
    try:
        account_info = mongo.db.users.remove({"AccountID": accountid})
        return "Account deleted"
    except Exception as e:
        return "Unable to Delete the account"
        
@app.route("/transferFunds/<accountid1>/<accountid2>/<amount>")
def TransferFunds():
    try:
        account_info1 = mongo.db.users.find({"AccountID": accountid1})
        account_info1 = mongo.db.users.find({"AccountID": accountid2})
        balance1 = account_info['Balance']
        balance2 = account_info['Balance']
        if(balance1<amount):
            return "No Sufficient Funds"
        else:
            balance2 += amount
            balance1 -= amount
            account_info1 = mongo.db.users.update({"AccountID": accountid1},{$set:{"Balance":balance1}})
            account_info1 = mongo.db.users.update({"AccountID": accountid2},{$set:{"Balance":balance2}})
            
    except:
        return "Unable to fetch Account Details"
        
@app.route("/futureAmount/<accountid>/<date>")
def FutureAmount():
    currentdate = datetime.date.today()
    delta = currentdate - date
    noOfDays = delta.days
    account_info = mongo.db.users.find({"AccountID": accountid})
    balance = account_info['Balance']
    intrest = (balance*noOfDays*4)/(100*365)
    total_amount = balance+intrest
    return str(total_amount)
    
@app.route("/login/<accountid>/<password>")
def Login():
    account_info1 = mongo.db.users.find({"AccountID": accountid1})
    password_hash = account_info1['password']
    if bcrypt.check_password_hash(password_hash, password):
        return "Valid Credentials"
    else:
        return "Invalid Credentials"

    



























    