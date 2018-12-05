import flask
from flask import Flask
from flask_pymongo import PyMongo
from datetime import date
#from flask.ext.bcrypt import Bcrypt
#import Bcrypt

app = Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost:27017/BankDatabase"
mongo = PyMongo(app)
#bcrypt = Bcrypt(app)

"""
@app.route("/login/<accountid>/<password>")
def login(accountid,password):
    try:
        account_info1 = mongo.db.users.find({"AccountID": accountid})
        password_hash = account_info1['password']
        if bcrypt.check_password_hash(password_hash, password):
            return "Valid Credentials"
        else:
            return "Invalid Credentials"
    except:
        return "Unable to Fetch Details"
"""

@app.route("/getbalance/<accountid>")
def getBalance(accountid):
    try:
        accountid = int(accountid)
        account_info = mongo.db.users.find({"AccountID": accountid})
        if account_info.count() > 0:
            for record in account_info:
                amount = record['Balance']
                return "Available Balance of Account Number "+str(accountid)+" is Rs "+str(amount)
        else:
            return "Customer Information doesnot exist"
    except Exception as e:
        return "Unable to Fetch Details",e
    
@app.route("/addBeneficiary/<accountid>/<customername>/<balance>")
def addBeneficiary(accountid,customername,balance):
    try:
        accountid = int(accountid)
        balance = int(balance)
        account_info = mongo.db.users.insert({"AccountID": accountid,"CustomerName":customername,"Balance":balance})
        return "Beneficiary Added: "+str(customername)
    except Exception as e:
        return "Unable to Add Beneficiary"
        
@app.route("/deleteBeneficiary/<accountid>")
def deleteBeneficiary(accountid):
    try:
        accountid = int(accountid)
        account_info = mongo.db.users.find({"AccountID": accountid})
        if account_info.count() > 0:
            account_info = mongo.db.users.remove({"AccountID": accountid})
            return "Account Deleted: "+str(accountid)
        else:
            return "Customer Information doesnot exist"
    except Exception as e:
        return "Unable to Delete the account"
     
@app.route("/transferFunds/<accountid1>/<accountid2>/<amount>")
def transferFunds(accountid1,accountid2,amount):
    try:
        accountid1 = int(accountid1)
        accountid2 = int(accountid2)
        amount = int(amount)
        account_info1 = mongo.db.users.find({"AccountID": accountid1})
        account_info2 = mongo.db.users.find({"AccountID": accountid2})
        if account_info1.count() > 0 and account_info2.count() > 0:
            for record in account_info1:
                balance1 = int(record['Balance'])
            for record in account_info2:
                balance2 = int(record['Balance'])
            if(balance1<amount):
                return "No Sufficient Funds in :"+str(accountid1)
            else:
                balance2 += amount
                balance1 -= amount
                mongo.db.users.update({'AccountID': accountid1}, {'$set': {"Balance": balance1}}, multi=True)
                mongo.db.users.update({'AccountID': accountid2}, {'$set': {"Balance": balance2}}, multi=True)
                return "Transferred Funds"
    except:
        return "Unable to fetch  Details"
        
@app.route("/futureAmount/<accountid>/<day>/<month>/<year>")
def futureAmount(accountid,day,month,year):
    try:
        currentdate = date.today()
        accountid = int(accountid)
        day = int(day)
        month = int(month)
        year = int(year)
        futuredate = date(year,month,day)
        delta = currentdate - futuredate
        noOfDays = delta.days
        account_info = mongo.db.users.find({"AccountID": accountid})
        if account_info.count() > 0:
            for record in account_info:
                balance = record['Balance']
            interest = (balance*noOfDays*4)/(100*365)
            total_amount = balance+interest
            return "Expected Balance of "+str(accountid)+" on "+str(futuredate)+" is Rs "+str(total_amount)
        else:
            "Customer Information doesnot exist"
    except Exception as e:
        return "Unable to fetch Details",e
    

    
    