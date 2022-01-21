import requests , json

BASE = "http://localhost:8002/"

try:
    data = [{"user_id":1,"name" :"jhon","surname" : "Depp"},
            {"user_id":2,"name" : "jhon","surname" : "Depp"},
            {"user_id":3,"name" : "jhon","surname" : "Depp"}]

    for i in range(len(data)):
        response = requests.post(BASE + "costumer/", data[i])
        if (response.status_code == 200) :
            print("errore nel post")
        

    response = requests.put(BASE + "costumer/1", {"user_id":1,"name" : "jhon","surname" : "Depp"})
    if (response.status_code != 200) :
            print("errore nel patch")
            
    response = requests.get(BASE + "costumer/2")
    if (response.status_code != 200) :
            print("errore nel get")
            
    response = requests.get(BASE + "costumer")
    if (response.status_code != 200) :
        
        print("errore nel get")
    
    response = requests.delete(BASE + "costumer/1")
    if (response.status_code != 200) :
        print("errore nel delete")
    response = requests.delete(BASE + "costumer/2")
    if (response.status_code != 200) :
        print("errore nel delete")
    response = requests.delete(BASE + "costumer/3")
    if (response.status_code != 200) :
        print("errore nel delete")
    
except Exception as ex:
    print (ex)
    
print("Test completato")