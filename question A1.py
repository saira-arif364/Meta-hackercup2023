def calculate(test_case, S, D, K):
    buns_we_have = 2 * (S + D)
    p_and_c = S * 1 + D * 2

    print(f"Case #{test_case}: ", end='')
    file.write(f"Case #{test_case}: ")

    if buns_we_have >= K + 1 and p_and_c >= K:
        print("YES")
        file.write("YES\n")
    else:
        print("NO")
        file.write("NO\n")

def main():
    test_cases = int(input())

    for tc in range(1, test_cases + 1):
        S, D, K = map(int, input().split())
        calculate(tc, S, D, K)

    file.close()

if __name__ == "__main__":
    main()
