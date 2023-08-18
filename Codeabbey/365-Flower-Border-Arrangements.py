import functools

@functools.lru_cache(maxsize=1000000)
def score(string):
    N = sum(plant == 'R' for plant in string)

    if len(string) < 2:
        return N

    if len(string) % 2 == 0:
        half_len = len(string) // 2
        left_score = score(string[:half_len])
        right_score = score(string[half_len:])
        computed_score = N + max(left_score, right_score)
    else:
        half_len = len(string) // 2
        left_score = score(string[:half_len + 1])
        right_score = score(string[half_len + 1:])
        computed_score = N + max(left_score, right_score)

    return computed_score


def generate_positions_util(N, Nr, Score, start, positions):
    if Nr == 0:
        plants = ['R' if i in positions else 'B' for i in range(N)]
        string = ''.join(plants)
        if score(string) == Score:
            return 1
        else:
            return 0

    count = 0
    for i in range(start, N - Nr + 1):
        positions.add(i)
        count += generate_positions_util(N, Nr - 1, Score, i + 1, positions)
        positions.remove(i)

    return count


# Read input
T = int(input())
Answer = []

for _ in range(T):
    Score, N, Nr = map(int, input().split())
    count = generate_positions_util(N, Nr, Score, 0, set())
    Answer.append(count)

print(' '.join(map(str, Answer)))
