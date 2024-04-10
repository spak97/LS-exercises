numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}
result = []
for v in numbers.values():
    result.append(v // 2)

print(result)