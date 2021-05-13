# "Mermaid" Downloader

Scarica tutti materiali e le videolezioni di un corso da un certo sito didattico online di una certa università.

## Come funziona

Vai sulla pagina del corso che ti interessa, e premi Ctrl + U per visualizzare il sorgente pagina. Salvalo nel file page.txt (stessa cartella) e bon fai partire lo script python o il notebook, sono la stessa cosa.

Nel caso il sito da cui si sta scaricando ha materiali in allegato bisogna fornire l'url del sito e il cookie arielauth

Esempio di url: https://mpindarovs."mermaid".ctu.uni"me".it/v5

Capiate le virgolette

## Requirements

- Python 3
- ffmpeg
- Beautifoul soup (pip install beautifulsoup4)

Le altre librerie dovrebbero essere standard
