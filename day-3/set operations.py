enrolled_python={"Riya","Kabir","Ananya","Dev"}
completed_task={"Kabir","Dev","Meera"}
both_set= enrolled_python & completed_task
print("Student who are in both sets are: ",both_set)
uncomplete_task = enrolled_python - completed_task
print("Student who haven't completed their task are: ",uncomplete_task)
every_one= enrolled_python | completed_task
print("Every student across both sets are:",every_one)