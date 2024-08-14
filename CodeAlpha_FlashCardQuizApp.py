class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardApp:
    def __init__(self):
        self.flashcards = []
        self.score = 0

    def add_flashcard(self, question, answer):
        flashcard = Flashcard(question, answer)
        self.flashcards.append(flashcard)

    def quiz(self):
        self.score = 0
        for flashcard in self.flashcards:
            print(f"Question: {flashcard.question}")
            user_answer = input("Your answer: ")
            if user_answer.lower() == flashcard.answer.lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {flashcard.answer}")
        print(f"Your final score is: {self.score}/{len(self.flashcards)}")

def main():
    app = FlashcardApp()
    while True:
        print("\n1. Add flashcard\n2. Quiz yourself\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            app.add_flashcard(question, answer)
        elif choice == '2':
            app.quiz()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

