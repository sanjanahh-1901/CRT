def right_triangle(n: int) -> str:
    for i in range(1, n + 1):
        print("*" * i)

if __name__ == "__main__":
    n = int(input())
    print(right_triangle(n))
