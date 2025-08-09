with open("input.txt","w") as file:
    file.write("Line1 \n")
    file.write("Line2 \n")
    file.write("Line3 \n")
    file.write("Line4 \n")
    file.write("Line5 \n")

with open("input.txt","r") as file:
    rd = file.read()
    print(rd)

with open("input.txt","r") as file:
    rd = file.read()
    st= rd.split()
    print(len(st))
with open("input.txt","r") as file:
    ru = file.read()
    n=ru.upper()

with open('output.txt', 'w') as file:
    file.write(n)