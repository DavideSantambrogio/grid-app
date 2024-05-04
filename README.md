# Grid App

Grid App è un'applicazione desktop che ti consente di visualizzare una griglia dinamica sullo schermo del tuo computer. Puoi scegliere il colore delle linee della griglia e la griglia si adatterà dinamicamente alla dimensione della finestra.

## Utilizzo

Nella cartella dist è già presente un file eseguibile

## Se hai problemi oppure vuoi personalizzare il codice:

### Requisiti di sistema

- Python 3.x
- Tkinter

### Installazione

1. Assicurati di avere Python 3 installato sul tuo computer.
2. Clona o scarica questo repository nella tua macchina locale.
3. Installa le dipendenze necessarie eseguendo il seguente comando:

pip install -r requirements.txt


### Utilizzo

1. Dopo aver installato le dipendenze, esegui il file grid_app.py con Python.
2. Si aprirà una finestra di dialogo che ti chiederà di selezionare il colore delle linee della griglia.
3. Scegli il colore desiderato e premi il pulsante "OK".
4. La finestra di dialogo scomparirà e verrà mostrata la griglia con il colore selezionato.

### Come creare un eseguibile

Puoi creare un eseguibile autonomo utilizzando strumenti come PyInstaller o cx_Freeze. Ecco un esempio di come creare un eseguibile con PyInstaller:

pyinstaller --onefile --noconsole grid_app.py


Questo creerà un'eseguibile che puoi eseguire senza dover installare Python o altre dipendenze.


### Problemi noti

- Su alcuni sistemi operativi, la finestra dell'applicazione potrebbe chiudersi quando si chiude la finestra del terminale. Per risolvere questo problema, considera l'utilizzo di un wrapper per l'eseguibile che gestisce correttamente il ciclo di vita dell'applicazione.

### Contributi

Se trovi dei bug o desideri apportare miglioramenti a Grid App, sentiti libero di aprire una issue o inviare una pull request.

### Licenza

Questo progetto è distribuito con licenza MIT. Per ulteriori informazioni, leggi il file LICENSE.
