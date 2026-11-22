book_info=("Atomic Habits", 450, "Self-Help")
title,price,genre = book_info
print("Title of the book is ",title) 
print(f"Price of the book is {price} rupees.")
print(f"It is a {genre} book.")
a_tuple=tuple(book_info)
list_info=list(a_tuple)
list_info[1]=399
print(list_info)
book_info=tuple(list_info)
print(book_info)
name,cost,category =book_info
print(f"New price of the book is {cost} rupees")