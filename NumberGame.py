import random
import numpy as np

from scipy import rand
##answer = random.randint(100, 999)
def generator(length):
    ans = []
    while len(ans) < length:
        rand = random.randint(0, 9)
        if rand in ans:
            pass
        else:
            ans += [rand]
    return ans






def hitblow(command, ans):
    hit = 0
    blow = 0
    for i in range(len(command)):
        if command[i] == ans[i]:
            hit += 1
        else:
            if command[i] in ans:
                blow += 1
    return [hit, blow]


print("[Hit & Blow Game] \n")
print("指定された桁数の数字において．数当てゲームを行います")
print("各桁ごとに 桁も数値も当てられれば「Hit, 桁が異なり数値だけが当てられれば「Blow」と表示されます ")
print("間違えるたびに1つずつヒントが与えられます 6回以内に当てられないとGame Over!")
print("できるだけ少ない試行回数で当てられるよう頑張りましょう!!! \n")

digit = input("遊びたい桁数を入力して下さい: ")
ans = generator(int(digit))
cont = True
count = 0
print("Game Start!")
while cont:
    count += 1
    command = input("{}桁の数字を入力してください > ".format(digit))
    answer = [int(ans[i]) for i in range(len(ans))]
    your_ans = [int(command[i]) for i in range(len(command))]
    [hit, blow] = hitblow(your_ans, ans)
    print("{}: {} Hit, {} Blow".format(command, hit, blow))
    answer = int("".join([str(j) for j in (ans)]))


    if hit == len(ans):
        print("おめでとうございます!正解です!!! 正解までに {} 回試行しました.".format(count))
        cont = False
    
    if hit != len(ans):
        if count < 6:
            if your_ans > ans:
                print("ヒント:もっと小さな数です!")
            if your_ans < ans:
                print("ヒント:もっと大きな数です！")

        if count == 2:
            if answer %2 == 0:
                print("ヒント:答えは偶数です")
            if answer %2 != 0:
                print("ヒント:答えは奇数です")
        if count == 3:
            if answer %3 == 0:
                print("ヒント:答えは3の倍数です")
            if answer %3 != 0:
                print("ヒント:答えは3の倍数ではありません")
        
        if count == 4:
            if answer %7 == 0:
                print("ヒント:答えは7の倍数です")
            if answer %7 != 0:
                print("ヒント:答えは7の倍数ではありません")

        if count == 5:
            if answer %11 == 0:
                print("大ヒント:答えは11の倍数です")
            if answer %13 == 0:
                print("大ヒント:答えは13の倍数です")
            if answer %17 == 0:
                print("大ヒント:答えは17の倍数です")
            if answer %19 == 0:
                print("大ヒント:答えは19の倍数です")
            if answer %23 == 0:
                print("大ヒント:答えは23の倍数です")
            if answer %29 == 0:
                print("大ヒント:答えは29の倍数です")  
            if answer %31 == 0:
                print("大ヒント:答えは31の倍数です")  
            if answer %37 == 0:
                print("大ヒント:答えは37の倍数です")
            if answer %41 == 0:
                print("大ヒント:答えは41の倍数です")
            if answer %43 == 0:
                print("大ヒント:答えは43の倍数です")
            if answer %47 == 0:
                print("大ヒント:答えは47の倍数です")
            else:
                print("もうヒントはありません")      
             



        if count == 6:
            print("Game Over!!!!!HAHAHA!!!!!!!")
            print("正解は%dです!" %(answer) )
            break
        

