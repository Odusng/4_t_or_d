import random

# List of truth questions and dares
truths = [
    "What's the most embarrassing thing you've ever done?",
    "Have you ever lied to get out of trouble?",
    "What’s your biggest fear?",
    "If you could be invisible for a day, what’s the first thing you would do?",
    "Have you ever had a crush on someone in this room?"
]

dares = [
    "Do 10 push-ups right now!",
    "Send a funny selfie to the last person you chatted with.",
    "Dance for 30 seconds with no music.",
    "Talk in a funny accent for the next 2 minutes.",
    "Text your crush and say ‘I have a confession...’"
]

print("🔥 Welcome to Truth or Dare! 🔥")
while True:
    choice = input("\nPick one - Truth (T) or Dare (D)? (Press Q to quit): ").strip().lower()

    if choice == 't':
        print("🗣️ Truth:", random.choice(truths))
    elif choice == 'd':
        print("💪 Dare:", random.choice(dares))
    elif choice == 'q':
        print("Game Over! Thanks for playing! 🎉")
        break
    else:
        print("Bruh, choose 'T' for Truth, 'D' for Dare, or 'Q' to quit. No do anyhow! 😆")
