import random


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
        if not (isinstance(min, int) and isinstance(max, int)): #check for errors
            print("")
            raise ValueError("Input values must be integers")
        return random.randint(min, max)                         #returns random int
    
    except ValueError as error:                                 #error correction
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
    
    return random.choice(['+', '-', '*'])


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
    p = f"{n1} {operation} {n2}"
    if operation == '+': answer = n1 + n2
    elif operation == '-': answer = n1 - n2
    else: answer = n1 * n2
    return p, answer

def math_quiz():
    """
    Starts the math quiz.
    """
    
    score = 0
#     t_q = 3.14159265359
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    try:                                                     #error checking
        if not isinstance(t_q, int):
            raise ValueError("t_q has to be an integer.")
    except ValueError as error:                              #error correction
        print(f"Error: {error}")
        
    for _ in range(t_q):
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

    print(f"\nGame over! Your score is: {score}/{t_q}")

if __name__ == "__main__":
    math_quiz()
