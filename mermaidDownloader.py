#!/usr/bin/env python
# coding: utf-8
from bs4 import BeautifulSoup as bs
import re
import requests
import os


def downloadFiles():
	link = input("Inserisci link della sezione del sito ariel da cui vuoi scaricare video e slide")

	arielauth = input("Inserisci il tuo cookie arielauth. Se non sai come recuperarlo leggi sul readme. Assicurati di aver fatto l'accesso di recente")
	cookies = {"arielauth": f"{arielauth}"}


	r = requests.post(link, allow_redirects=True, cookies=cookies)
	soup = bs(r.text)


	videos = [ div.find("video").find("source")["src"] for div in soup.find_all("div", class_="embed-responsive embed-responsive-16by9")]



	materials_nonflat  = [ div.find_all("a") for div in soup.find_all("div", class_="arielMessageBody")]
	materials = [item["href"] for sublist in materials_nonflat for item in sublist]



	attacched_materials_non_flat =  [ div.find_all("a") for div in soup.find_all("div", class_="arielAttachmentBox")]
	sitoAriel=""
	if len(attacched_materials_non_flat)!=0:
	    sitoAriel = re.search("(https://[\w]+.ariel.ctu.unimi.it/[\w]+)", link).group(1)
	attached_materials = [{"url":sitoAriel + re.search( '(/.+)', item["href"]).group(1), "name":item.getText() }for sublist in attacched_materials_non_flat for item in sublist]


	for materiale in materials:
	    print(f"Sto scaricando {materiale}")
	    m = re.search('.+/(.+)', materiale).group(1).strip('/')
	    r = requests.get(materiale, allow_redirects=True)
	    os.makedirs(os.path.dirname("Result/"), exist_ok=True)
	    with open('Result/' + m , 'wb+') as f:
	       f.write(r.content)


	for materiale in attached_materials:
	    print(f"Sto scaricando {materiale['name']}")
	    r = requests.post(materiale["url"], allow_redirects=True, cookies=cookies)
	    os.makedirs(os.path.dirname("Result/"), exist_ok=True)
	    with open('Result/' + materiale["name"] , 'wb+') as f:
		f.write(r.content)
	print("Ho finito di scaricare slide e altri materiali.")


	i=1
	for video in videos:
	    m = re.search('.+/mp4:(.+)(.mp4|.MP4)/.+', video).group(1).replace("%20", " ")
	    print(f'Sto scaricando {m}. Progresso: {i}/{len(videos)}')
	    os.makedirs(os.path.dirname("Result/videos/"), exist_ok=True)
	    command = f'ffmpeg -i "{video}" -y -c copy "Result/videos/{m}.mp4"'
	    if os.system(command):
		raise RuntimeError(f'program {command} failed!')
	    print(f'Ho finito di scaricare {m}')
        i++
	print("Finito!")

if __name__=="__main__":
	downloadFiles()

