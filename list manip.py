# for loop in python
mangoes=("book")
for i in mangoes:
    print (i)
    print("Done")
# for loops with lists
words=["1","DID","A"]
for word in words:
    print(word + "!")
str = "hello guys,welcome back to my youtube channel"
count = 0
for x in str:
    if(x=="o"):
        count+=1
        print("the number of o's is:",count)
for x in str:
    if(x=="l"):
        continue
    else:
        print(x)


