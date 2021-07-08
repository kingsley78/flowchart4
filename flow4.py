#flowchart 4
name = input("please enter name")
if name == "alice":
    print("hi alice")
else:
    age = int(input("enter age"))
    if age < 12:
        print("you are not alice, kiddo")
    elif age > 200:
        print("unlike you alice is not an undead, immortal vampire")
    elif age >100:
        print("you are not alice, grannie!")