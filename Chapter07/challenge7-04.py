correctNums = [47, 20, 39, 10, 5, 83, 72]

while True:
    userInput = input('Input: ')
    if userInput == 'q':
        break

    try:
        if int(userInput) in correctNums:
            print('正解!')
        else:
            print('不正解')
    except ValueError:
        print('数字を入力するか、qで終了します。')
