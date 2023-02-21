import sys
memory = {}
instructions = []
instcount = 0

f = open(sys.argv[1], "r")
instructions = f.readlines()
f.close()

retaddr = 0

def setMemAddr(addr, value):
    memory[int(addr)] = value
while True:
    try:
        inst = instructions[instcount].strip()
    except:
        sys.exit()
    if inst.split(" ")[0] == "set":
        if inst.split(" ")[2].isnumeric():
            setMemAddr(inst.split(" ")[1], int(inst.split(" ")[2]))
        else:
            setMemAddr(inst.split(" ")[1], inst.split(" ", 2)[2])
    elif inst.split(" ")[0] == "add":
        setMemAddr(inst.split(" ")[1], memory[int(inst.split(" ")[2])] + memory[int(inst.split(" ")[3])])
    elif inst.split(" ")[0] == "sub":
        setMemAddr(inst.split(" ")[1], memory[int(inst.split(" ")[2])] - memory[int(inst.split(" ")[3])])
    elif inst.split(" ")[0] == "mul":
        setMemAddr(inst.split(" ")[1], memory[int(inst.split(" ")[2])] * memory[int(inst.split(" ")[3])])
    elif inst.split(" ")[0] == "div":
        setMemAddr(inst.split(" ")[1], memory[int(inst.split(" ")[2])] / memory[int(inst.split(" ")[3])])
    elif inst.split(" ")[0] == "import":
        setMemAddr(inst.split(" ")[1], __import__(inst.split(" ")[2]))
    elif inst.split(" ")[0] == "dis":
        try:
            display = memory[int(inst.split(" ")[1])]
        except:
            display = ""
        print(display)
    elif inst == "":
        pass
    elif inst.split(" ")[0] == "jmp":
        counter = 0
        while True:
            line = instructions[counter].strip()
            if line == inst.split(" ", 1)[1]:
                instcount = counter
                break
            counter += 1
    elif inst.split(" ")[0] == "call":
        counter = 0
        retaddr = instcount
        while True:
            line = instructions[counter].strip()
            if line == inst.split(" ", 1)[1]:
                instcount = counter
                break
            counter += 1
    elif inst.split(" ")[0] == "callpy":
        memory[int(inst.split(" ")[3])] = getattr(memory[int(inst.split(" ")[1])], inst.split(" ")[2])()
    elif inst == "ret":
        instcount = retaddr
    elif inst.startswith("<") and inst.endswith(">"):
        pass
    elif inst.startswith(";"):
        pass
    else:
        print("Unknown instruction")
        print(inst)
        sys.exit()
    instcount += 1