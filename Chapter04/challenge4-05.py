def strToFloat(x):
    """
    この関数は、受け取った文字列をfloat型に変換して返します。

    引数: 文字列
    戻り値: 引数をfloat型に変換した値
    """
    return float(x)

i = input("Enter a number: ")

try:
    print(strToFloat(i))
except(ValueError):
    print("平沢 唯「Invalid input」")
