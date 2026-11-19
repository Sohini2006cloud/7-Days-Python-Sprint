agents =["Gojo","Yuta","Maki","Geto"]
print("The original Team members are:",agents)
retired_agents = agents.pop(0)
print(f"{retired_agents}has retired from the team.")
print("The current Team members are:",agents)
new_agent = input("enter your name:")
agents.insert(1,new_agent)
print("The new members are:",agents)
for index, agents in enumerate(agents):
    print(f"{index}. {agents}")
