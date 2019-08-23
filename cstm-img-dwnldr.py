import urllib.request as url
import bs4

x = input('Enter the type of images that you want to download:')
x = x.split()
y = '-'.join(x)
print(y)
res = url.urlopen(f'https://giphy.com/search/{y}')
page = bs4.BeautifulSoup(res)
images = page.find_all('img')
for i in range(len(images)):
    path = images[i]['src']
    url.urlretrieve(path,'img_{}.gif'.format(i))
