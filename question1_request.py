import requests
import json
url = ('http://saral.navgurukul.org/api/courses')
var=requests.get(url)
string=var.text
# print(type(string))
data = var.json()

my_files=open("courses.json",'r') 
files=json.loads(string)
# print(files)

cource=files["availableCourses"]
for i in range(len(cource)):
	print(i+1,cource[i]['name'],"id =",cource[i]['id'])
course_select=int(input("enter a cource number:"))
# print(cource[course_select-1]['name'])

# course_select=int(input("enter a cource number:"))	

sec_api = requests.get("http://saral.navgurukul.org/api/courses/"+str(cource[course_select-1]['id'])+"/exercises")
data = sec_api.json()
# print(type(sec_api))
api=open("sec_api.json",'w')
dat=json.dump(data,api,indent=2)
parents=data['data']
for j in range(len(parents)):
	print(j+1,"-",parents[j]['name'])
	counter = 1
	for index in parents[j-1]["childExercises"]:
		print("      ",counter,".",index["name"])
		counter+=1
Up_Navigation=input("enter 'up' for going back to all courses:")
cource2=files["availableCourses"]
if Up_Navigation=="up":
	for i in range(len(cource)):
		print(i+1,cource2[i]['name'],"id =",cource[i]['id'])
	course_select=int(input("enter a cource number:"))
	sec_api = requests.get("http://saral.navgurukul.org/api/courses/"+str(cource[course_select-1]['id'])+"/exercises")
	data = sec_api.json()
	# print(type(sec_api))
	api=open("sec_api.json",'w')
	dat=json.dump(data,api,indent=2)
	parents=data['data']
	for j in range(len(parents)):
		print(j+1,"-",parents[j]['name'])
		counter = 1
		for index in parents[j-1]["childExercises"]:
			print("      ",counter,".",index["name"])
			counter+=1

select_parent=int(input("select a parent"))
print(parents[select_parent-1]["name"])
count=1
for index in parents[select_parent-2]["childExercises"]:
	print("   ",count,index["name"])
	count+=1
select_child=int(input("select a child"))
slug = parents[select_parent-2]["childExercises"][select_child-1]['slug']
# print(cource[course_select-1]['id'])

link="http://saral.navgurukul.org/api/courses/"+str(cource[select_child-1]['id'])+"/exercise/getBySlug?slug="+str(slug)
slug1=requests.get(link)
slug2=slug1.json()
print(slug2["content"])


Previous_Navigation=input("enter'p'if you want previous line:")	
# index=0
# while index<len(select_child):
if Previous_Navigation =='p':
    print(parents[select_parent-2]["childExercises"][select_child-2]['slug'])
    # index=index+1
    link2="http://saral.navgurukul.org/api/courses/"+str(cource[select_child]['id'])+"/exercise/getBySlug?slug="+str(slug)
    slug_open=requests.get(link2)
    slug2_hit=slug_open.json()
    print(slug2_hit["content"])




		
# ++++++++++++++++-----------------------------------+++++++++++++++++++++++++++++++++++++++--------------------+++++++

 import requests
 import json
 url = ('http://saral.navgurukul.org/api/courses')
 var=requests.get(url)
 string=var.text
 # print(type(string))
 data = var.json()

 my_files=open("courses.json",'r') 
 files=json.loads(string)
 print(files)

 cource=files["availableCourses"]
 for i in range(len(cource)):
 	print(i+1,cource[i]['name'],"id =",cource[i]['id'])
 course_select=int(input("enter a cource number:"))
 print(cource[course_select-1]['name'])

course_select=int(input("enter a cource number:"))	

 sec_api = requests.get("http://saral.navgurukul.org/api/courses/"+str(cource[course_select-1]['id'])+"/exercises")
 data = sec_api.json()
 print(type(sec_api))
 api=open("sec_api.json",'w')
 dat=json.dump(data,api,indent=2)
 parents=data['data']
 for j in range(len(parents)):
 	print(j+1,"-",parents[j]['name'])
 	counter = 1
 	for index in parents[j-1]["childExercises"]:
 		print("      ",counter,".",index["name"])
		counter+=1
Up_Navigation=input("enter 'up' for going back to all courses:")
cource2=files["availableCourses"]
if Up_Navigation=="up":
	for i in range(len(cource)):
 		print(i+1,cource2[i]['name'],"id =",cource[i]['id'])
	course_select=int(input("enter a cource number:"))
	sec_api = requests.get("http://saral.navgurukul.org/api/courses/"+str(cource[course_select-1]['id'])+"/exercises")
 	data = sec_api.json()
 	# print(type(sec_api))
 	api=open("sec_api.json",'w')
 	dat=json.dump(data,api,indent=2)
 	parents=data['data']
	for j in range(len(parents)):
 		print(j+1,"-",parents[j]['name'])
		counter = 1
 		for index in parents[j-1]["childExercises"]:
 			print("      ",counter,".",index["name"])
			counter+=1

 select_parent=int(input("select a parent"))
 print(parents[select_parent-1]["name"])
count=1
for index in parents[select_parent-2]["childExercises"]:
 	print("   ",count,index["name"])
 	count+=1
 select_child=int(input("select a child"))
 slug = parents[select_parent-2]["childExercises"][select_child-1]['slug']
 print(cource[course_select-1]['id'])

 link="http://saral.navgurukul.org/api/courses/"+str(cource[select_child-1]['id'])+"/exercise/getBySlug?slug="+str(slug)
 slug1=requests.get(link)
 slug2=slug1.json()
 print(slug2["content"])

 Previous_Navigation=input("enter'p'if you want previous line:")	
 index=0
 while index<len(select_child):
 print(cource[select_child-1]["id"])

 if Previous_Navigation =='p':
     slug=(parents[select_parent-2]["childExercises"][select_child-2]['slug'])
    # # index=index+1
	# # print(cource[select_child-1]["ct_child-2]["id"])
     link2="http://saral.navgurukul.org/api/courses/"+str(int(cource[select_child-1]['id']))+"/exercise/getBySlug?slug="+str(slug)
 	# print(cource[select_child-2]["id"])
     slug_open=requests.get(link2)
     slug2_hit=slug_open.json()
     print(slug2_hit["content"])
 print(link2)

 
*********************************************-----------------------------------****************************************************************
#with function#

import requests
import json
url = ('http://saral.navgurukul.org/api/courses')
def cource(first_api):
    var=requests.get(first_api)
    string=var.text
    print(string)

    my_files=open("courses.json",'r') 
    store_data=json.loads(string)
# print(files)

    cource=store_data["availableCourses"]
    for i in range(len(cource)):
	    print(i+1,cource[i]['name'],"id =",cource[i]['id'])
    course_select=int(input("enter a cource number:"))
    
    
  
# # ***to print all the courses which are in saral using loop***

    sec_api = requests.get("http://saral.navgurukul.org/api/courses/"+str(cource[course_select-1]['id'])+"/exercises")   
    data = sec_api.json()
    # print(type(sec_api))
    api=open("sec_api.json",'w')
    dat=json.dump(data,api,indent=2)
    parents=data['data']
    for j in range(len(parents)):
        print(j+1,"-",parents[j]['name'])
        counter = 1
        for index in parents[j-1]["childExercises"]:
            print("      ",counter,".",index["name"])
            counter+=1
    
    Up_Navigation=input("enter 'up' for going back to all courses:")
    if Up_Navigation=="up":
        cource=store_data["availableCourses"]
        for i in range(len(cource)):
	        print(i+1,cource[i]['name'],"id =",cource[i]['id'])
        course_select=int(input("enter a cource number:"))
        for j in range(len(parents)):
            print(j+1,"-",parents[j]['name']
        select_parent=int(input("select a parent"))
        print(parents[select_parent-1]["name"])
        count=1
        for index in parents[select_parent-2]["childExercises"]:
	        print("   ",count,index["name"])
	        count+=1
        select_child=int(input("select a child"))
        slug = parents[select_parent-2]["childExercises"][select_child-1]['slug']
        link="http://saral.navgurukul.org/api/courses/"+str(cource[select_child-1]['id'])+"/exercise/getBySlug?slug="+str(slug)
        slug1=requests.get(link)
        slug2=slug1.json()  
        print(slug2["content"])
        Previous_Navigation=input("enter'p'if you want previous line:")	
# index=0
# while index<len(select_child):
        if Previous_Navigation =='p':
            slug=(parents[select_parent-2]["childExercises"][select_child-2]['slug'])
    # index=index+1
            link2="http://saral.navgurukul.org/api/courses/"+str(int(cource[select_child-1]['id']))+"/exercise/getBySlug?slug="+str(slug)
            slug_open=requests.get(link2)
            slug2_hit=slug_open.json()
            print(slug2_hit["content"])  
cource(url) 


		

