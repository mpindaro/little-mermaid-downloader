# Little Mermaid Downloader

Tool che scarica tutti materiali (slide e simili) e le videolezioni di un corso da un certo sito didattico online di una certa università.


![](https://thumbs-prod.si-cdn.com/YVaC3lqx4bk9jPIThb-0RJnKbbw=/800x600/filters:no_upscale()/https://public-media.si-cdn.com/filer/26/34/26349ee5-df4d-4595-8d77-674a8ef40fc0/t03pxm.jpg)
## Utilizzo

Il tool chiede in ingresso due cose:
- Il link della **sezione** del sito ariel d'interesse. Detto terra terra la pagina dove sono contenuti i materiali e/o le registrazioni-.
- Il cookie **arielauth**. Per ottenerlo basta aprire da un qualsiasi sito ariel, bisogna essersi però loggati, i developer tools. In particolare mi riferirò a Chrome ma dovrebbe essere circa lo stesso anche per gli altri browser. Da lì ```Application > Storage > Cookies > Cookies di unimi```. A questo punto dovreste trovarmi una tabella con header Name - Value - Domain - etc. Di questa tabella ci interessa, come detto prima, solo il cookie arielauthm, trovatelo, copiate il valore e datelo in pasto al tool. È importante che il cookie sia ancora caldo di forno (**dovete esservi loggati da poco**).

Ho messo sia uno script Python che un Notebook Jupyter, sono la stessa cosa, usate quello che preferite. Non richiede parametri e scaricherà tutto in una cartella ```Result```, in particolare i video saranno sotto ```Result/videos```

⚠️Se i file scaricate sono corrotti o illeggibili significa che il cookie è scaduto nel mentre e che va reinserito⚠️

## Requirements

- Python 3
- requests: ```pip install requests```
- os
- Beautifoul soup: ```pip install beautifulsoup4```
- ffmpeg: [Download](https://www.ffmpeg.org/download.html)
