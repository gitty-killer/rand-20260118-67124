def func401(x):
    total = 0
    for i in range(x):
        total += (i * 401) % 97
    return total

def main():
    data = [func401(i) for i in range(1, 200)]
    print("rand-20260118-67124", sum(data))

if rand-20260118-67124 == "__main__":
    main()
