import requests

import json

def getReq(url):
    try:
        res = request.get(url)
        return json.dumps(res.json(),indent = 4)
    except Exception as e:
        return f"Error:{e}"

def postReq(url,data):
    try:
        res = request.post(url,json=data)
        return json.dumps(res.json(), indent = 4)
    except Exception as err:
        return f"Error:{err}"

while True:
    try:
        choice = int(input("1.Get Request\n2.Post Request\n3.Exit\nEnter Choice: "))
        if choice == 1:
            url_inp = input("Enter a valid get url: ")
            print(getReq(url_inp))
        elif choice == 2:
            url_inp = input("Enter a valid get url: ")
            data_inp = {
                "name": input("Name:"),
                "email":input("Email:"),
                "work":input("Work:"),
                "age":input("Age:")
            }
            print(postReq(url_inp,data_inp))
        elif choice == 3:
            exit(0)
    except Exception as ex:
        print("Error:",e)
        
