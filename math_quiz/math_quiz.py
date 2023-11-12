import random

TOTAL_QUESTIONS = 3

def randomInt(min, max):
    """
    Chooses a random integer between the given borders.
    
    Args: 
        min(int): Minimum value
        max(int): Maximum value
        
    Returns: 
        A random integer between a given min and max value.
        
    Example:
        randomInt(2,7)
    """
    
    try:  
        #check for errors
        if not (isinstance(min, int) and isinstance(max, int)): 
            print("")
            raise ValueError("Input values must be integers")
        return random.randint(min, max)                         #returns random int
    
    #error correction
    except ValueError as error:                                 
        print(f"ERROR: {error}")
        print("USE ROUNDED VALUES")
        result = random.randint(round(min),round(max))
        return result


def randMathOperation():
    """
    Chooses a random mathematical operation.
    
    Returns: 
         Either +, -, *
        
    Example:
        randMathOperation() 
    """

    try:
        return random.choice(['+', '-', '*'])
    except IndexError:
        return "Error: The list of operations is empty."
    


def calc(n1, n2, operation):
    """
    Calculates two numbers with a given operation.
    
    Args: 
        n1: first number
        n2: second number
        operation: mathematical operation
    
    Return: 
        A tuple with the calculation string and the result of the calculation
        
    Example: 
        calc(3,4,'+') 
    
    """

    problem = f"{n1} {operation} {n2}"
    if operation == '+': answer = n1 + n2
    elif operation == '-': answer = n1 - n2
    else: answer = n1 * n2
    return problem, answer

def math_quiz():
    """
    Starts the math quiz.
    """
    
    score = 0

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    #error checking if TOTAL_QUESTIONS is an integer
    try:                                                     
        if not isinstance(TOTAL_QUESTIONS, int):
            raise ValueError("TOTAL_QUESTIONS has to be an integer.")
    #error correction if its no integer
    except ValueError as error:                              
        print(f"Error: {error}")
        
    for _ in range(TOTAL_QUESTIONS):
        n1 = randomInt(1, 10); n2 = randomInt(1, 5); operation = randMathOperation()
        

        PROBLEM, ANSWER = calc(n1, n2, operation)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{TOTAL_QUESTIONS}")

if __name__ == "__main__":
    math_quiz()
