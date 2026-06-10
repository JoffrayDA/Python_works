tasks = ["run", "shower", "breakfast", "revisions"]

#How many tasks ?
print("Nombre de tâches :", len(tasks))

#What is the first element in the list?
print("Premier élément de la liste :", tasks[0])

#What is the last element in the list?
print("Premier élément de la liste :", tasks[-1])

#Add an element to the list 
tasks.append('do shopping')
print("The element 'do shopping' has been added")

#Insert an element
tasks.insert(3,"swim")
print("The element 'swim' has been inserted at the 3rd index")

#What happens if you run tasks.remove("pizza")?
#There is an error because "pizza" is not in the list

#What exactly does the instruction tasks[0] = "intense workout" do?
#It will replace the first element of the list(run) and will replace it with "intense workout"

#Rewrite the loop so it displays each task along with its position number
for i in range(len(tasks)):
    print(i + 1,"-",tasks[i])

#Create a new list containing only the tasks that have more than 10 characters.
new_tasks = [t for t in tasks if len(t)>10]
print(new_tasks)

for i in tasks:
    print(i.upper())

#Sort the list alphabetically and display it.
tasks.sort()
print(tasks)







