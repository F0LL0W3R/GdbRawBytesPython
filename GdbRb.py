
import time
import subprocess

scripts = [b"\xcc"*64,b"\x44"*64] # put your commands here

file = input("Input file for gdb to open: ")

proc = subprocess.Popen(["gdb",file],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
time.sleep(1)
print(proc.stdout.read1().decode("utf-8"))
proc.stdout.flush()

while(True):

    inp = input()
    if inp == "quit":

        break

    elif "python -c" in inp: #you can also run scripts from the shell
        pycmd = subprocess.Popen(inp,stdout=subprocess.PIPE)
        time.sleep(2)
        response = pycmd.stdout.read1()
        print(response.decode("utf-8"))
        print(f"Printing result: {response}")
        proc.stdin.write(response+b"\n")

    elif "python -s" in inp: #to load the output from your .py script

        pycmd = subprocess.Popen(inp.replace("-s","") ,stdout=subprocess.PIPE)
        time.sleep(2)
        response = pycmd.stdout.read1()
        print(response.decode("utf-8"))
        proc.stdin.write(response+b"\n")

    elif "pyc" in inp:

        try:
            index = int(inp[4])
        except:
            print("Usage: pyc [index]")
            continue

        try:
            script = scripts[index]
        except:
            print("Script not found")
            continue
        print(f"Printing command #{index}: {scripts[index]}")
        proc.stdin.write(scripts[index]+b"\n")






    else:
        proc.stdin.write(inp.encode("utf-8")+b"\n")


    proc.stdin.flush()
    time.sleep(0.5)
    print(proc.stdout.read1().decode("utf-8"),end="")
    proc.stdout.flush()
