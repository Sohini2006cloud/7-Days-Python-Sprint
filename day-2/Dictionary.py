agent_file ={ "Name" : "Sohini",
               "Special id": "008",
               "grade" :"Special Agent"}
print(f"Agent {agent_file["Name"]} Your next Mission is to Spy on Rudransh Rathore.")
print(f"Agent {agent_file["Special id"]} your new partner will be James Bond.")

agent_file["Special id"] = int(input("Enter the id you would like:"))
print(f"Agent {agent_file["Name"]} your new id for mission is {agent_file["Special id"]}.")