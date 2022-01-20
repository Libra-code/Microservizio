#test dellle funzioni CRUD del microservizio
#urllib3 ==> 1.26.7 
import requests
import json

def read_all_test():
    try:
        r = requests.get('http://localhost:8000/book')        
    except requests.exceptions.ConnectionError:
        print("connection failed!")
        return False
    if r.status_code == 200:
        print("Read all successful, status code: ", r.status_code)
        return True
    else:
        print("Something is wrong")
    

def create_test():
    jtest = open('microservice/books/sample_test.json')
    try:
        r = requests.post('http://localhost:8000/book/1', json =json.load(jtest))     
    except requests.exceptions.ConnectionError:
        print("connection failed!")
        return False
    if r.status_code == 200:
        print("Create successful, status code: " , r.status_code)
        return True
    else:
        print("Something is wrong, status code: ", r.status_code)

def update_test():
    jtest = open('microservice/books/sample_update_test.json')
    try:
        r = requests.put('http://localhost:8000/book/1', json =json.load(jtest))   
    except requests.exceptions.ConnectionError:
        print("connection failed!")
        return False
    if r.status_code == 200:
        print("Update successful, status code: " , r.status_code)
        return True
    else:
        print("Something is wrong, status code: ", r.status_code)



def read_one_test():
    try:
        r = requests.get('http://localhost:8000/book/1')        
    except requests.exceptions.ConnectionError:
        print("connection failed!")
        return False
    if r.status_code == 200:
        print("Read one successful, status code: ", r.status_code)
        return True
    else:
        print("Something is wrong")

def delete_test():
    try:
        r = requests.delete('http://localhost:8000/book/1')        
    except requests.exceptions.ConnectionError:
        print("connection failed!")
        return False
    if r.status_code == 200:
        print("Delete successful, status code: ", r.status_code)
        return True
    else:
        print("Something is wrong")
    


def my_test():
    if read_all_test() and create_test() and update_test() and read_one_test() and delete_test():
        print("\U0001f600")
        return True
    else: 
        print("\U0001f622")
        return False

print("Test result: ", my_test())