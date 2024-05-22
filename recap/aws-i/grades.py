# For every student with a pass, print 1, for every fail print 2 for anything else, print "Invalid Value"

weird = [[{"name": "sarah"}, {"grade": "pass"}], [{"name": "abdi"}, {"grade": "fail"}], [{"name": "jack"}, {"grade": "j2hg3v1h23"}]]


for e in weird:
    grade = (e[1]["grade"])
    if grade == "pass":
        print(1)
    elif grade == "fail":
        print(0)
    else:
        print("Incorrect Value")
