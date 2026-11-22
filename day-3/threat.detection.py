threat_name= input ("Enter the threat name:")
danger_level = int(input("Enter the danger level score:"))

for countdown in range(3,0,-1):
    print(f"{countdown}...",end = " ")
print()

if 90 <= danger_level <= 100:
    print(f"TheThreat {threat_name} that has danger level score {danger_level} is classified as a Catastrophic Threat, Evacuate Immidiately.")
elif 60 <= danger_level <= 89:
    print(f"TheThreat {threat_name} that has danger level score {danger_level} is classified as a High Risk Threat, Dispatch Elite Units.")
elif 30 <= danger_level <= 59:
    print(f"TheThreat {threat_name} that has danger level score {danger_level} is classified as a Moderate Threat, Standard patrol required.")
else:
    print(f"TheThreat {threat_name} that has danger level score {danger_level} is classified as a Low-Level Threat, Area is secured.")

