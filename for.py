
## ex1 range
for i in range(1, 5):
    print(i)

## ex2 for break
strings =['ruby', 'python', 'perl', 'java', 'c']
for string in strings:
    if string == 'python':
        print('ok')
        break
    print(string)

## ex3 for continue
strings = ['ruby', 'python', 'perl', 'java', 'c']
for string in strings:
    if string != 'python':
        print(string)
        continue
    print('ok')
    break
