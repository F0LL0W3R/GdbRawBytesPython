import time
import subprocess

scripts = [b"\xcc"*64] # put your commands here

file = input("Input file for gdb to open: ")

proc = subprocess.Popen(["gdb",file],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
time.sleep(1)
print(proc.stdout.read1().decode("utf-8"))
proc.stdout.flush()

while(True):

    inp = input()

    if "py" in inp:
        index = int(inp[3])
        print(f"printing script #{index}: {scripts[index]}")
        proc.stdin.write(scripts[int(inp[3])]+b"\n")
    else:
        proc.stdin.write(inp.encode("utf-8")+b"\n")


    proc.stdin.flush()
    time.sleep(0.1)
    print(proc.stdout.read1().decode("utf-8"),end="")
    proc.stdout.flush()
