from itertools import product



def maximize_expression(K, M, lists):
    max_value=0
    for combination in product(*lists):
        current_sum = sum(x ** 2 for x in combination)
        current_value = current_sum % M
        max_value = max(max_value, current_value)
    return max_value



if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
