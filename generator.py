def curve(n):
    x = [0]
    for _ in range(n):
        for i in reversed(x):
            x.append((i-1) % 4)
    return x


with open('curve.js', 'w') as f:
    f.write('var curve =')
    f.write(str(curve(21)))
