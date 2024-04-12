import random

class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What does OOP stand for?",
                "options": ["Object Oriented Programming", "Object Oriented Protocol", "Object Oriented Process"],
                "answer": "Object Oriented Programming"
            },
            {
                "question": "What does MVC stand for?",
                "options": ["Model View Controller", "Model View Component", "Model Visual Controller"],
                "answer": "Model View Controller"
            },
            {
                "question": "Which language is known for its simplicity and readability?",
                "options": ["Python", "Java", "C++"],
                "answer": "Python"
            },
            {
                "question": "What is the output of 2 + 2 * 2?",
                "options": ["4", "6", "8"],
                "answer": "6"
            },
            {
                "question": "Which of the following is not a version control system?",
                "options": ["Git", "Subversion", "MySQL"],
                "answer": "MySQL"
            }
        ]
        self.score = 0

    def start_quiz(self):
        print("Welcome to the Software Engineer Quiz Game!")
        print("Answer the following questions:")
        random.shuffle(self.questions)
        for i, q in enumerate(self.questions):
            print(f"\nQuestion {i+1}: {q['question']}")
            random.shuffle(q['options'])
            for j, opt in enumerate(q['options']):
                print(f"{j+1}. {opt}")
            user_answer = input("Your answer (enter option number): ").strip()
            if user_answer == str(q['options'].index(q['answer']) + 1):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
                print(f"The correct answer is: {q['answer']}")
        print("\nQuiz completed!")
        print(f"Your score: {self.score}/{len(self.questions)}")

class RecruiterQuiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What qualities do you value the most in a candidate?",
                "options": ["Technical skills", "Problem-solving ability", "Communication skills", "All of the above"],
                "answer": "All of the above"
            },
            {
                "question": "How do you assess a candidate's cultural fit?",
                "options": ["Through technical assessments", "By evaluating their previous work experience", "Through behavioral interviews", "All of the above"],
                "answer": "All of the above"
            },
            {
                "question": "What programming languages are essential for the roles you hire for?",
                "options": ["Python", "Java", "JavaScript", "All of the above"],
                "answer": "All of the above"
            },
            {
                "question": "How important is continuous learning and growth mindset in a candidate?",
                "options": ["Not important", "Somewhat important", "Very important", "Critical"],
                "answer": "Critical"
            },
            {
                "question": "What level of experience are you looking for in candidates?",
                "options": ["Entry-level", "Mid-level", "Senior-level", "Depends on the role"],
                "answer": "Depends on the role"
            },
            {
                "question": "How do you gauge a candidate's teamwork and collaboration skills?",
                "options": ["Through group projects", "By asking about their previous team experiences", "Through reference checks", "All of the above"],
                "answer": "All of the above"
            },
            {
                "question": "What soft skills do you prioritize in candidates?",
                "options": ["Time management", "Adaptability", "Leadership", "All of the above"],
                "answer": "All of the above"
            },
            {
                "question": "How do you handle cultural diversity in your hiring process?",
                "options": ["By promoting diversity and inclusion initiatives", "By ensuring unbiased evaluation criteria", "By offering diversity training to interviewers", "All of the above"],
                "answer": "All of the above"
            }
        ]
        self.score = 0

    def start_quiz(self):
        print("Welcome to the Software Engineer Recruiter Quiz!")
        print("Answer the following questions:")
        for i, q in enumerate(self.questions):
            print(f"\nQuestion {i+1}: {q['question']}")
            for j, opt in enumerate(q['options']):
                print(f"{j+1}. {opt}")
            user_answer = input("Your answer (enter option number): ").strip()
            if user_answer == str(q['options'].index(q['answer']) + 1):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
                print(f"The correct answer is: {q['answer']}")
        print("\nQuiz completed!")
        print(f"Your score: {self.score}/{len(self.questions)}")

def main():
    choice = input("Choose quiz type (1 for Software Engineer Quiz, 2 for Software Engineer Recruiter Quiz): ")
    if choice == "1":
        quiz = Quiz()
        quiz.start_quiz()
    elif choice == "2":
        recruiter_quiz = RecruiterQuiz()
        recruiter_quiz.start_quiz()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
