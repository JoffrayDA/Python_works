cities = ["Paris", "Rome", "Berlin", "Madrid", "Lisbon"]
durations = [3, 5, 2, 4, 6]      # en jours
budgets = [450, 600, 300, 500, 700]  # en euros

#Display all cities with their duration and budget
for city, duration, budget in zip(cities,durations,budgets):
    print(city, "-", duration, "days - ", budget,"€")

#Add a new city 
cities.append("Vienna")
durations.append(4)
budgets.append(550)

#Find the cheapest city
budgets.sort()
print("The chepeast city is :", budgets[0])