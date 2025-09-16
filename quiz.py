# quiz game with levels.

import random
import time   # timer ke liye

# ✅ Questions with Levels
quiz = {
    "easy": [
        {"question": "1. What is the capital of INDIA ?", 
         "options": ["A. Bhopal", "B. Gujrat", "C. Delhi", "D. Haryana"], "answer": "C"},
        {"question": "2. Which planet is known as the Red Planet?", 
         "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"], "answer": "C"},
        {"question": "3. What is 5 * 6?", 
         "options": ["A. 11", "B. 25", "C. 30", "D. 56"], "answer": "C"},
    ],
    "medium": [
        {"question": "4. Who developed Python programming language?", 
         "options": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. James Gosling", "D. Charles Babbage"], "answer": "B"},
        {"question": "5. Who is the Father of the Nation of India?", 
         "options": ["A. Jawaharlal Nehru", "B. Subhas Chandra Bose", "C. Mahatma Gandhi", "D. Sardar Patel"], "answer": "C"},
        {"question": "6. Which gas do plants release during photosynthesis?", 
         "options": ["A. Carbon Dioxide", "B. Oxygen", "C. Nitrogen", "D. Hydrogen"], "answer": "B"},
    ],
    "hard": [
        {"question": "7. What is the largest mammal?", 
         "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Whale Shark"], "answer": "B"},
        {"question": "8. What is the national sport of India?", 
         "options": ["A. Cricket", "B. Football", "C. Hockey", "D. Kabaddi"], "answer": "C"},
        {"question": "9. Who was the first man to step on the Moon?", 
         "options": ["A. Yuri Gagarin", "B. Neil Armstrong", "C. Rakesh Sharma", "D. Michael Collins"], "answer": "B"},
        {"question": "10. Which is the smallest prime number?", 
         "options": ["A. 0", "B. 1", "C. 2", "D. 3"], "answer": "C"},
    ]
}


def play_quiz(level, timer_limit):
    score = 0
    questions = quiz[level][:]
    random.shuffle(questions)   # 🔀 har bar order change

    print(f"\n🎉 Welcome to the {level.upper()} Quiz! 🎉")
    print(f"⏱️ You have {timer_limit} seconds for each question!\n")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        start_time = time.time()
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        elapsed = time.time() - start_time

        if elapsed > timer_limit:
            print(f"⏰ Time's up! Correct answer was {q['answer']}\n")
        elif answer == q["answer"]:
            print("✅ Correct Answer!\n")
            score += 1
        else:
            print(f"❌ Wrong Answer! Correct is {q['answer']}\n")

    # Result
    print("🎯 Quiz Over!")
    print(f"Your Final Score: {score}/{len(questions)}")

    if score == len(questions):
        print("🏆 Excellent! Perfect Score!")
    elif score >= len(questions) // 2:
        print("👏 Good Job!")
    else:
        print("😢 Better Luck Next Time!")


# 🔁 Replay Loop with Levels
while True:
    print("\nChoose Level:")
    print("1. Easy (15 sec)")
    print("2. Medium (10 sec)")
    print("3. Hard (7 sec)")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        play_quiz("easy", 15)
    elif choice == "2":
        play_quiz("medium", 10)
    elif choice == "3":
        play_quiz("hard", 7)
    else:
        print("❌ Invalid choice, try again.")
        continue

    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("👋 Thanks for playing! Goodbye.")
        break