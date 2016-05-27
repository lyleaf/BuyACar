import requests
from lxml import html

r = requests.get('https://www.leboncoin.fr/voitures/offres/provence_alpes_cote_d_azur/?th=1&location=Nice%2006000%2CNice%2006200%2CAntibes%2006600')

#https://www.leboncoin.fr/voitures/offres/provence_alpes_cote_d_azur/?o=2&location=Nice+06000%2CNice+06200%2CAntibes+06600

r.status_code

r.text

tree = html.fromstring(r.content)
#XPath or CSSelect

for i in xrange(1,36):
    bigImage = tree.xpath('//*[@id="listingAds"]/section/ul/li[1]/a/div/span[%d]/span/img' % i)
    price = tree.xpath('//*[@id="listingAds"]/section/ul/li[%d]/a/section/h3/text()' % i)[0]
    hyperlink = tree.xpath('//*[@id="listingAds"]/section/ul/li[%d]/a' % i)
    link = hyperlink[0].attrib['href']
    title = hyperlink[0].attrib['title']
    price = int(price.encode("utf8","ignore")[0:-5].replace(" ",""))
    if (price < 5000):
        print price
        print title 
        print link

#Rewrite this application to use threads for improved speed.

