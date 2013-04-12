__author__ = 'Zilvinas Kucinskas'

import httplib

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

url = open('myfile', 'r').read()

index = find_nth(url, '/', 3)
main_url = url[0:index]
print "MAIN URL: " + main_url
params = url[index:len(url)] + '&user-select=TWO'
print "PARAMS: " + params

h = httplib.HTTPConnection(main_url)
h.request('GET', params)
r = h.getresponse()

rh = r.getheaders()
print 'Header:'
for i in rh:
    print i[0], ':', i[1]
print '\n'

rr = r.read()
print 'Content:'
print rr
print '\n'

h.close()