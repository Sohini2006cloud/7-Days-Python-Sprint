order_a ={101,102,103,102}
order_b ={103,104,105,103}
#How many uniqe id;
unique_id = order_a | order_b
print("All unique ids: ",unique_id)
#product-id that appeared in both
product_id= order_a & order_b
print("Ids that appeared in both order: ",product_id)
#convert into tuple
order_a_tuple = tuple(order_a)
sorted_copy=sorted(order_a_tuple)
print("Sorted Tuple: ",sorted_copy)
