import requests
import json
url="https://api.github.com/users/swati2728/repos"
api=requests.get(url)
# print(api)**<Response [200]>
data=api.text
# string=data.json
# print(data)

my_files=open("second.json",'w')
files=my_files.write(data)
data_store=json.loads(data)

repository_data=data_store
for i in data_store:
    print("This are the name of the repository:-",i["name"]+"    "+"This are the name of the descipition:-",i["description"])
    # for j in i:
    #     print(i+1,repository_data[0]["name"])



