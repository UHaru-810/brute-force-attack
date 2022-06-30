import itertools
import zipfile
import subprocess
import os

#zipの展開
def unZip(P):
    #以下の2行は必要に応じて変更してください
    zipFile = "secret.zip"
    unZipFolder = "./unZip/"
    with zipfile.ZipFile(zipFile, "r") as zp:
        try:
            zp.extractall(path=unZipFolder, pwd=P.encode())
            return True
        except:
            return False

def main():
    C = 0
    passLength = 0
    passLengthIsalnum = False
    password = ""
    letter = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVEWXZ"
    letterList = list(letter) #リストにし、1文字ずつに区切る
    status = False
    openFolder = ""

    #パスワードの桁数処理
    passLength = input("\nパスワードの桁数を半角数字で入力してください。\n")
    while passLength.isdigit() == False:
        passLength = input("半角数字で入力してください。\n")
    passLength = int(passLength)
    print("\n--------------------\n")

    #パスワードの桁数分のパターンを実行
    for password in itertools.product(letterList, repeat=passLength):
        C+=1
        password = ''.join(password) #パスワードを連結
        status = unZip(password)
        print(password, end='')
        if status == True:
            print(": Succeed! [", C, "]", sep='')
            print("\n--------------------\n")
            print("zipファイルのパスワードは", password, "です。")
            openFolder = input("展開したフォルダを表示しますか？ (Y/N)\n")
            while openFolder != "Y" and openFolder != "N":
                openFolder = input("Y または N のどちらかを入力してください。\n")
            if openFolder == "Y":
                print("展開したフォルダを開いています...\n")
                if os.name == "nt":
                    subprocess.Popen(["explorer", "unZip"], shell=True)
                if os.name == "posix":
                    subprocess.Popen(["open", "unZip"])
            else:
                print("プログラムを終了します。\n")
            break
        else:
            print(": Failed [", C, "]", sep='')

main()
