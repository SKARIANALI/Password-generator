import random
import string
import argparse # Import the argparse library

def generate_strong_password(length: int) -> str:
    # Same function from Enhancement 1
    if length < 4:
        raise ValueError("Password length must be at least 4.")
    password_chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password_chars.extend(random.choices(all_chars, k=length - 4))
    random.shuffle(password_chars)
    return ''.join(password_chars)

def main():
    # 1. Setup the Argument Parser
    parser = argparse.ArgumentParser(
        description="A powerful command-line password generator."
    )

    # 2. Add Arguments
    parser.add_argument(
        "length", 
        type=int, 
        help="The desired length of the password (must be at least 4)."
    )
    parser.add_argument(
        "-c", "--copies", 
        type=int, 
        default=1, 
        help="Number of passwords to generate."
    )
    parser.add_argument(
        "-s", "--save", 
        metavar="FILENAME",
        help="Save the generated password(s) to a file."
    )
    
    # 3. Parse the arguments from the command line
    args = parser.parse_args()

    # 4. Main logic
    try:
        if args.length < 4:
            parser.error("Minimum password length must be 4.")

        passwords = [generate_strong_password(args.length) for _ in range(args.copies)]
        
        print("--- Generated Passwords ---")
        for pwd in passwords:
            print(pwd)
        
        if args.save:
            with open(args.save, "a") as f:
                for pwd in passwords:
                    f.write(pwd + "\n")
            print(f"\nSuccessfully saved {args.copies} password(s) to {args.save}")

    except ValueError as e:
        parser.error(str(e))


if __name__ == "__main__":
    main()