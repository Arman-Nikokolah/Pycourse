
import datetime


print("python is awsome")

print(datetime.datetime.now())


stringname = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(stringname[::-1])

print(stringname[1:3])


hungray = True
if hungray:
    print("feed den")


loc = "Iranain"
if loc == "canada":
    print("false")
elif loc == "iranain":
    print("true")
else:
    print("go to hell")


mylist = {'k1': "arman", "k2": "nikookolah"}
for item in mylist.keys():
    print("_" + item)

num = 0
while num < 5:
    print(f"the {num} is ridiiii")
    num += 1
    continue

# step one
mylist = {"a": "arman"}
itemsing = {"_" + key: value for key,
            value in mylist.items()}
print(itemsing)


# step 2

mydict = {"name": "arman", "family": "nikookolah", "age": 25}
for xitem in mydict:
    print("_" + xitem)


# list comperhension

mylist = []
mystring = "hello world"
mylists = [letter for letter in mystring]
print(mylists)
mylist.append(1)


st = "Sam Name is as sam very well s"
for t in st.split():
    if t[0] == "s" or t[0] == "S":
        print(t)


def aRMAN():
    baby = "world"
    strings = "hello" + baby
    print(strings)


aRMAN()


def check(addad):
    if(addad % 2 != 0):
        return True
    elif(addad % 2 != 1):
        return False
    else:
        return "hich!"


moment = check(15)
print(moment)


def mydef(*args):
    print(args)


mydef(40, 50, 90, 60, 70, 80)


data = [2, 4, 6, 8, 10]


def date(data):
    mydata = data == 10
    print(mydata)


list(map(date, data))


lambda num: num * 22
print(num(2))
