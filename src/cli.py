def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="My Python CLI Tool")
    parser.add_argument("command", type=str, help="The command to execute")
    parser.add_argument("--option", type=str, help="An optional argument for the command")

    args = parser.parse_args()

    if args.command == "greet":
        greet(args.option)
    else:
        print(f"Unknown command: {args.command}")

def greet(name: str) -> None:
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")

if __name__ == "__main__":
    main()