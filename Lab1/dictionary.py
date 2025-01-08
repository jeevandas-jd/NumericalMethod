
"""def printDictionary(d):
    print(f"This is {d["name"]} and he is a {d["occupation"]}")"""
human1={"name":"jeevandas","occupation":"software engineer","age":20}
human2={"name":"JD","occupation":"pilot","age":28}
human2["name"]="nidal"
ls=[human1,human2]
for i in ls:
    print(i)


    i["salary"]=input(f"enter salary of {i["name"]}")

    print(i["name"])
    print(i)

human2.popitem()

print(human2)