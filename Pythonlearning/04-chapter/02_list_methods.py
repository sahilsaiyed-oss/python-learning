fruits = ["mango","orange","banana",2,304.4]
print(fruits[0])

fruits[0] ="graphs" 
print(fruits[0])
print(fruits[1:4])

fruits.append("Sahil")
print(fruits)

#insert
fruits.insert(4,'apple')
print(fruits)

#sorting of list
l1 = [1,45,78,4,6,90,88,76.]
l1.sort()
print(l1)

#reverse
l2 = [4,2,1,5,6,7,8]
l2.reverse()
print(l2)

#pop   pop means delete a perticuler element from a list
l3 = [1,2,3,4,5,6,7,8]
l3.pop(2)
print(l3)

#remove     write an direct elemenets value not his index  
l4 = [12,13,14,15,16]
l4.remove(13)
print(l4)