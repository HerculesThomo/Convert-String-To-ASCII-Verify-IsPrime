"""
/*
* This method urges the user to
* insert a String or a number. A number is convertible to ascii code as well
* @ return userInput: Returns the user's input
*/
"""
def get_inserted_string():
     userInput = (input("Insert a string or a number: "))
     return userInput
"""
/*
* This method converts the user's input into
* ASCII code
* @ return sum: Returns the ascii code of the String
*/
"""
def convert_string_into_ascii_code(number):
    sum = 0
    for i in range(len(number)):
        sum += ord(number[i])
    return sum
"""
/*
* It defines if the number is prime
* or not
* @ return counter: Returns a number. if the number is 2 this means that the number is devided only with 1 and its self so it's a prime number.
* if the division is a number other than 2 it's not a prime number
*/
"""
def isPrime(number):
    counter = 0
    for i in range(1, number + 1):
        if(number % i == 0 ):
            counter = counter + 1
    return counter
"""
/*
* This method displays whether the number is
* prime or not
*/
"""
def displayIsPrime(flag):
    print("The number is prime" if flag == 2 else "The number is not prime")
"""
/*
* This is the main method where the program actually begins
*/
"""
def main():
    nextIteration = 'yes'
    print("This program converts a string or a number into ascii code and checks if it's a prime number or not!")
    while(nextIteration.casefold() == 'yes'):
        alphanumeric = get_inserted_string()
        asciiNumber = convert_string_into_ascii_code(alphanumeric)
        print("The converted String in ascii code is: " + str(asciiNumber))
        flag = isPrime(asciiNumber)
        displayIsPrime(flag)
        nextIteration = input("Type 'yes' if you want to continue or anything else to stop: ")
    print("Terminating the program!")

main()
