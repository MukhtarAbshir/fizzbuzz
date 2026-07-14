def fizzbuzz():
    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))

    for number in range(start, end +1 ):

        if number %15 == 0 :
            print("Fizzbuzz")
        elif number %5 == 0 :
            print("Buzz")
        elif number %3 == 0 :
            print("Fizz")
        else:
            print(number)

fizzbuzz()
