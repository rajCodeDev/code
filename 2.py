Email=input("Enter your Email:")#g@g.in , rajgaming@gmail.com
k,j,d=0,0,0
if len(Email)>=6:
    if Email[0]. isalpha():
        if ("@" in Email) and (Email.count("@")==1):
            if (Email[-4]==".") ^ (Email[-3]=="."):
                for i in Email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:  
                    print('WRONG EMAIL 5')  
                else:
                    print('RIGHT EMAIL')     
            else:
                print('WRONG EMAIL 4')
        else:
            print('WRONG EMAIL 3')
    else:
        print('WRONG EMAIL 2')
else:
    print('WRONG EMAIL 1')        