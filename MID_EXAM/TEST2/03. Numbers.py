numbers = list(map(int, input().split()))

average = sum(numbers) // len(numbers)
numbers.sort(reverse=True)

result = [x for x in numbers if x > average][:5]
if result:
    print(' '.join(str(x) for x in result))
else:
    print('No')
