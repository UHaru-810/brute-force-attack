import itertools

C = 0
correctPass = ""
password = ""
letter = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVEWXZ"
letterList = list(letter)

#入力したパスワードの処理
correctPass = input("\nパスワードを英数字で入力してください。\n")
while correctPass.encode('utf-8').isalnum() == False:
    correctPass = input("半角英数字で入力してください。\n")
print("\n--------------------\n")

#パスワードの桁数分パターンを作成
for password in itertools.product(letterList, repeat=len(correctPass)):
    C+=1
    password = ''.join(password)
    print(password, end='')
    if password == correctPass:
        print(": Succeed! [", C, "]", sep='')
        print("\n--------------------\n")
        print("パスワードは", password, "です。\n")  
        break
    else:
        print(": Failed [", C, "]", sep='')


