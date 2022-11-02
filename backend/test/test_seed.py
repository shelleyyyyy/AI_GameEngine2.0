from gameEngine.seed_generator import generateWhiteNoise
def run_test_seed():
    noise = generateWhiteNoise(25, 25, 'ab10')
    num_blank = 0
    num_blocked = 0
    for i in noise:
        print()
        for o in i:
            if(o == 0):
                num_blank = num_blank + 1
                print('-',end='')
            else:
                num_blocked = num_blocked + 1
                print('#',end='')
    print()
    print("blank", num_blank)
    print("blocked", num_blocked)