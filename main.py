import subprocess

def create_session():
    subprocess.run(["python", "register.py"])

def run_bot():
    subprocess.run(["python", "query.py"])
    subprocess.run(["python", "tap.py"])

def main():
    while True:
        print("Select an option:")
        print("1. Create session")
        print("2. Run bot")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_session()
        elif choice == "2":
            run_bot()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
