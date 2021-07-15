#!/usr/bin/env python
# coding: utf-8
from ntpath import join
from bs4 import BeautifulSoup as bs
import argparse
import re
import requests
import os
import urllib.parse

from requests.api import patch


def arielUrl(arg: str):
    if re.match(r'(https:\/\/.+.ariel.ctu.unimi.it/.+)', arg):
        return arg

    raise argparse.ArgumentTypeError(f"'{arg}' non è un link Ariel valido!")


def downloadFiles(askedVideos, askedFiles, link, arielauth):
    cookies = {"arielauth": f"{arielauth}"}

    r = requests.post(link, allow_redirects=True, cookies=cookies)
    soup = bs(r.text, "html.parser")

    baseName = os.path.join(
        'output',
        soup.select_one('.navbar-brand a span').getText().strip(),
        soup.select_one('#forum-header h1.arielTitle').getText().strip()
    )

    if askedFiles:
        # aggiungere qualche tipo di check se sono file o pagine web
        materials = [
            {
                'url': element['href'],
                'name': os.path.join(baseName, element['href'].split('/')[-1])
            }
            for element in soup.select('.arielMessageBody a')]

        materials.extend([
            {
                'url': urllib.parse.urljoin(link, element['href']),
                'name': os.path.join(baseName, element.getText())
            }
            for element in soup.select('.arielAttachmentBox a')
        ])

        for item in materials:
            print(f'Sto scaricando {item["name"]}')
            os.makedirs(
                os.path.dirname(item['name']), exist_ok=True
            )

            with open(item['name'], 'wb+') as f:
                f.write(
                    requests.get(item['url'], allow_redirects=True).content
                )

        print('Ho finito di scaricare slide e altri materiali.')

    if askedVideos:
        baseName = os.path.join(baseName, 'videos')

        videoList = [
            {
                'url': element['src'],
                'name': os.path.join(
                    baseName,
                    re.search(r'mp4:(.*)/', element['src'], re.IGNORECASE)[1]
                )
            }
            for element in soup.select('.lecturecVideo source')
        ]

        for i, video in enumerate(videoList, start=1):
            print(
                f'Sto scaricando {video["name"]}. \n' +
                f'Progresso: {i}/{len(videoList)}'
            )
            os.makedirs(os.path.dirname(video['name']), exist_ok=True)

            command = f'ffmpeg -i "{video["url"]}" -loglevel quiet -y -c copy "{video["name"]}"'
            if os.system(command):
                raise RuntimeError(f'program {command} failed!')

            print('Dowload completato! \n')

    print('Finito!')


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
