import random
import json
import string


#lon = (lo = load) + (n = file n.json ||| n.json = names.json)
#fon = (fo = file + open) + (n = names)
def lon():
    global names
    fon = open("n.json")
    names = json.load(fon)


#lod = (lo = load) + (d = file d.json ||| d.json = domains.json)
#fod = (fo = file + open) + (d = domains)
def lod():
    global domains
    fod = open("d.json")
    domains = json.load(fod)


# (values and dom are lists that are made to put into random.choice)
#the for loop uses the list in d.json for the (i in domains) and the dom.append(i[0]) takes the 1st item from every list in the domains
def getdomain():
    values = []
    dom = []
    lod()
    for i in domains:
        dom.append(i[0])
        values.append(float(i[1]))
    domain = ("@" + str(random.choices(dom, values, k=1)[0]))
    return domain


#makes a let of 3 rancdom charters using lowercase letters, upercase letters and 0-9
#the chars+=i makes a string of the 3 random letters
def ranchar():
    chars = ""
    letnum = string.ascii_letters + string.digits
    for i in range(3):
        i = random.choice(list(letnum))
        chars+=i
    return chars


#writes to a file called output.txt and makes the file if it is not there
#it writes an list to the file so it could work with json (probably)
def write(input):
    with open("output.txt", "w") as f:
        f.write("\n".join(input))



#main function that runs everything
#throws the email together
def main():
    global email
    femail = []
    lon()
    lod()
    for i in names:
        email = (ranchar() + i + ranchar() + getdomain())
        femail.append(email)
    write(femail)
main()