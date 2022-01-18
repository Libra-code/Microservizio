import requests , json

BASE = "http://localhost:8000/"
#BASE = "http://127.0.0.1:5000/"

data = [{"name" : "Tim","views" : 100,"likes" : 10},
		{"name" : "Jon","views" : 1000,"likes" : 100},
		{"name" : "Jim","views" : 10000,"likes" : 1000}]

 #for i in range(len(data)):
	#response = requests.put(BASE + "video/" + str(i), data[i])
	#print(response.json())

#input()
response = requests.put(BASE + "video/10", {"name" : "Tim","views" : 100,"likes" : 10})
#print(response.headers, response.status_code)
#print(response.json())
#input()
#response = requests.get(BASE + "video/10")
print(response.json())