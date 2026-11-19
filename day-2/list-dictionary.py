registered_codename = ["Shadow", "Phantom", "Venom", "Revenant"]
agent_file ={ "Name":"Sohini",
             "Codename":"Revenant",
             "Grade":"Special Grade"}
print(f"Agent {agent_file["Codename"]} your new mission is updated!! check the dashboard.")
print(f"Agent {agent_file["Codename"]} your grade has updated to {agent_file["Grade"]}.")

new_name = input("Enter the codename you want:")
for name in registered_codename:
    if new_name == name:
        print(f"Agent {agent_file["Name"]} the code name you want is not availabe.")
        break
else:
    print(f"Agent {agent_file["Name"]} your Codename is available")
    agent_file["Codename"]= new_name
    print(f"Agent{agent_file["Name"]} Your new codename is {agent_file["Codename"]}")
    registered_codename.append(new_name)
    print(f"The updated list of taken codenames are{registered_codename}")
