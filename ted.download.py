import urllib.request
from bs4 import BeautifulSoup

fout = open('data.json', 'w')

d = dict()

for i in range(1, 1001):
    try:
        print(i)
        opener = urllib.request.FancyURLopener({})
        url = 'http://www.ted.com/talks/{}'.format(i)
        f = opener.open(url)
        content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        desc = soup.findAll(attrs={"property":"video:tag"})

        d[i] = [desc[j]['content'] for j in range(len(desc))]
    except:
        d[i] = []

fout.write(str(d))
fout.close()
