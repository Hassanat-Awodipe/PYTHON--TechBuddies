import math
from statistics import geometric_mean, harmonic_mean, mean
import cmath



def menu():

    print ("""\nThis program can perform the following mathematical operations.
Please select a number to get to the formula you are interested in. 
Then press Enter to continue: """)

    Userchoice = int(input("""\n1.Addition 
    \n2.Subtraction 
    \n3.Multiplication
    \n4.Division 
    \n5.Simple_average 
    \n6.Weighted_average 
    \n7.Geometric_average 
    \n8.Harmonic_average 
    \n9.Quadratic_root 
    \n\n"""))


    #Addition
    if Userchoice == 1:
            print("\nAddition") 
            try:
                UserInput = input("\nPlease, enter the numbers to be added separated by a space: " )

                def add(UserInput):
                    """The required argument is a list of numbers 

                    Only a single list of numbers can be added at once. The numbers have
                    to be separated by a space i.e you only have to click the spacebar once.

                    Parameters
                    ------------
                    int or float

                    Returns
                    ---------
                    A single float number is returned as the sum of the list

                    Example
                    >>> userinput = 1 2 3 4 5 6
                    >>> add(userinput) 
                    >>> answer = 21.0
                    """

                    UserInput = UserInput.split(' ')
                    UserInput = list(map(float, UserInput))
                    return math.fsum(UserInput)
                                
                print(add(UserInput))

            except ValueError as error:
                print ("\nSorry, you have entered an invalid input") 
        
            except Exception as error:
                print (error)

    
        #Subtraction of Numbers
    if Userchoice == 2:
        print ("\nSubtraction")
        try:
            FirstInput = input("\nPlease, enter the first list of numbers separated by a space: ")
            SecondInput = input("\nPlease, enter the second list of numbers separated by a space: ")
            print("\nplease note that the subtraction will be done as list1 - list2")
            def subtract(FirstInput, SecondInput):

                """The required argument are two lists of numbers.  
        
                The two lists may contain a single number each. The second list is subtracted from 
                the first list. The numbers in the list have to be separated by a space i.e you
                only have to click the spacebar once.
            
                Parameters
                ------------
                int or float

                Returns
                ---------
                A list of float numbers is returned as the subtraction of the list. A single float 
                number may also be returned.

                Example
                >>> firstinput = 1 2 3 4 5 6
                >>> secondinput = 4 5 6 1 2 3
                >>> subtract(firstinput, secondinput) 
                >>> answer = [-3.0 -3.0 -3.0 3.0 3.0 3.0]
                """

                FirstInput = FirstInput.split(' ') ; SecondInput = SecondInput.split(' ')
                FirstInput = list(map(float, FirstInput)) ; SecondInput = list(map(float, SecondInput))
                return [i-j for i,j in zip(FirstInput, SecondInput)]

            print (subtract(FirstInput,SecondInput))

        except ValueError:
            print ("\nSorry, you have entered an invalid Input")

        except Exception as error:
            print (error)


    #Multiplication of multiple numbers
    if Userchoice == 3:  
        print ("\nMultiplication")
        try:
            UserInput = input("\nPlease, enter the numbers to be multiplied separated by a space: " )
            def multiply(UserInput):

                """The required argument is a list of numbers. 
    
                Only a single list of numbers can be multiplied at once. The numbers have
                to be separated by a space i.e you only have to click the spacebar once.
            
                Parameters
                ------------
                int or float

                Returns
                ---------
                A single float number is returned as the product of the list.

                Example
                >>> userinput = 1 2 3 4 5 6
                >>> multiply(userinput) 
                >>> answer = 720.0
                """

                UserInput = UserInput.split(' ')
                UserInput = list(map(float, UserInput))
                return math.prod(UserInput)
            
            print(multiply(UserInput))

        except ValueError:
            print ("\nSorry, you have entered an invalid Input")
            
        except Exception as error:
            print (error)
                

                        
    #Division of numbers
    if Userchoice == 4:
        print ("\nDivision")
        try:
            InputNumer = input("\nPlease, enter the list of numerators separated by a space: ")
            InputDenom = input("\nPlease, enter the list of denominators separated by a space: ")
            def divide(InputNumer, InputDenom):

                """The required arguments are two lists of numbers.  

                The two lists may contain a single number each. The first list is divided by 
                the second list. The numbers in the list have to be separated by a space i.e you
                only have to click the spacebar once.
            
                Parameters
                ------------
                int or float

                Returns
                ---------
                A list of float numbers is returned as the division of the list. A single float 
                number may also be returned.

                Example
                >>> inputnumer = 1 2 3 4 5 6
                >>> inputdenom = 4 5 6 1 2 3
                >>> divide(firstinput, secondinput) 
                >>> answer = [0.25 0.4 0.5 4.0 2.5 2.0]
                """

                InputNumer = InputNumer.split(' ') ; InputDenom = InputDenom.split(' ')
                InputNumer = list(map(int, InputNumer)) ; InputDenom = list(map(int, InputDenom))
                return [i/j for i,j in zip(InputNumer,InputDenom)]

            print(divide(InputNumer, InputDenom))

        except ValueError:
            print ("\nSorry, you have entered an invalid Input")

        except Exception as error:
            print (error)


    #Average
    if Userchoice == 5:
        print ("\nAverage")
        try:
            UserInput = input('\nPlease, enter the numbers separated by a space to find their average: ')
            def simple_avg(UserInput):

                """The required argument is a list of number.  

                The average is used to determine a single number representation of a list of numbers. The 
                numbers in the list have to be separated by a space i.e you only have to click the spacebar 
                once.
            
                Parameters
                ------------
                int or float

                Returns
                ---------
                A single float number is returned as the average of the list. 
                
                Example
                >>> userinput = 1 2 3 4 5 6
                >>> average(userinput) 
                >>> answer = 3.0
                """

                UserInput = UserInput.split(' ')
                UserInput = list(map(float, UserInput))
                return (math.fsum(UserInput))/(len(UserInput))

            print(simple_avg(UserInput))

        except ValueError:
            print ("\nSorry, you have entered an invalid Input")

        except Exception as error:
            print (error)


    #weighted average
    if Userchoice == 6:
        print ("\nWeighted Average")
        try:
            Weights = input('\nPlease, enter the set of weights (Ws) separated by a space: ')
            values = input('\nPlease, enter the set of values (Xs) separated by a space: ')
            if len(Weights) == len(values):
                def weighted_avg(Weights, values):

                    """The required arguments are two lists of numbers.  

                    The weighted average, unlike the simple average, considers the value of each weights.
                    The two lists must contain equal number of elements. The first list is multiplied by 
                    the second list then divided by the sum of the second list. The numbers in the list 
                    have to be separated by a space i.e you only have to click the spacebar once.
                
                    Parameters
                    ------------
                    int or float

                    Returns
                    ---------
                    A single float number is returned as the weighted average of the list. 
                    
                    Example
                    >>> weights = 1 2 3 4 5 6
                    >>> values = 4 5 6 1 2 3
                    >>> weighted_avg(weights, values) 
                    >>> answer = 3.05
                    """

                    Weights = Weights.split(' '); values = values.split(' ')
                    Weights = list(map(float, Weights)); values = list(map(float, values))
                    return (math.fsum([i*j for i,j in zip(Weights,values)])) / (math.fsum(values))

                print(weighted_avg(Weights, values))

            else: 
                print("\nThe numbers of weights and values have to be equal")

        except ValueError:
            print ("\nSorry, you have entered an invalid Input")

        except Exception as error:
            print (error)


    #Geometric Mean
    if Userchoice == 7:
        print ("\nGeometric mean")
        try:
            UserInput = input('\nPlease, enter the set of values (Xs) separated by a space: ')
            def geometric_mean(UserInput):

                """The required argument is a list of number.  

                The geometric mean is also used to determine a single number representation of 
                a list of numbers. The numbers in the list have to be separated by a space i.e 
                you only have to click the spacebar once.
            
                Parameters
                ------------
                int or float

                Returns
                ---------
                A single float number is returned as the geometric mean of the list. 
                
                Example
                >>> userinput = 1 2 3 4 5 6
                >>> geometric_mean(userinput) 
                >>> answer = 3.0
                """

                UserInput = UserInput.split(' ')
                n = len(UserInput)
                UserInput = list(map(float, UserInput))
                UserInput = math.prod([i for i in UserInput])
                return pow(UserInput, (1/n))

            print(geometric_mean(UserInput))

        except ValueError:
            print ("\nSorry, you have entered an invalid Input")

        except Exception as error:
            print (error)


    #Harmonic Mean
    if Userchoice == 8:
        print ("\nHarmonic mean")
        try:
            UserInput = input('\nPlease, enter the set of values (Xs) separated by a space: ')
            def harmonic_mean(UserInput):

                """The required argument is a list of number.  

                The harmonic mean is the reciprocal of the average of the reciprocals. The numbers 
                in the list have to be separated by a space i.e. you only have to click the spacebar once.
            
                Parameters
                ------------
                int or float

                Returns
                ---------
                A single float number is returned as the harmonic mean of the list. 
                
                Example
                >>> userinput = 1 2 3 4 5 6
                >>> harmonic_mean(userinput) 
                >>> answer = 2.45
                """

                UserInput = UserInput.split(' ')
                n = len(UserInput)
                UserInput = list(map(float, UserInput))
                UserInput = math.fsum([1/i for i in UserInput])
                return n/UserInput
                
            print(harmonic_mean(UserInput))

        except ValueError:
            print ("\nSorry, you have entered an invalid Input")

        except Exception as error:
            print (error)


    #Quadratic Root
    if Userchoice == 9:
        print ("\nQuadratic root")
        try:
            a = float(input("\nplease enter the coefficient of x^2: "))
            b = float(input("\nplease enter the coefficient of x: "))
            c = float(input("\nplease enter the constant value: "))
            def Quadratic_root(a,b,c):

                """The required arguments are numbers.  

                The quadratic roots are two unique answers of a quadratic 
                equation. The numbers in the list have to be separated by a space i.e. 
                you only have to click the spacebar once.
            
                Parameters
                ------------
                int or float

                Returns
                ---------
                Two float numbers are returned as the roots of the equation. 
                
                Example
                >>> userinput = 1 2 3
                >>> Quadratic_root(userinput) 
                >>> answer = -1 + 1.41j, -1 -1.14j
                """

                x1 = str((-b + (cmath.sqrt((b**2) - (4*a*c)))) / 2*a) 
                x2 = str((-b - (cmath.sqrt((b**2) - (4*a*c)))) / 2*a)
                return x1, x2

            print(Quadratic_root(a,b,c))

        except ValueError:
            print ("\nSorry, you have entered an invalid Input")

        except Exception as error:
            print (error)                                    


    if 1 < Userchoice > 9:
        print("you have selected a wrong number")
    
                                    
                                  
    restart =  input("""\nDo you wish to return to the main menu? 
yes or no: """).lower()
            
    if restart == "yes" :
        menu()
        
    else: 
        exit()
            
menu()
    
    
                                        