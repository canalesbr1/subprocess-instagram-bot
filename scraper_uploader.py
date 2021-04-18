import bs4, requests, json
from random import shuffle

#Main website URL
main_url = 'https://www.tumblr.com/search/'

#Get Artist URL
artist = "Tom Wesselmann"
myurl = main_url + '+'.join(artist.split(" "))
print(f"Requesting {myurl} to find images from {artist}...")

#Request & get image links
r = requests.get(myurl)
soup = bs4.BeautifulSoup(r.text,"html.parser")
img_links = [img.get("srcset") for img in soup.find_all("img")]
print(f"Found {len(img_links)} images in the first tumblr page for {artist}...")

#Shuffle images
shuffle(img_links)

#Go through images in order and select one that is appropriate size / make sure we dont have that link yet
for link in img_links:
	big = link.split(', ')[-1]
	size = int((big.split(' ')[1][:-1]))
	if size > 1080:
		mylink = big.split(' ')[0]
		save = True
		with open('data.txt','r') as infile:
			data = json.load(infile)
		if my link not in [image['link'] for image in data['images']]:
			print('Found image link larger than 1080px in width that has not been posted...')
			break
		
print(f'Downloading {mylink}')

with open('data.txt','r') as infile:
	data = json.load(infile)
	lastnum = data['images'][-1]['post']

#Download image
r = requests.get(mylink)
file = open('tmp/image.jpg','wb')
file.write(r.content)
file.close()

#Log information to JSON file
data = {}
data['images'] = []
data['images'].append({
	'artist': artist,
	'link': mylink,
	'post': lastnum + 1
	})

with open('data.txt','w') as outfile:
	json.dump(data,outfile)

#Upload image




