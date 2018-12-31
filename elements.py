def atomic_dict():
	mydict={'H':"Hydrogen",'O':"Oxygen",'C':"Carbon",'N':"Nitrogen",'F':"Fluorine"}
	newsym=input("Enter the new Symbol: ")
	newname=input("Enter the new name: ")
	if newsym in mydict.keys():
		print("Symbol exists, new name for symbol is taken")
	else:
		print("Added new element")
	mydict[newsym]=newname
	print(mydict)
	print("Length of dictionary is: ",len(mydict))
	newsym=input("Enter symbol to search: ")
	if newsym in mydict.keys():
		print("Element found: ",mydict[newsym])
	else:
		print("No Elements found")