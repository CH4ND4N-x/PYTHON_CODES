#Student and Faculty JSON
import json
Faculty_json="""
    {
     "FACULTY1":{
                     "First Name":"Rakesh",
                     "Last Name":"Joshi",
                     "photo":"https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
                     "Department":"computer science",
                     "Research":["big data","cloud computing"],
                     "Contact":[8888888,"xyz@gmail.com"]
                 },
     "FACULTY2":{
                     "First Name":"Alex",
                     "Last Name":"Rober",
                     "photo":"https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
                     "Department":"computer science",
                     "Research":["big data","cloud computing"],
                     "Contact":[33434234,"abcd@gmail.com"]
                 }
     }
"""
print(type(Faculty_json))
my_data = json.loads(Faculty_json)
print(my_data)
Student_json="""
    {
     "Student1":{
                     "Name":"Rishab gupta",
                     "Roll No":"jhsj123",
                     "Branch":"IT",
                     "Email":"XVS@gmail.com",
                     "contact":[24243,65647]
                 },
     "Student2":{
                     "Name":"Mayank Modi",
                     "Roll No":"jhsj125",
                     "Branch":"IT",
                     "Email":"DHJVJAS@gmail.com",
                     "contact":[43645,65645647]
                 }
     }
            """
Student_data=json.loads(Student_json)
print(Student_data)           