"""Name: Zackery Vering
    Project: Python2 lab2c
    Date: 4 Sept 2018"""
print "==================================="
print "Item price: $19.99"
print "Sales tax: 7%"
priceA = 19.99
taxA = 7
taxA = taxA * 0.01
totalA = priceA * (1+taxA)
print "Total with sales tax: {}".format(totalA)

print "Item price: $24.87"
print "Sales tax: 9%"
priceB = 24.87
taxB = 9
taxB = taxB * 0.01
totalB = priceB * (1+taxB)
print "Total with sales tax: {}".format(totalB)

print "Item price: $109.44"
print "Sales tax: 10%"
priceC = 109.44
taxC = 10
taxC = taxC * 0.01
totalC = priceC * (1+taxC)
print "Total with sales tax: {}".format(totalC)

print "Item price: $9.27"
print "Sales tax: 5%"
priceD = 9.27
taxD = 5
taxD = taxD * 0.01
totalD = priceD * (1+taxD)
print "Total with sales tax: {}".format(totalD)
print "==================================="
