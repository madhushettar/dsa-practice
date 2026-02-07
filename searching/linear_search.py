# Linear search implementation
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

if __name__ == "__main__":
    example = [10, 20, 30, 40]
    target = 30
    print("Index found:", linear_search(example, target))
