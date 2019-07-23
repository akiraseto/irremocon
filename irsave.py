from irmagician import IrMagician
import sys

# 保存ファイル名を得る --- (*1)
if (len(sys.argv) != 2):
    print("no filename")
    quit()
savefile = sys.argv[1]

# irMagicianのメモリデータを読み取り、JSON形式で保存
mag = IrMagician()
mag.set_debug(True)
mag.ir_save(savefile)
mag.close()


