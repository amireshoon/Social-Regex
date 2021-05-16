import re
import json

f = open("regexes.json", "r")
regexes = json.loads(f.read())

for ir, regex in enumerate(regexes):
    print("-Testing ", regex['title'])
    totalTests = len(regex['tests'])
    failedTests = 0

    for i, test in enumerate(regex['tests']):
        print("--Test", i+1, "of", totalTests)
        r,c = regex['regex'], test['case']
        x = re.search(r, c)
        if test['want'] == True and x == None or test['want'] == False and x != None:
            failedTests = failedTests + 1
            print('--failed')
            print("--Want:", test['want'], "Got:", False if x == None else True)
        else:
            print('--pass')
    print("--Tests completed, Passed Tests:", totalTests - failedTests, ",Failed Tests:",failedTests)