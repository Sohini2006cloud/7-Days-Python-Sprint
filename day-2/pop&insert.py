agent_list =["Gojo","Yuta","Sohini","megha"]
print("The Original Team:",agent_list)
new_agent=input("Enter your name new agent:")
retired_agent = agent_list.pop(0)
print(f"{retired_agent} has retired")
print("The new position of the team is:",agent_list)
agent_list.insert(1,new_agent)
print("\nFinal team :",agent_list)
