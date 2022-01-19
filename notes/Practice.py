def convert():
    #get user input
    celsius = eval(input("What is the temperature in celsius?" ))
    #convert input from celsius to farenheit with the equation c * (9 / 5) + 32
    farenheit = celsius * 9/5 + 32
    #display result to user
    print("the temperature is", farenheit, "degrees farenheit.")

