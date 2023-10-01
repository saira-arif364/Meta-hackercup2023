def apple_finder(apples):
    apples.sort()
    if len(apples) == 1:
        return apples[0]

    start = 0
    end = len(apples) - 1
    total = apples[start] + apples[end]
    prediction = -1
    prediction_count = 0

    while start < end:
        if prediction_count > 1:
            return -1

        start += 1
        end -= 1

        if start >= end:
            break

        if total != apples[start] + apples[end]:
            prediction = apples[start - 1]
            end += 1
            prediction_count += 1
            total = apples[start] + apples[end]

    return total - (apples[start] if prediction == -1 else prediction)

def main():
    with open("data.txt") as file:
        test_cases = int(file.readline().strip())

        for t in range(1, test_cases + 1):
            days = int(file.readline().strip())
            apples = list(map(int, file.readline().split()))

            result = apple_finder(apples)
            print(f"Case #{t}: {result}")

if __name__ == "__main__":
    main()
