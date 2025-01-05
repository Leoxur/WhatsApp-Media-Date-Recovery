# WhatsApp-Media-Date-Recovery
WhatsApp Foto &amp; Video Date Recovery

Questo progetto include due script Python progettati per aggiornare i metadati e i timestamp dei file multimediali (foto e video) provenienti da WhatsApp. È particolarmente utile per ordinare i file multimediali e ripristinare le date di creazione corrette basandosi sul nome dei file. Questo si rende necessario poichè nell'effettuare il ripristino dei media di whatsapp (es. cambio smartphone), questo riporterà tutti i media con il timestamp corrispondente al momento in cui si effettua l'operazione, comportando poi che tutti i media saranno riportati in galleria senza rispettare lo storico.

---

## Funzionalità principali

- **Per le foto (`image-exif_timestamp.py`)**:
  - Funziona con i file JPEG il cui nome segue il formato `IMG-YYYYMMDD-WAXXXX.jpg`.
  - Estrae la data dal nome del file e la utilizza per aggiornare i metadati EXIF e i timestamp del file.
  - Imposta **mezzanotte** come orario predefinito per tutte le foto.
  - Per i file che non rispettano il formato, assegna come data di default il **1° gennaio 1995**.

- **Per i video (`video-timestamp.py`)**:
  - Funziona con i file video il cui nome segue il formato `VID-YYYYMMDD-WAXXXX.mp4`.
  - Estrae la data dal nome del file e aggiorna i timestamp di sistema (modifica e creazione) del file.
  - I file che non rispettano il formato vengono ignorati.

---

## Struttura delle cartelle

```plaintext
.
├── images
│   ├── image-exif_timestamp.py
│   ├── whatsapp-images-dest
│   └── whatsapp-images-source
├── README.md
└── videos
    ├── video-timestamp.py
    ├── whatsapp-video-dest
    └── whatsapp-video-source
```

### Cartelle principali
- `whatsapp-images-source`: Cartella sorgente delle immagini da elaborare.
- `whatsapp-images-dest`: Cartella di destinazione per le immagini elaborate.
- `whatsapp-video-source`: Cartella sorgente dei video da elaborare.
- `whatsapp-video-dest`: Cartella di destinazione per i video elaborati.

---

## Istruzioni

### Prerequisiti
1. **Python 3.6 o superiore**.
2. Moduli Python necessari:
   - `shutil`
   - `datetime`
   - `piexif` (per elaborare i metadati EXIF delle immagini).

   Puoi installare con:
   ```bash
   pip install shutil
   pip install datetime
   pip install piexif
   ```

---

### Per le foto

1. Copia i file JPEG ricevuti da WhatsApp nella cartella sorgente:
   ```plaintext
   whatsapp-images-source/
   ```
   Percorso tipico su Android:
   ```plaintext
   /Spazio di archiviazione/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/
   ```

2. Avvia lo script:
   ```bash
   python3 images/image-exif_timestamp.py
   ```

3. Una volta completata l'elaborazione, copia i file dalla cartella `whatsapp-images-dest/` nel percorso originale sul tuo dispositivo Android. Durante la copia, seleziona "Sostituisci file esistenti".

---

### Per i video

1. Copia i file video ricevuti da WhatsApp nella cartella sorgente:
   ```plaintext
   whatsapp-video-source/
   ```
   Percorso tipico su Android:
   ```plaintext
   /Spazio di archiviazione/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Video/
   ```

2. Avvia lo script:
   ```bash
   python3 videos/video-timestamp.py
   ```

3. Una volta completata l'elaborazione, copia i file dalla cartella `whatsapp-video-dest/` nel percorso originale sul tuo dispositivo Android. Durante la copia, seleziona "Sostituisci file esistenti".

---

## Limitazioni

- **Foto**:
  - Funziona solo con file JPEG il cui nome rispetta il formato `IMG-YYYYMMDD-WAXXXX.jpg`.
  - Non supporta altri formati di immagine (ad esempio PNG o HEIC).
  - Per i file con nomi non standard, viene impostata la data di default 01/01/1995.

- **Video**:
  - Funziona solo con file MP4 il cui nome rispetta il formato `VID-YYYYMMDD-WAXXXX.mp4`.
  - I file che non rispettano il formato vengono ignorati.

---

## Esempi Output:

   ```plaintext
File copiato: whatsapp-images-source/IMG-20180607-WA0006d.jpg -> whatsapp-images-dest/IMG-20180607-WA0006d.jpg
Metadati EXIF e timestamp di sistema aggiornati per: IMG-20180607-WA0006d.jpg
File copiato: whatsapp-images-source/adIMG-20180705-WA0011.jpg -> whatsapp-images-dest/adIMG-20180705-WA0011.jpg
Nome file non standard: adIMG-20180705-WA0011.jpg. Imposto data 1 gennaio 1995.
Metadati EXIF e timestamp di sistema aggiornati per: adIMG-20180705-WA0011.jpg
File copiato: whatsapp-images-source/IMG-20180607dasd-WA0006.jpg -> whatsapp-images-dest/IMG-20180607dasd-WA0006.jpg
Errore nell'elaborazione di IMG-20180607dasd-WA0006.jpg: Formato data non valido nel nome del file.
File copiato: whatsapp-images-source/IMG-sdfs20180607-WA0006d.jpg -> whatsapp-images-dest/IMG-sdfs20180607-WA0006d.jpg
Errore nell'elaborazione di IMG-sdfs20180607-WA0006d.jpg: Formato data non valido nel nome del file.


Nome file non valido, ignorato: VID-20230309-WA0007e.mp4
Modificato timestamp per: VID-20230309-WA0007.mp4 -> 2023-03-09
Nome file non valido, ignorato: VID-20230309-dWA0007e.mp4
Nome file non valido, ignorato: VID-20230309-dWA0007.mp4
Nome file non valido, ignorato: VID-20230309df-WA0007.mp4
Nome file non valido, ignorato: VID-sdf20230309-WA0007.mp4
Nome file non valido, ignorato: VIDfd-20230309-WA0007.mp4
Nome file non valido, ignorato: fdVID-20230309-WA0007.mp4
   ```

---

## Riconoscimenti

Questo progetto è stato creato con l'aiuto di **ChatGPT**, un'IA sviluppata da OpenAI.

---

## Licenza

Questo progetto è rilasciato sotto la [MIT License](LICENSE). Sei libero di utilizzarlo, modificarlo e distribuirlo, a patto di includere il file della licenza originale nel tuo progetto.

---

## Contatti

Per suggerimenti o segnalazioni, sentiti libero di aprire un'issue nel repository GitHub.

