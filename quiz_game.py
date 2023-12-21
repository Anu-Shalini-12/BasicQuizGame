# quiz_game.py

def display_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def get_user_input():
    while True:
        try:
            user_input = int(input("Enter the number of your answer: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def run_quiz():
    # Define quiz questions, options, and correct answers
    questions = [
        "What is the capital of France?",
        "Who wrote Thirukural?",
        "What is the square root of 144?",
        "How many continents are there in the world?",
        "What is the largest planet in our solar system?",
        "In which year did World War I begin?",
        "Who wrote 'Romeo and Juliet'?",
        "Who discovered Telephone?",
        "What is the capital of Japan?",
        "Who developed the theory of relativity?"
    ]
    options = [
        ["Paris", "Berlin", "London"],
        ["Bharathiyar", "Thiruvalluvar", "Bharathidasan"],
        ["12", "10", "15"],
        ["5", "6", "7"],
        ["Earth", "Mars", "Jupiter"],
        ["1939", "1914", "1945"],
        ["William Shakespeare", "Jane Austen", "Charles Dickens"],
        ["Einstein", "GrahamBell", "Newton"],
        ["Tokyo", "Seoul", "Beijing"],
        ["Isaac Newton", "Albert Einstein", "Galileo Galilei"]
    ]
    correct_answers = [1, 2, 1, 3, 3, 2, 1, 2, 1, 2]

    # Initialize score
    score = 0

    # Run the quiz
    for i in range(len(questions)):
        display_question(questions[i], options[i])
        user_answer = get_user_input()

        if check_answer(user_answer, correct_answers[i]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answers[i]}.\n")

    # Display final score
    print(f"Quiz completed! Your final score is {score}/{len(questions)}.")

# Run the quiz if the script is executed directly
if __name__ == "__main__":
    run_quiz()
