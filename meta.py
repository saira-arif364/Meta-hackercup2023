# Step 1: Read the number of test cases
T = int(input())

# Step 2: Loop over each test case
for i in range(T):
    # Step 2a: Read the values of S, D, and K
    S, D, K = map(int, input().split())

    # Step 2b: Calculate the number of buns, cheese slices, and patties
    total_buns=S * 4 +D *2
    total_patties = S + D *2
    total_cheese= S +D *2

    # Step 2c: Check if there are enough ingredients for a K-decker cheeseburger
    if K <= total_buns // 2 and K <= total_cheese and K <= total_patties:
        print(f"Case #{i+1}: YES")
    else:
        print(f"Case #{i+1}: NO")
