#!/usr/bin/env python
# coding: utf-8
from bs4 import BeautifulSoup as bs
import argparse
import re
import requests
import os


def arielUrl(arg: str):
    if re.match(r'(https:\/\/.+.ariel.ctu.unimi.it/.+)', arg):
        return arg

    raise argparse.ArgumentTypeError(f"'{arg}' non è un link Ariel valido!")


def downloadFiles(askedVideos, askedFiles, link, arielauth):
    cookies = {"arielauth": f"{arielauth}"}

    r = requests.post(link, allow_redirects=True, cookies=cookies)
    soup = bs(r.text, "html.parser")

    if askedFiles:
        materials_nonflat = [div.find_all("a") for div in soup.find_all(
            "div", class_="arielMessageBody")]
        materials = [item["href"]
                     for sublist in materials_nonflat for item in sublist]

        attacched_materials_non_flat = [div.find_all(
            "a") for div in soup.find_all("div", class_="arielAttachmentBox")]
        sitoAriel = ""
        if len(attacched_materials_non_flat) != 0:
            sitoAriel = re.search(
                "(https://[\w]+.ariel.ctu.unimi.it/[\w]+)", link).group(1)
        attached_materials = [{"url": sitoAriel + re.search('(/.+)', item["href"]).group(
            1), "name":item.getText()}for sublist in attacched_materials_non_flat for item in sublist]

        for materiale in materials:
            print(f"Sto scaricando {materiale}")
            m = re.search('.+/(.+)', materiale).group(1).strip('/')
            r = requests.get(materiale, allow_redirects=True)
            os.makedirs(os.path.dirname("Result/"), exist_ok=True)
            with open('Result/' + m, 'wb+') as f:
                f.write(r.content)

        for materiale in attached_materials:
            print(f"Sto scaricando {materiale['name']}")
            r = requests.post(materiale["url"],
                              allow_redirects=True, cookies=cookies)
            os.makedirs(os.path.dirname("Result/"), exist_ok=True)
            with open('Result/' + materiale["name"], 'wb+') as f:
                f.write(r.content)
        print("Ho finito di scaricare slide e altri materiali.")

    if askedVideos:

        videos = [div.find("video").find("source")["src"] for div in soup.find_all(
            "div", class_="embed-responsive embed-responsive-16by9")]

        i = 1
        for video in videos:
            m = re.search('.+/mp4:(.+)(.mp4|.MP4)/.+',
                          video).group(1).replace("%20", " ")
            print(f'Sto scaricando {m}. Progresso: {i}/{len(videos)}')
            os.makedirs(os.path.dirname("Result/videos/"), exist_ok=True)
            command = f'ffmpeg -i "{video}" -loglevel quiet -y -c copy "Result/videos/{m}.mp4"'
            if os.system(command):
                raise RuntimeError(f'program {command} failed!')
            print(f'Ho finito di scaricare {m}')
            i = i+1
    print("Finito!")


def readInputs():
    parser = argparse.ArgumentParser()

    parser.add_argument('url', type=arielUrl,
                        help='Link alla pagina dove sono contenuti i materiali e/o le registrazioni')
    parser.add_argument('arielAuth', type=str,
                        help='Il cookie arielAuth. Vedi README su come ottenerlo')
    parser.add_argument('-v', '--video', action="store_true", default=False,
                        help='Scaricare solamente i video')
    parser.add_argument('-s', '--slide', action="store_true", default=False,
                        help='Scaricare solamente slide/materiali')

    args = parser.parse_args()

    # default
    if not args.video and not args.slide:
        downloadFiles(True, True, args.url, args.arielAuth)
    else:
        downloadFiles(args.video, args.slide, args.url, args.arielAuth)


if __name__ == "__main__":
    readInputs()
