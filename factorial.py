def loop_factorial(num):
    ans = 1
    for i in range(num):
        ans *= (i+1)
    return ans


def recursion(num):
    if num == 1:
        return 1
    if num == 2:
        return 2    
    return num * recursion(num - 1)


if __name__ == "__main__":
    # 5 factorial
    # print(loop_factorial(5))
    print(recursion(1))
