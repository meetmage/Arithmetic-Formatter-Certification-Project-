def arithmetic_arranger(problems, solution):
    ans = 0

    for i in problems:
        s = i.split()
        op1 = s[0]
        sign = s[1]
        op2 = s[2]
        op1_l = len(op1)
        op2_l = len(op2)

        if len(op1) > 4:
            print("Error: Numbers cannot be more than 4 digits!")
            quit()
        elif len(op2) > 4:
            print("Error: Numbers cannot be more than 4 digits!")
            quit()
        elif len(i) > 15:
            print("Error: Too many problems!")
            quit()
        elif op1.isdigit() == False:
            print("Error: Numbers must only contain digits!")
            quit()
        elif '+' == sign:
            if op1_l > op2_l:
                bigo = op1_l
                second_line = sign + " " * (bigo - op2_l + 1) + op2
            else:
                bigo = op2_l
                second_line = sign + " " + op2
            print(op1.rjust(len(second_line)+ 1),'\n', second_line,'\n', '-' * len(second_line))

        elif '-' == sign:
            if op1_l > op2_l:
                bigo = op1_l
                second_line = sign + " " * (bigo - op2_l + 1) + op2
            else:
                bigo = op2_l
                second_line = sign + " " + op2
            print(op1.rjust(len(second_line) + 1),'\n', second_line,'\n', '-' * len(second_line))




        else:
            print("beep")
            quit()
        if solution == True and sign == '-':
            ans = int(op1) - int(op2)
            ans = str(ans)
            print(ans.rjust(len(second_line) + 1))
        elif solution == True and sign == '+':
            ans = int(op1) + int(op2)
            ans = str(ans)
            print(ans.rjust(len(second_line) + 1))
arithmetic_arranger(["4000 - 20", "30 + 4000", "30 + 4"],False)