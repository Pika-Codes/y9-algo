fo = open("yeet.txt", "w")
fo.write("Rohin\n")
fo.write("Mark\n")
fo.write("Moyaad\n")
fo.write("Xan\n")
fo.write("Banq\n")
fo.write("Amar\n")
fo.write("Jeff\n")
fo.write("Will\n")
fo.write("Krishnin\n")
fo.write("JohnL\n")
fo.close()

fa = open("yeet.txt", "a")
fa.write("Fisher")
fa.close()

fr = open("yeet.txt", "r")
frr = fr.readlines()
print(frr)
fr.close()

fi = open("yeet.txt", "r")
flist = fi.readlines()
fi.close()

print(flist)

Friend = "Will"

for find in flist:
    clean = find.strip()
    print(clean)
    if (clean == Friend):
        print("Look! It's " + Friend)
