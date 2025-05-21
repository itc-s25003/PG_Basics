def f(x):
    """
    この関数は、受け取った引数を文字列として出力します。

    引数: 文字列
    戻り値: strに変換された引数
    """
    return str(x);

i = input("Enter a string: ")
result = f(i);
print(result);
