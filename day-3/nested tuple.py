record=("Order-501",["chai","biscuit"])
print(record)
# record[0]="Order-502"  this will give typeerror because order-501 is a tupple and oit cannot be change into order-502
record[1].append("cake")  # now it will add cake because from index 1 there is a list starting insidea tuple and and we can make changes inside a list
print(record)