import tty, sys, termios
import os

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
key = 0
bRun = True
while bRun:
  key=sys.stdin.read(1)[0]
  print("You pressed", key)
  if key == "q":
    print("Quit")
    bRun = False
  elif key == "a":
    print("LEFT")
    os.system("python3 lt.py")
  elif key == "s":
    print("BACKWARD")
    os.system("python3 bk.py")
  elif key == "d":
    print("RIGHT")
    os.system("python3 rt.py")
  elif key == "w":
    print("FORWARD")
    os.system("python3 fd.py")

termios.tcsetattr(sys.stdin, termios.TCSADRAIN,filedescriptors)
