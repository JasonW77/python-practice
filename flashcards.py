def run_quiz(questions):
    score = 0
    for i, (question, answer) in enumerate(questions.items(), start=1):
        print(f"\nQuestions {i}: {question}")
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == answer.lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was: {answer}")
    print(f"\nYou got {score}/{len(questions)} correct.")

def main():
    flashcards = {
        "What is the capital of France?": "Paris",
        "What language is primarily used for web development?": "HTML",
        "What does CPU stand for?": "Central Processing Unit",
        "What is the square root of 64?": "8",
        "What Python keyword defines a function?": "def"
    }

    print("🧠 Flashcard Quiz Time!")
    run_quiz(flashcards)
    
if __name__ == "__main__":
    main()