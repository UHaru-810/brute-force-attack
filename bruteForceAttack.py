import itertools

C = 0
correctPass = ""
correctPassIsalnum = False
passLength = 0
password = ""
letter = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVEWXZ"
letterList = list(letter)
status = False

correctPass = input("\nパスワードを英数字で入力してください。\n")
while True:
    correctPassIsalnum = correctPass.encode('utf-8').isalnum()
    if correctPassIsalnum == True:
        break
    correctPass = input("半角英数字で入力してください。\n")
print("\n--------------------\n")

while status == False:
    passLength += 1
    for password in itertools.product(letterList, repeat=passLength):
        C+=1
        password = ''.join(password)
        print(password, end='')
        if password == correctPass:
            status = True
            print(": Succeed! [", C, "]", sep='')
            print("\n--------------------\n")
            print("パスワードは", password, "です。\n")  
            break
        else:
            print(": Failed [", C, "]", sep='')