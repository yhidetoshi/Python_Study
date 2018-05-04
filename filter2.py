#def even_evaluator(x):
def even_evaluator(x:int)->bool:
    return x % 2 ==0

#print(even_evaluator(18))

num_list = list(range(10))
even_list = filter(even_evaluator, num_list)
print(list(even_list))

num_list2 = list(range(10))
even_list2 = filter(lambda n : n%2==0 , num_list2)
print(list(even_list2))
