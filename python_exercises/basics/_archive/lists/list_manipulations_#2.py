travel_tasks = ["book_flight", "pack_bag", "check_documents", "charge_devices"]

#Print the total number of tasks in the list
print("Total number of tasks :",len(travel_tasks))

#Print the first element of the list.
print("First element in the list :",travel_tasks[0])

#Print the last element of the list.
print("Last element in the list :",travel_tasks[-1])

#Add a new element to the list: "buy_snacks"
travel_tasks.append("buy_snacks")

#Insert a new element at index 2: "check_weather".
travel_tasks.insert(2,"buy_snacks")

#Rewrite a loop that displays each task along with its position number.
for i in range(len(travel_tasks)):
    print(i+1, "-", travel_tasks[i])

#Create a new list containing only the tasks that have more than 12 characters

new_travel_tasks = [t for t in travel_tasks if len(t) >12]
print(new_travel_tasks)

#Print each element of the list in lowercase.
for i in travel_tasks:
    print(i.lower())    

#Sort the list alphabetically and print it.
travel_tasks.sort()
print(travel_tasks)









