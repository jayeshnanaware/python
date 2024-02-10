Title:- To calculate the  net salery by using all profestional terms include in it
# code...
basicSalery=int(input("enter your salery: "))
hra=basicSalery*0.1                  #hra=house rent allowence
ta=basicSalery*0.05                # ta=travel allowence
grossSalery=basicSalery+hra+ta
pt=grossSalery*0.02                # pt=provisional tax
netSalery=grossSalery-0.02
print("your net salery: ",netSalery)
print("your house rent allowses",hra)
print("your gross salery: ",grossSalery)
print("provisional tax: ",pt)



