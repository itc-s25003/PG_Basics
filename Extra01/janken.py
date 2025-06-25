import random

def outputResult(enemyHand, playerHand, result):
    print("===============")
    print("相手: {}".format(enemyHand))
    print("自分: {}".format(playerHand))
    print("結果: {}".format(result))
    print("===============")

hands = ["グー", "チョキ", "パー"]
result = ""
isGameEnd = False

while isGameEnd == False:
    print("1: グー")
    print("2: チョキ")
    print("3: パー")

    playerInput = input("じゃんけん: ")
    playerHand = hands[int(playerInput) - 1]

    enemyHand = hands[random.randint(0, 2)]

    if playerHand == enemyHand:
        result = "あいこ"
        isGameEnd = False
        outputResult(enemyHand, playerHand, result)
    else:
        if playerHand == hands[0]:
            if enemyHand == hands[1]:
                result = "勝ち"
            elif enemyHand == hands[2]:
                result = "負け"
        elif playerHand == hands[1]:
            if enemyHand == hands[0]:
                result = "負け"
            elif enemyHand == hands[2]:
                result = "勝ち"
        elif playerHand == hands[2]:
            if enemyHand == hands[1]:
                result = "負け"
            elif enemyHand == hands[0]:
                result = "勝ち"
        isGameEnd = True
        outputResult(enemyHand, playerHand, result)


