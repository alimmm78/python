#python 3

m=1
while m==1:
    a1=input('birinci yazili notunuz')
    a2=input('ikinci yazili notunuz')
    a3=input('3. yazili')
    if bool(a1) == True:
        if bool(a2)==True:
            if bool(a3)==True:
                print((int(a1)+int(a2)+int(a3))/3)
            else:
                print((int(a1)+int(a2))/2)
        else:
            print(int(a1))
    else:
        print('yazili olmadin mi??')
    print('\n')
