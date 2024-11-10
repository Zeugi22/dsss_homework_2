import random

def create_random_number(min, max):
    """Returns a random integer in a range from min to max including both."""

    return random.randint(min, max)

def choose_operation():
    """Randomly returns one of the given operations '+', '-' and '*' as a string."""

    return random.choice(['+', '-', '*'])

def generate_problem(nr1, nr2, op):
    """
    Creates a mathematical problem and its answer from two numbers and an operator.
    
    Args:
        nr1 (int): first number
        nr2 (int): second number
        op (string): operator

    Returns:
        (problem, answer):
        problem (string): composed of all three args, answer (int): correct answer to the problem.
    """
    #create problem as f-string
    problem = f"{nr1} {op} {nr2}"

    #calculate answer to problem by differentiating the operator
    if op == '+': answer = nr1 + nr2
    elif op == '-': answer = nr1 - nr2
    else: answer = nr1 * nr2

    return problem, answer

def math_quiz():
    """
    Starts a quiz containing four simple mathematical problems.

    -four problems
    -userinput requested for each problem
    -one chance to answer for each problem
    -score is being tracked and printed at the end
    """
    score = 0
    number_of_problems = 4

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    #loop for the 4 problems
    for _ in range(number_of_problems):
        #create the 3 parts of a problem
        nr1 = create_random_number(1, 10); nr2 = create_random_number(1, 6); op = choose_operation()

        PROBLEM, ANSWER = generate_problem(nr1, nr2, op)
        print(f"\nQuestion: {PROBLEM}")
        #loop to ensure correct input format
        while(1):
            useranswer = input("Your answer: ")
            try:
                useranswer = int(useranswer)
            except:
                print("invalid numberformat: please enter an integer!")
            else:
                break
        
        #checking, if useranswer is correct, and edit score, if needed
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{number_of_problems}")

if __name__ == "__main__":
    math_quiz()
