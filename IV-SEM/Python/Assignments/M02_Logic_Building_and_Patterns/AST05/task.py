def number_triangle(n: int) -> str:
    for i in range(1, n + 1):
        print(str(i) * i)

if __name__ == "__main__":
    n = int(input())
    number_triangle(n)
