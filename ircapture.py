from irmagician import IrMagician

# irMagicianに接続 --- (*1)
mag = IrMagician("/dev/ttyACM0")

# キャプチャを実行 --- (*2)
while True:
    print("> 赤外線リモコンのボタンを押してください")
    print("...")
    r = mag.ir_capture()
    if r.find("Time Out") > 0 or r == "":
        print("失敗(ToT)")
        continue
    print("ok")
    break
mag.close()

