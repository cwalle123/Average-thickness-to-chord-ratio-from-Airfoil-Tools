import matplotlib.pyplot as plt

with open(r'NACA64-212.txt',"r") as fin:
    xtab = []
    ytab = []
    header = fin.readline()
    for line in fin:
        line = line.strip()
        if line != " ":
            coordinates = line.split('=')
            x = coordinates[0]
            y = coordinates[1]
            xtab.append(float(x))
            ytab.append(float(y))
    ttab = []
    for i in range(len(ytab)):
        t = abs(float(ytab[i])) # thickness calculated as the y coordinate, so its a "half" thickness
        ttab.append(t) 
    tavg = sum(ttab)/(len(ytab)/2)
    print(tavg)
    
    plt.plot(xtab,ytab)
    plt.axis([0,1,-0.5,0.5])
    plt.show()