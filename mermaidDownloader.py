from bs4 import BeautifulSoup as bs
import re
import requests
import os

def downloadFiles():
	pagetxt = open("page.txt", "r")
	soup = bs(pagetxt)
	
	videos = [ div.find("video").find("source")["src"] for div in soup.find_all("div", class_="embed-responsive embed-responsive-16by9")]

	materials_nonflat  = [ div.find_all("a") for div in soup.find_all("div", class_="arielMessageBody")]
	materials = [item["href"] for sublist in materials_nonflat for item in sublist]
	attacched_materials_non_flat =  [ div.find_all("a") for div in soup.find_all("div", class_="arielAttachmentBox")]
	sitoAriel=""
	if len(attacched_materials_non_flat)!=0:
    		sitoAriel = input("Inserire il link del sito ariel")
	attached_materials = [sitoAriel + re.search( '(/.+)', item["href"]).group(1) for sublist in attacched_materials_non_flat for item in sublist]
	materials = materials + attached_materials
	
	print('Sto scaricando slide e altri materiali')
	for materiale in materials:
    		r = requests.get(materiale, allow_redirects=True)
    		m = re.search('.+/(.+)', materiale).group(1)
    		with open('Result/' + m , 'wb+') as f:
		f.write(r.content)
	print("Ho finito di scaricare slide e altri materiali. Inizio a scaricare le videolezioni")

	
	for video in videos:
		print(f'Sto scaricando {video}')
		m = re.search('.+/mp4:(.+).mp4/.+', video).group(1)
		command = f'ffmpeg -i "{video}" -c copy "Result/videos/{m}.mp4"'
		if os.system(command):
			raise RuntimeError(f'program {command} failed!')
		print(f'Ho finito di scaricare {video}')

if __name__=="__main__":
	downloadFiles()
