marksheet ={ "Sub1":"Marks1",
             "Sub2":"Marks2",
             "Sub3":"Marks3"
             }
marksheet["Sub1"]= input("Enter Your First Subject:")
marksheet["Marks1"]=int(input("Enter your marks for the subject-1 :"))
marksheet["Sub2"]= input("Enter Your second Subject:")
marksheet["Marks2"]=int(input("Enter your marks for the subject-2 :"))
marksheet["Sub3"]= input("Enter Your third Subject:")
marksheet["Marks3"]=int(input("Enter your marks for the subject-3:"))
print(f"You got {marksheet["Marks1"]} in subject {marksheet["Sub1"]}")
print(f"You got {marksheet["Marks2"]} in subject {marksheet["Sub2"]}")
print(f"You got {marksheet["Marks3"]} in subject {marksheet["Sub3"]}")
print(f"Your Marksheet for this semester :{marksheet}")