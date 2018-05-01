input1 = input()
input2 = input()
input3 = input()

answer = [input1, input2, input3]
dog_cnt = 0
cat_cnt = 0

for val in answer:
    if val == 'dog':
        dog_cnt += 1
    if val == 'cat':
        cat_cnt += 1

if dog_cnt > cat_cnt:
        print("dog")
else:
        print("cat")
