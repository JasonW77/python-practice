def binary_search_visualize(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        mid = (low + high) // 2
        steps += 1

        #Visual display
        print(f"\nStep {steps}:")
        print("Current range:", arr[low:high+1])
        print(f"Low: {low} | Mid: {mid} | High: {high}")
        print(f"Comparing target {target} to {arr[mid]}")

        if arr[mid] == target:
            print(f"\n✅ Found {target} at index {mid} in {steps} steps.")
            return
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    
    print(f"\n❌ {target} not found after {steps} steps.")

def main():
    print("🔍 Binary Search Visualizer")
    nums = input("Enter a sorted list of numbers (comma-seperated): ")
    arr = [int(x.strip()) for x in nums.split(",")]
    target = int(input("Enter a number to search for: "))
    binary_search_visualize(arr, target)

if __name__ == "__main__":
    main()