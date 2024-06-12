## Study Drill #2: 
## Write a completely new game. Maybe you don't like this one, so make your own. This is your computer; do what you want.

# Answer: 

print("""You have two paths. Which one will you pick?""")

path = input("> ")

if path == "1":
    print("You're starting understand that you are dreaming. Select dream paths")
    
    dream_path = input("> ")

    if dream_path == "1":
        print("Okay, now you're flying")
    elif dream_path == "2":
        print("You are eating a hamburger in your dream. Nice!")
    else:
        print(f"You've decided to ignore it. So you stopped dreaming, but you are still dreaming")

elif path == "2":
    print("You are starting to waking up. What should you do?")

    answer = input("> ")
    
    if answer == "1" or answer == "2":
        print("Okay, you are still sleeping.")
    else:
        print("You woke up.")

else:
    print("You stopped dreaming, but still sleeping. Are you aware that you were sleeping?")