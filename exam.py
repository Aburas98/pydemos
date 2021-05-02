w = eval(input("Please enter the weight of the commodity."))
p = 0
if w <= 50:
	p = w*0.5
else:
	p = w*0.6
print(p)