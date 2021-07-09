# Little Mermaid Downloader

Tool che scarica tutti materiali (slide e simili) e le videolezioni di un corso da un certo sito didattico online di una certa università.


![](https://thumbs-prod.si-cdn.com/YVaC3lqx4bk9jPIThb-0RJnKbbw=/800x600/filters:no_upscale()/https://public-media.si-cdn.com/filer/26/34/26349ee5-df4d-4595-8d77-674a8ef40fc0/t03pxm.jpg)
## Utilizzo

Il tool chiede in input due elementi:
- Il link della **sezione** del sito  🧜Ariel🧜 d'interesse. Detto terra terra, **la pagina dove sono contenuti i materiali e/o le registrazioni**, non del corso in generale.
- Il cookie **arielauth**. Per ottenerlo basta aprire da un qualsiasi sito 🧜Ariel🧜 i Developers Tools, **è necessario essere loggati**. In particolare mi riferirò a Chrome, ma dovrebbe essere circa lo stesso anche per gli altri browser. Da lì ```Application > Storage > Cookies > Cookies di uni*me*```. A questo punto dovreste trovarvi una tabella con header Name - Value - Domain - etc. Di questa tabella ci interessa, come detto prima, solo il cookie arielauth. Trovatelo, copiate il valore e datelo in pasto al tool. È importante che il cookie sia ancora caldo di forno (**dovete esservi loggati da poco**).

Ho messo sia uno script Python che un Notebook Jupyter, usate quello che preferite. Verrà scaricato tutto in una cartella ```Result```, in particolare i video saranno sotto ```Result/videos```

⚠️Se i file scaricati sono corrotti o illeggibili significa che il cookie è scaduto nel mentre e che va reinserito. Questo discorso vale per le slide, i video non ne hanno bisogno⚠️

Per domande mpindaro su telegram se invece a leggere è qualcuno dell'università sono Manuel Dileo.

### Script Python
```python3 downloader.py [-video] [-slide] url cookie```

Parametri obbligatori (spiegati sopra):
- ```url``` 
- ```cookie```

**Entrambi devono essere racchiusi tra doppi apici**

Parametri opzionali:
- ```-video``` per scaricare solo i video
- ```-slide``` per scaricare solo slide e materiali

Se assenti verrà scaricato tutto. 

### Notebook
Hai totale libertà evviva! Ma ricorda... [I Don't Like Notebooks](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/edit#slide=id.g362da58057_0_1)


## Requirements

- Python 3
- Requests e Beautifoul Soup installabili con ```pip install -r requirements.txt```
- ffmpeg: [Download](https://www.ffmpeg.org/download.html)

