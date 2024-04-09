import sys

def main():
    # Parse arguments
    if len(sys.argv) != 3:
        print("Usage: python sports.py <username> <sport>")
        return

    username = sys.argv[1]
    sport = sys.argv[2]

    # Display information based on recommendation
    print(f"Welcome {username}! Displaying information for {sport}")

if __name__ == "__main__":
    main()