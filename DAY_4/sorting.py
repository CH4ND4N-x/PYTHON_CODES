#Sorting 
students_list= []

while True:
    user_input = input("Enter name, age ,score: ")
    
    if not user_input:
        break
    
    name, age, marks = user_input.split(",")
    
    students_list.append( (name, int(age), int(marks) ) )

students_list.sort()
print (students_list)