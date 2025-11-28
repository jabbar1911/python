#!/usr/bin/env python3
"""Quiz Game - Improved Version"""

import random

questions = [
    {"q": "What is the capital of France?", 
     "options": ["London", "Berlin", "Paris", "Madrid"], "ans": 2},

    {"q": "Which planet is known as the Red Planet?", 
     "options": ["Venus", "Mars", "Jupiter", "Saturn"], "ans": 1},

    {"q": "Who wrote Romeo and Juliet?", 
     "options": ["Dickens", "Austen", "Shakespeare", "Twain"], "ans": 2},

    {"q": "What is the largest ocean?", 
     "options": ["Indian", "Atlantic", "Arctic", "Pacific"], "ans": 3},

    {"q": "Which gas do plants release?", 
     "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "ans": 0},
]

def main():
    print("=" * 60)
    print("QUIZ GAME".center(60))
    print("=" * 60)

    score = 0
    q_list = random.sample(questions, min(5, len(questions)))

    for i, q in enumerate(q_list, 1):
        print(f"\nQ{i}: {q['q']}")
        for j, opt in enumerate(q['options'], 1):
            print(f"  {j}. {opt}")

        try:
            ans = int(input("\nYour answer (1-4): "))
            if ans < 1 or ans > 4:
                print("⚠ Invalid Choice! Skipped.")
                continue

            if ans - 1 == q['ans']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct: {q['options'][q['ans']]}")
        except:
            print("⚠ Invalid Input! Skipped.")

    print("\n" + "="*60)
    print(f"FINAL SCORE: {score}/{len(q_list)}")
    print("="*60)

if __name__ == "__main__":
    main()

