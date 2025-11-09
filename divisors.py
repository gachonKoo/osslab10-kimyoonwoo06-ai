def get_divisors(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])   # 명령줄에서 숫자 받아오기
    divisors = get_divisors(n)
    for d in divisors:
        print(d)