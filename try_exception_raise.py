def exception_test(value1, value2):
    print('star calc')
    result = 0

    try:
        result = value1 + value2abs
    except:
        print('計算できなかった')
        raise
    finally:
        print('計算終了')

    return result

try:
    print(exception_test(100, 100))
    print(exception_test(100, 200))
    print(exception_test(100, '300'))
except:
    print('エラーを受け取った')
