import tty, sys, termios

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
  elif key == "s":
    print("BACKWARD")
  elif key == "d":
    print("RIGHT")
  elif key == "w":
    print("FORWARD")

termios.tcsetattr(sys.stdin, termios.TCSADRAIN,filedescriptors)
