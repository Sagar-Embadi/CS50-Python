def main():
    greeting = input("Greeting: ")
    value_to_print = value(greeting)
    print(f"${value_to_print}")

def value(greeting):
    greeting = greeting.lower().strip()
    if 'hello' in greeting:
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
