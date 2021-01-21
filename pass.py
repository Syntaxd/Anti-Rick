import random

color = ['red', 'orange', 'yellow', 'gold', 'green', 'lime', 'cyan', 'blue', 'magenta', 'purple', 'violet', 'silver', 'gray', 'white', 'black']
animals = ['fox', 'bear', 'cat', 'dog', 'bird', 'pig', 'fish', 'monkey', 'spider', 'bat']
describer = ['lover', 'Man', 'Kindly', 'Funny']
numb = range(1, 10)
numb2 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

with open("pass.txt", "w") as f:
    for c in color:
        for N in numb:
            for n in numb2:
                print(c + str(N) + '0' + str(n) + "\n")
                f.write(c + str(N) + '0' + str(n) + "\n")
    for a in animals:
        for d in describer:
            for n in numb:
                f.write(a + d + str(n) + '0' + "\n")
                print(a + d + str(n) + '0' + "\n")
    for c in color:
        for a in animals:
            for n in numb:
                print(c + a + str(n) + '0' + "\n")
                f.write(c + a + str(n) + '0' + "\n")