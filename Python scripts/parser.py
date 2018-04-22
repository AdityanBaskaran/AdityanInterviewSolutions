import sys
import json
jsonfilelocation = raw_input( "provide complete path of the json file....  " )
with open(jsonfilelocation) as f:
    jsoncontent = json.load(f)
args = sys.argv[1].split('.')
try:
    for x in range(len(args)):
        jsoncontent = jsoncontent[args[x]]
    print jsoncontent
except Exception as e :
    print 'The %s Key does not exist in the input json please check ' %e
