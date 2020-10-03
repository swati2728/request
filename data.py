# import json
# obj = '{"name":"Swati","age":19,"learning":"pythonS"}'
# files=open("courses.json",'w')
# my_files=json.dumps(obj,indent=4)
# print(my_files)


import json 
  
# # initialising dictionary 
# test1 = { "testname" : "akshat", 
#           "test2name" : "manjeet", 
#           "test3name" : "nikhil"} 
  
# # print original dictionary 
# print (type(test1)) 
# print ("initial dictionary = ", test1) 
  
# # convert dictionary into string 
# # using json.dumps() 
# result = json.dumps(test1) 
  
# # printing result as string 
# print ("\n", type(result)) 
# print ("final string = ", result)


import json

dict1 = {"name":"Swati","age":19,"learning":"pythonS"}


out_file = open("courses.json", "w")
  
json.dump(dict1, out_file, indent = 6)
  
# out_file.close()

# new='{"age":"12"}'
# print(new[8]+new[9])



