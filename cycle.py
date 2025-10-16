import main

choice = input("Enter 'mod_a' or 'mod_b' to run a module: ")

if choice == 'mod_a':
    main.execute()
elif choice == 'mod_b':
    main.execute()
else:
    print("Invalid module choice.")
