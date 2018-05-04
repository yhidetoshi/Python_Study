def exception_test(value1, value2):
    print('star calc')
    result = 0

    try:
        result = value1 + value2
    except:
        print('can not calc')
    finally:
        print('end')

    return result

print(exception_test(100, 200))
print(exception_test(100, '200'))

"""
star calc
end
300
star calc
can not calc
end
0
"""
