import requests , json

BASE = "http://127.0.0.1:5000/"

data = [{"title" : "Tim","author" :"jhon","genre" : "fantasy"},
		{"title" : "Alex","author" : "jhon","genre" : "fantasy"},
		{"title" : "Kong","author" : "jhon","genre" : "fantasy"}]

#for i in range(len(data)):
	#response = requests.post(BASE + "book/" + str(i), data[i])
	#print(response.json())

#input()
#response = requests.patch(BASE + "book/1", {"author" : "Italy"})
#print(response.headers, response.status_code)
#print(response.json())
#input()
#response = requests.get(BASE + "book/2")
#print(response.json())
response = requests.get(BASE + "book/2")
print(response)