import requests , json

BASE = "http://localhost:8000/"

try:
    data = [{"title" : "Tim","author" :"jhon","genre" : "fantasy"},
            {"title" : "Alex","author" : "jhon","genre" : "fantasy"},
            {"title" : "Kong","author" : "jhon","genre" : "fantasy"}]

    for i in range(len(data)):
        response = requests.post(BASE + "book/" + str(i+1), data[i])
        if (response.status_code != 201) :
            print("errore nel post")
        

    response = requests.patch(BASE + "book/1", {"author" : "Italy"})
    if (response.status_code != 200) :
            print("errore nel patch")
            
    response = requests.get(BASE + "book/2")
    if (response.status_code != 200) :
            print("errore nel get")
            
    response = requests.get(BASE + "book")
    if (response.status_code != 200) :
        print("errore nel get")
    
    
    response = requests.delete(BASE + "book/1")
    if (response.status_code != 204) :
        print("errore nel delete")
    response = requests.delete(BASE + "book/2")
    if (response.status_code != 204) :
        print("errore nel delete")
    response = requests.delete(BASE + "book/3")
    if (response.status_code != 204) :
        print("errore nel delete")
    
except Exception as ex:
    print (ex)
    
print("Test completato")