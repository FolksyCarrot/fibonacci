def fibonnaci(n):
    a = 0
    b = 1
    
    if type(n) != int:
        print("invalid entry. Please enter an integer")
        
    elif n <= 2:
        print("invalid entry. Please enter a number greater than 2")
        
    else:
        print(a)
        print(b)
        
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)
            
fibonnaci(5)


def fibonnaci_input():
    
    a = 0
    b = 1
    
    while True:
        try:
            n = int(input("Please enter a number greater than zero:"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        
        if n > 2:
            print(a)
            print(b)
        
            for i in range(2, n):
                c = a + b
                a = b
                b = c
                print(c)
            break
        else:
            print("That answer is invalid. Please enter a number greater than 2 and try again")
   
fibonnaci_input()