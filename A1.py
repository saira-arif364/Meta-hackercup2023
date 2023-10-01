def read_input_from_file(file_path):
    with open("cheeseburger_corollary_1_input.txt", 'r') as file:
        lines = file.readlines()

    return lines

def calculate(S, D, K):
    bunsWeHave = 2 * (S + D)
    pAndc = (S * 1) + (D * 2)

    if bunsWeHave >= K + 1:
        if pAndc >= K:
            return "YES"

    return "NO"

def main():
    lines = read_input_from_file("input.txt")
    test_cases = int(lines[0])

    for tc in range(1, test_cases + 1):
        S, D, K = map(int, lines[tc].split())
        result = calculate(S, D, K)
        output = f"Case #{tc}: {result}"
        print(output)

if __name__ == "__main__":
    main()
