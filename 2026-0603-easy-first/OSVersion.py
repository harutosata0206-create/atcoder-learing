X,Y = input().split()

if(X == "Lynx"):
    print("Yes")
elif(X == "Serval" and Y != "Lynx" ):
    print("Yes")
elif(X == "Ocelot" and Y =="Ocelot"):
    print("Yes")
else:
    print("No")