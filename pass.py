color = ['red', 'orange', 'yellow', 'gold', 'green', 'lime', 'cyan', 'blue', 'magenta', 'purple', 'violet', 'silver', 'gray', 'white', 'black']
numb = range(1, 10)
numb2 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
with open("pass.txt", "w") as f:
    for c in color:
        for N in numb:
            for n in numb2:
                print(c + str(N) + '0' + str(n) + "\n")
                f.write(c + str(N) + '0' + str(n) + "\n")
