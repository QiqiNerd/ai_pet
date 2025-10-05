# AI Pet Designer

print("🐾 Welcome to the AI Pet World!")
pet_name = input("What do you want to name your pet? ")
pet_type = input("What kind of animal is it? (e.g., cat, dog, dragon) ")
pet_trait = input("What is its personality? (e.g., friendly, shy, playful) ")

print(f"\nAwesome! You now have a {pet_trait} {pet_type} named {pet_name}! 🐾")
print(f"{pet_name}: Hi! I'm your pet {pet_name}. You can talk to me or ask me to do things.")
print("You can type one of these commands: talk / sing / play / feed / sleep / bye")

# Simple happiness system
happiness = 5  # Ranges from 0 (sad) to 10 (very happy)

while True:
    command = input("\nWhat do you want me to do?\n> ").lower()

    if command == "talk":
        if happiness > 7:
            print(f"{pet_name}: I'm feeling AMAZING today! 😸")
        else:
            print(f"{pet_name}: I'm ok, just a little bored. 😺")
        happiness += 1
    elif command == "sing":
        print(f"{pet_name}: Meow meow~ 🎵 That’s my favorite song!")
        happiness += 1
    elif command == "play":
        print(f"{pet_name}: Woohoo! Let's play fetch with the ball! 🏀")
        happiness += 2
    elif command == "feed":
        print(f"{pet_name}: Yum! I love my food! 🍲 Thank you!")
        happiness += 2
    elif command == "sleep":
        print(f"{pet_name}: Zzz... Taking a little nap... 💤")
        happiness -= 1
    elif command == "bye":
        print(f"{pet_name}: Okay, see you next time! I’ll miss you! 🐾")
        break
    else:
        print(f"{pet_name}: Hmm... I don't understand that. Try: talk / sing / play / feed / sleep / bye")

    # Keep happiness within 0 to 10
    if happiness > 10:
        happiness = 10
    elif happiness < 0:
        happiness = 0

    # Show happiness visually
    print(f"{pet_name}'s happiness level: {'💖' * happiness}{'🤍' * (10 - happiness)}")

print("🎮 Thanks for playing with your AI pet. Goodbye!")
