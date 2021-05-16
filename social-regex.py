import re
import json

f = open("regexes.json", "r")
regexes = json.loads(f.read())

for regex in regexes:
    print("Testing ", regex['title'])
    totalTests = len(regex['tests'])
    for i, test in enumerate(regex['tests']):
        print("Test", i+1, "of", totalTests)
        r,c = regex['regex'], test['case']
        x = re.search(r, c)
        if test['want'] == True:
            if x == None:
                print("failed")
                print("Want:", test['want'], "Got:", False if x == None else True)
            else:
                print("pass")
        else:
            if x != None:
                print("failed")
                print("Want:", test['want'], "Got:", False if x == None else True)
            else:
                print("pass")