# Little Mermaid Downloader

Tool che scarica tutti materiali (slide e simili) e le videolezioni di un corso da un certo sito didattico online di una certa università.


![](https://thumbs-prod.si-cdn.com/YVaC3lqx4bk9jPIThb-0RJnKbbw=/800x600/filters:no_upscale()/https://public-media.si-cdn.com/filer/26/34/26349ee5-df4d-4595-8d77-674a8ef40fc0/t03pxm.jpg)
## Utilizzo

Il tool chiede in input due elementi:
- Il link della **sezione** del sito  🧜Ariel🧜 d'interesse. Detto terra terra, **la pagina dove sono contenuti i materiali e/o le registrazioni**, non del corso in generale.
- Il cookie **arielauth**. Per ottenerlo basta aprire da un qualsiasi sito 🧜Ariel🧜 i Developers Tools, **è necessario essere loggati**. In particolare mi riferirò a Chrome, ma dovrebbe essere circa lo stesso anche per gli altri browser. Da lì ```Application > Storage > Cookies > Cookies di uni*me*```. A questo punto dovreste trovarvi una tabella con header *Name - Value - Domain - etc*. Di questa tabella ci interessa, come detto prima, solo il cookie arielauth. Trovatelo, copiate il valore e datelo in pasto al tool. È importante che il cookie sia ancora caldo di forno (**dovete esservi loggati da poco**).

Ho messo sia uno script Python che un Notebook Jupyter, usate quello che preferite. **Verrà scaricato tutto in una cartella ```Result```, in particolare i video saranno sotto ```Result/videos```**

⚠️Se i file scaricati sono corrotti o illeggibili significa che il cookie è scaduto nel mentre e che va reinserito. Questo discorso vale solo per le slide⚠️

Per domande @mpindaro su telegram se invece a leggere è qualcuno dell'università sono Manuel Dileo.

Da ricordare:

- Per il download delle videolezioni è necessario avere installato FFmpeg (vedi requisiti in fondo). Potrebbe esserci bisogno di impostare la sua cartella ```/bin/``` nell'elenco del PATH (variabile di sistema): [qui](https://www.google.com/search?client=firefox-b-d&q=settare+variabile+d%27ambiente+windows) per sapere come fare.
- Non viene scaricato *l'intero sito didattico* ma le singole sezioni, definite da singoli URL. 

### Script Python

```console 
python3 downloader.py [-arielAuth] [-video] [-slide] [-username] [-password] <url>
```

```py
usage: downloader.py [-h] [-a ARIELAUTH] [-v] [-s] [-u USERNAME] [-p PASSWORD] url

positional arguments:
  url                   Link alla pagina dove sono contenuti i materiali e/o le registrazioni

optional arguments:
  -h, --help            show this help message and exit
  -a ARIELAUTH, --arielAuth ARIELAUTH
                        Il cookie arielAuth. Vedi README su come ottenerlo
  -v, --video           Scaricare solamente i video
  -s, --slide           Scaricare solamente slide/materiali
  -u USERNAME, --username USERNAME
                        Nome utente con cui fare il login
  -p PASSWORD, --password PASSWORD
                        Password con cui fare il login
```

**Sia `url` che `arielAuthCookie` vanno racchiusi tra doppi apici**
Se non si specifica nessuna opzione verranno scariati sia video che slide/materiali

#### Esempio pratico per Ariel

- Windows, comando da CMD - C:\\```python.exe downloader.py "https://<nome insegnamento>.ariel.ctu.unimi.it/<etc>" "ABCDEFGHJI432121N3JNDS11122121211"```

- Linux - pippo@LinuxOS:~$```python downloader.py "https://<nome insegnamento>.ariel.ctu.unimi.it/<etc>" "ABCDEFGHJI432121N3JNDS11122121211"```

avendo cura di recarsi nella directory dov'è presente lo script.


### Notebook
Hai totale libertà evviva! Ma ricorda... [I Don't Like Notebooks](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/edit#slide=id.g362da58057_0_1)


## Requirements

- [Python 3](https://www.python.org/)
- Requests e Beautifoul Soup installabili con ```pip install -r requirements.txt```
- ffmpeg: [Download](https://www.ffmpeg.org/download.html)


## Legal Disclaimer
*Questo programma (c.d. "script") è uno strumento sviluppato per le sole finalità d'uso concesse dal portale didattico Ariel, quindi per uso strettamente personale e di studio, senza condivisione dello stesso a persone terze. Il creatore ed i futuri collaboratori open-source declinano ogni possibile coinvolgimento legale che potrebbe implicare gli utilizzatori dello script.*

*```I contenuti di questa piattaforma sono protetti ai sensi della Legge del 22/04/1941 n. 633 (Protezione del diritto d’autore e di altri diritti connessi al suo esercizio) e successive modificazioni.
Si ricorda che L’utilizzo di tali contenuti per uso personale, di studio e di ricerca, sono consentiti nell’ambito e con i limiti stabiliti dalla normativa in tema di opere dell’ingegno. È invece tassativamente vietata qualsiasi altra utilizzazione, totale o parziale dei contenuti della presente piattaforma, ivi inclusa la riproduzione e ogni rielaborazione, diffusione, distribuzione o comunicazione al pubblico mediante qualsiasi piattaforma tecnologica, supporto o rete telematica, in assenza di previa autorizzazione scritta dell’Università degli Studi di Milano. Eventuali violazioni saranno segnalate alle Autorità competenti e i trasgressori appartenenti alla Comunità universitaria saranno passibili anche di sanzioni disciplinari.```* [Fonte](https://ariel.unimi.it/documenti/copyright)

Inoltre, ```Si ricorda che, come previsto dall’art. 2 delle “Condizioni di utilizzo e norme sulla privacy di Ariel”, espressamente accettate in occasione del primo accesso al Portale Ariel, il materiale didattico reso disponibile online deve essere utilizzato dagli Utenti esclusivamente per il proprio studio personale, senza ledere i diritti di proprietà intellettuale dei relativi autori. Nessuna riproduzione, diffusione o distribuzione, totale o parziale, di tale materiale è consentita senza preventiva autorizzazione scritta dell’Università degli Studi di Milano. Eventuali violazioni saranno segnalate alle Autorità competenti e i trasgressori appartenenti alla Comunità universitaria passibili di sanzioni disciplinari.```[Fonte](https://ariel.unimi.it/)
