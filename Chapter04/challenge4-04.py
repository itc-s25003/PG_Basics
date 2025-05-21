def divideByTwo(x):
    """
    この関数は、引数を数値として受け取ります。
    引数を2で割った値を返します。

    引数: 数値
    戻り値: 引数を2で割った値
    """
    return int(x) / 2

def multipleByFour(x):
    """
    この関数は、引数を数値として受け取ります。
    引数に4をかけた値を返します。

    引数: 数値
    戻り値: 引数に4をかけた値
    """
    return int(x) * 4

n = input("Enter a number: ")
result = multipleByFour(divideByTwo(n))
print(result)
