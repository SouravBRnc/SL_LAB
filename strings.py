mystr=['Hello I am Someone','What is your name','How are you12','I am fine, thank you23']
for i in range(len(mystr)):
	if(i!=0 and i%2==0):
		print(mystr[i])
print("3s")
for i in range(len(mystr)):
	if(i!=0 and i%3==0):
		mystr[i]=mystr[i].upper()
print(mystr)

print("rev")
for i in range(len(mystr)):
	mystr[i]=" ".join(reversed(mystr[i].split()))
print(mystr)	

num=[]
for i in range(len(mystr)):
	for s in mystr[i]:
		if s.isdigit():
			num.append(s)
print(num)
