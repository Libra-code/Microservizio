import requests , json

BASE = "http://localhost:8001/"

try:
    data = [{"book_id" : 1,"costumer_id" :3},
            {"book_id" : 2,"costumer_id" :3},
            {"book_id" : 2,"costumer_id" :4}]

    for i in range(len(data)):
        response = requests.post(BASE + "borrowing/" + str(i+1), data[i])
        if (response.status_code != 201) :
            print("errore nel post")
        

    response = requests.patch(BASE + "borrowing/1", {"author" : "Italy"})
    if (response.status_code != 200) :
            print("errore nel patch")
            
    response = requests.get(BASE + "borrowing/2")
    if (response.status_code != 200) :
            print("errore nel get")
            
    response = requests.get(BASE + "borrowing")
    if (response.status_code != 200) :
        print("errore nel get")
    
    
    response = requests.delete(BASE + "borrowing/1")
    if (response.status_code != 204) :
        print("errore nel delete")
    response = requests.delete(BASE + "borrowing/2")
    if (response.status_code != 204) :
        print("errore nel delete")
    response = requests.delete(BASE + "borrowing/3")
    if (response.status_code != 204) :
        print("errore nel delete")
    
except Exception as ex:
    print (ex)
    
print("Test completato")