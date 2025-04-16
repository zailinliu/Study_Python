inF = None
instr = ""
print(type( inF ))
print(type( instr ))

inF = open("./python2/temp/data1.txt","r",encoding="utf-8")
instr = inF.readlines()
print(instr)
inF.close()

with open("./python2/temp/data1.txt","r",encoding="utf-8") as inF:
    instr = inF.read()
    print(instr)