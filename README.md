# Destructive farm Guide

## Client side
La parte client di destructive farm si occupa eseguire gli exploit e ottenere le flag che poi la parte server manderà

### Configurazione
La configurazione del client si esegue direttamente da linea di comando con dei paramentri e non ha un file di configurazione dedicato.
Qui mostro i parametri disponibili:
```
Usage: start_sploit.py exploit_file -u SERVER_IP -a ATTACK_NAME_OR_SERVICE_NAME --token TOKEN (Il token solo se si ha attivato il login delle api)
```

### Exploit
L'unica particolarità sull exploit è na necessità di avere lo shebang `#!/usr/bin/env python3` all'inizio del file e che nel momento dove ottiene la flag deve stamparla in questo modo:
``` python
print(flag, flush=True)
```
Se manca il flush=True il server non riceverà la flag.
Per Comodità conviene che in tutto l'exploit si usi il flush=True.


## Server side
La parte server di destructive farm si occupa delle flag submission.
Si trova tutta nella cartella `server`.

### Flag submission
Nel file `config.py` bisogna decommentare e configurare il tipo di protocollo per la submission delle flag.
I protocolli supportati sono dentro la cartella `protocols`, nel caso nella cartella non ci sia il protocollo corretto per la gara il file deve essere scritto da voi o dato direttamente dal creatore della gara (nel caso di protocolli custom).
Inoltre va anche configurato il `FLAG_FORMAT` che è il formato delle flag che verranno inviate al server.

### Teams
Sempre nel file `config.py` bisogna configurare i team che partecipano alla gara.
La gestione è un dict formato da "team_name": "team_ip".
Di default viene generato con un ciclo for, ma è possibile modificarlo a piacimento.

### Server password
Nel file `config.py` bisogna configurare la password del server, che verrà usata per autenticare l'accesso alla web gui

### API
Il server espone una API di default non autenticata, è la api che server ai client per collegarsi al server.

### Tempistiche
Nel file `config.py` bisogna configurare le tempistiche della gara, in particolare `SUBMIT_FLAG_LIMIT`, `SUBMIT_PERIOD` e `FLAG_LIFETIME` (secondi)
- `SUBMIT_FLAG_LIMIT` -> quante flag possono essere inviate in un ciclo di gara
- `SUBMIT_PERIOD` -> quanto dura un ciclo di gara
- `FLAG_LIFETIME` -> quanto tempo ha una flag prima di scadere (solitamente 1 o più cicli di gara)
