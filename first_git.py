one = {'value1' : {'vineeth':001, 'yeshas':002},'value2' : 2}
two = {'value1' : ['vin1',{'vineeth':002}, 'yeshas'],'value2' : 33}
three = {'value1' : 22,'value2' : 33}
four = {'value1' : 22,'value2' : 33}
five = {'value1' : 22,'value2' : 33}
l1 = [one]

l1.append(two)
l1.append(three)
l1.append(four)
l1.append(five)

for a in l1 :
	print a['value1']

#for each of the elements in l1, print the values of the key 'value1'
