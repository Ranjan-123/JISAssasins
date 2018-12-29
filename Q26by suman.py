bs=int(input("Enter the basic salary"))
if bs>=5000:
    hra=bs*(50/100)
    da=bs*(150/100)
    gs=bs+hra+da
    print("hra is\n",hra,"\n da is\n",da,"/n the gross salary is \n",gs)
else:
    hra=bs*(10/100)
    da=bs*(110/100)
    gs=bs+hra+da
    
    
    print("hra is \n",hra,"da is \n",da,"gross salary is \n",gs)
