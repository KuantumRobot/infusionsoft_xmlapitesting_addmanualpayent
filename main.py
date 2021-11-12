import json, requests, datetime,os
from infusionsoft.library import InfusionsoftOAuth


access_token = requests.get("https://****").text #token is from outer source
private_code = os.getenv("private_code")

def orderCreation(request):
    request_json = request.get_json()
    
    if request_json["private_code"] != private_code:
        return 'You need Private Code to run this function', 403
    
    else:
        infusionsoft = InfusionsoftOAuth(access_token)
        invID = request_json["InvoiceId"]
        amount = request_json["amount"]
        date = request_json["date"]
        payType = "From Shopify"
        description = request_json["notes"]
        bypassComm = False

        req2 = infusionsoft.InvoiceService("addManualPayment",invID,amount,date,payType,description,bypassComm)
        return req2, 200



#This is to do the testing locally
  
#testJ = {"InvoiceId" : 6589, "amount" : 125.00,"date": datetime.datetime.now(), "notes":"I am a repeater."}
#print(orderCreation(testJ))



