from textblob import TextBlob
print("Welcome to the AI sentement analyzer")
name=input("Whats your name?")
print("Its nice to meet you",name)
while True:
    feelings=input("How are you feeling today")
    if feelings.lower()=="exit":
        break
    obj=TextBlob(feelings)
    polarity=obj.sentiment.polarity
    if polarity>0.25:
        print("Thats great!")
        good=input("What made you feel like that?")
    elif polarity<-0.25:
        print("Thats ok, we all have bad days. I am here for you")
        sad=input("Oh no. What happened?")
        sadans=input("How can I help?")
    else:
        print("We all have neutral days")
        print("Maybe spending time with your family can help cheer you up")
print("Goodbye",name)
