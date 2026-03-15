marks1 = int(input("ENTER YOUR MARKS1:" ))
marks2 = int(input("ENTER YOUR MARKS2:" ))
marks3 = int(input("ENTER YOUR MARKS3:" ))

#total_percentage
total_percentage = (100*(marks1+marks2+marks3)/300)

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed,congratulations:",total_percentage)

else:
    print("You are fail, Try again next year:",total_percentage )