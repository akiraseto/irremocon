from irmagician import IrMagician
import sys

# 保存ファイル名を得る --- (*1)
if (len(sys.argv) != 2):
    print("no filename")
    quit()
loadfile = sys.argv[1]

# irMagicianのメモリデータを書き換え再生
mag = IrMagician()
mag.set_debug(True)
mag.ir_load(loadfile)
mag.ir_play()
mag.close()


