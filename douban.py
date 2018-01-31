import requests
import re
import os

def getImagePath():
	urls = []
	
	target = 'https://www.douban.com/'
	headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
	req = requests.get(url=target)
	html = req.text
	for url in re.findall(r'https:[^ ]*?(?:jpg|png|gif)',html):
		urls.append(url)
	return urls

def getImage(urls,path):
	if not os.path.exists(path):
		os.mkdir(path)
	
	for url in urls:
		match=re.search(r'[^/]*?.(?:jpg|png|gif)',url)
		if match:
			filename = match.group()
			print('filename=%s\n'%filename)
			#print('正在下载'+url)
			req = requests.get(url = url)
			content = req.content
			open(path+filename,'wb').write(content)
		else:
			print('get pic name error url=%s' % url)
			open('log.txt','a').write('get pic name error url=%s \n' % url)

		
		
if __name__ == '__main__':
	path = './image.baidu/'
	urls = getImagePath()
	getImage(urls,path)