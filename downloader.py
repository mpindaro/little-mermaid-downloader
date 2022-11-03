#!/usr/bin/env python
# coding: utf-8
import argparse
import re
import os
from sys import stderr
from traceback import print_exc

import requests
from bs4 import BeautifulSoup as bs


def login(username, password):
    resp = requests.post(
            "https://elearning.unimi.it/authentication/skin/portaleariel/login.aspx?url=https://ariel.unimi.it/",
            data={
                "hdnSilent": "true",
                "tbLogin": username,
                "tbPassword": password,
                "ddlType": ""
            }
    )
    if len(resp.history) == 0:
        raise Exception("Username o password non corretti")
    return resp.cookies.get("arielauth")


def arielUrl(arg: str):
    if re.match(r'(https:\/\/.+.ariel.ctu.unimi.it/.+)', arg):
        return arg

    raise argparse.ArgumentTypeError(f"'{arg}' non è un link Ariel valido!")


def downloadFiles(askedVideos, askedFiles, link, arielauth, quiet):
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
            1), "name":item.getText().replace('/','-').replace('\\','-')}for sublist in attacched_materials_non_flat for item in sublist]

        for materiale in materials:
            try:
                print(f"Sto scaricando {materiale}")
                m = re.search('.+/(.+)', materiale).group(1).strip('/')
                r = requests.get(materiale, allow_redirects=True)
                os.makedirs(os.path.dirname("Result/"), exist_ok=True)
                with open('Result/' + m, 'wb+') as f:
                    f.write(r.content)
            except Exception:
                if not quiet:
                    print_exc()

        for materiale in attached_materials:
            try:
                print(f"Sto scaricando {materiale['name']}")
                r = requests.post(materiale["url"],
                                  allow_redirects=True, cookies=cookies)
                os.makedirs(os.path.dirname("Result/"), exist_ok=True)
                with open('Result/' + materiale["name"], 'wb+') as f:
                    f.write(r.content)
            except Exception:
                if not quiet:
                    print_exc()
        print("Ho finito di scaricare slide e altri materiali.")

    if askedVideos:

        videos = [div.find("video").find("source")["src"] for div in soup.find_all(
            "div", class_="embed-responsive embed-responsive-16by9")]

        i = 1
        for video in videos:
            m = re.search('.+/mp4:(.+)(.mp4|.MP4|m4v)/.+',
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
    parser.add_argument('-a', '--arielAuth', type=str,
                        help='Il cookie arielAuth. Vedi README su come ottenerlo')
    parser.add_argument('-v', '--video', action="store_true", default=False,
                        help='Scaricare solamente i video')
    parser.add_argument('-s', '--slide', action="store_true", default=False,
                        help='Scaricare solamente slide/materiali')
    parser.add_argument('-u', '--username', type=str,
                        help='Nome utente con cui fare il login')
    parser.add_argument('-p', '--password', type=str,
                        help='Password con cui fare il login')
    parser.add_argument('-q', '--quiet', action="store_true", default=False,
                        help='Nasconde i messaggi di errore')

    args = parser.parse_args()

    if (not args.username or not args.password) and not args.arielAuth:
        raise argparse.ArgumentError(None, "Passare username e password oppure il cookie usando arielAuth")
    if args.username and args.password:
        args.arielAuth = login(args.username, args.password)

    # default
    if not args.video and not args.slide:
        downloadFiles(True, True, args.url, args.arielAuth, args.quiet)
    else:
        downloadFiles(args.video, args.slide, args.url, args.arielAuth, args.quiet)


if __name__ == "__main__":
    readInputs()
