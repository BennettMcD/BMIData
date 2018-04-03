import math

class BMIAnalysis():
  
  def __init__(self):
    
    fin = open("body.dat", "r")
    file = fin.read()
    file = file.split("\n")[:-1]

    plist = []

    for l in file:
  
      xfile = l.split("\n")
      xfile = xfile[0].split(" ")
  
      nanfile = []
      fullfile = []
      
      for n in xfile:
    
        n = float(n)
        nanfile.append(n)
    
      for a in nanfile:
    
        if math.isnan(a) == True:
  
          pass
    
        else:
      
          fullfile.append(a)
    
      plist.append(fullfile)
  
    for num in range(0, len(plist)):
      curlist = plist[num]
      plist[num].append(self.BMI(num, curlist))
  
    for num in range(0, len(plist)):
      prelist = plist[num]
      plist[num].append(self.newBMI(num, prelist))
  
    
    lintest = linreg(plist, 21, 24)
    newlintest = linreg(plist, 22, 25)
    
    print(lintest.intercept())
    print( "Correlation = " + str(lintest.corr()))
    print(newlintest.intercept())
    print( "Correlation = " + str(newlintest.corr()))
      
  def BMI(self, person, pdata):
    self.data = pdata
    return ((self.data[22]/((self.data[23]) / 100) **2))
    
  def newBMI(self, person, pdata):
    self.data = pdata
    return (-110 + (1.34 * (self.data[4])) + (1.54 * (self.data[3])) + (1.20 * (self.data[2])) + (1.11 * (self.data[20])) + (1.15 * (self.data[19])) + (0.177 * (self.data[23])))


class linreg:
  
  def __init__(self, plist, x, y):
    
    self.ndata = plist
    self.sumx = self.calcsumx(x)
    self.sumy = self.calcsumy(y)
    self.sumxy = self.calcsumxy(x, y)
    self.sumxsq = self.calcsumxsq(x)
    self.sumysq = self.calcsumysq(y)
    self.N = len(plist)
    
  
  def calcsumx(self, x):
    
    xtotal = 0
    for l in self.ndata:
      xtotal += l[x]
    return xtotal
    
  def calcsumy(self, y):
    
    ytotal = 0
    for l in self.ndata:
      ytotal += l[y]
    return ytotal
      
  def calcsumxy(self, x, y):
    
    xytotal = 0
    for l in self.ndata:
      xytotal += l[x] * l[y]
    return xytotal
    
  def calcsumxsq(self, x):
    
    xsqtotal = 0
    for l in self.ndata:
      xsqtotal += (l[x] ** 2)
    return xsqtotal
    
  def calcsumysq(self, y):
    
    ysqtotal = 0
    for l in self.ndata:
      ysqtotal += (l[y] ** 2)
    return ysqtotal


  def slope(self):
    
    return ((self.N * self.sumxy) - (self.sumx * self.sumy)) / ((self.N * self.sumxsq) - ((self.sumx) ** 2))
    
  def intercept(self):
    
    self.aslope = self.slope()
    
    print("Slope = " + str(self.aslope))
    
    hnum = (self.aslope) * (self.sumx)
    num8r = self.sumx - hnum
    return num8r / self.N
    
  def corr(self): 
    
    num8r = (self.N * self.sumxy) - (self.sumx * self.sumy)
    print(num8r)
    
    d8r = ((self.N*self.sumxsq - (self.sumx)**2) * (self.N*self.sumysq - (self.sumy)**2))**0.5
    
    print(d8r)
    return num8r / d8r
    
Test = BMIAnalysis()
