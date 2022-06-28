import random
random.randint(100, 999)
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




print("Hit & Blow Game")
digit = input("遊びたい桁数を入力して下さい: ")
ans = generator(int(digit))
cont = True
count = 0
print("Game Start!")
while cont:
    count += 1
    command = input("{}桁の数字を入力してください > ".format(digit))
    your_ans = [int(command[i]) for i in range(len(command))]
    [hit, blow] = hitblow(your_ans, ans)
    print("{}: {} Hit, {} Blow".format(command, hit, blow))
    if hit == len(ans):
        print("おめでとうございます!正解です!!! You took {} steps.".format(count))
        cont = False