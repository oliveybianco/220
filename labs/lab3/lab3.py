"""
Name: <Olivia Bianco>
<lab3>.py

Problem: <Traffic function.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


def traffic():
    num_roads = eval(input("How many roads were surveyed? "))
    road_avg = 0
    total_cars = 0
    for road in range(num_roads):
        day_avg = 0
        num_days = eval(input("How many days was the road surveyed? " + str(road + 1)))
        for day in range(num_days):
            num_cars = eval(input("How many cars traveled on day" + str(day + 1) + "?"))
            day_avg = day_avg + num_cars / num_days
            total_cars = total_cars + num_cars
            road_avg = total_cars / num_roads
        print("Average number of cars on this road per day:", day_avg)
    print("Total number of vehicles traveled on all roads: ", total_cars)
    print("Average number of vehicles per road: ", road_avg)


traffic()
