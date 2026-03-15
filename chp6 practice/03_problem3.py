a = input("Enter your comment:" )


p1 = ("Make a lot of money")
p2 = ("buy now")
p3 = ("subscribe this")
p4 = ("click this")

if((p1 in a) or (p2 in a) or(p3 in a) or (p4 in a)):
    print("This is a spam comment")

else:
    print("Your comment is not spam")