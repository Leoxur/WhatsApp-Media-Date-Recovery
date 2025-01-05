from datetime import datetime
import os
import shutil
import piexif

def modify_exif_and_file_date(file_path):
    """
    Modifica i metadati EXIF e la data di creazione del file in base al nome del file.
    """
    file_name = os.path.basename(file_path)
    try:
        # Verifica se il nome del file rispetta il formato "IMG-YYYYMMDD-WAxxxx.jpg"
        if file_name.startswith("IMG-") and len(file_name) >= 15:
            try:
                date_str = file_name.split('-')[1]  # Estrai 'YYYYMMDD'
                date_obj = datetime.strptime(date_str, "%Y%m%d")
            except ValueError:
                raise Exception("Formato data non valido nel nome del file.")
        else:
            # Se il formato non è valido, assegna la data 1 gennaio 1995
            date_obj = datetime(1995, 1, 1)
            print(f"Nome file non standard: {file_name}. Imposto data 1 gennaio 1995.")

        # Formatta la data per EXIF (formato richiesto: "YYYY:MM:DD HH:MM:SS")
        exif_date = date_obj.strftime("%Y:%m:%d %H:%M:%S")
        
        # Aggiorna i metadati EXIF
        try:
            exif_dict = piexif.load(file_path)
        except Exception:  # Se fallisce il caricamento dei metadati EXIF
            exif_dict = {"Exif": {}}

        # Aggiungi o aggiorna i campi EXIF rilevanti
        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = exif_date.encode('utf-8')
        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = exif_date.encode('utf-8')
        exif_dict['0th'][piexif.ImageIFD.DateTime] = exif_date.encode('utf-8')
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, file_path)

        # Aggiorna i timestamp del file di sistema (File Modification Date/Time)
        timestamp = date_obj.timestamp()
        os.utime(file_path, (timestamp, timestamp))  # Access time e Modification time

        print(f"Metadati EXIF e timestamp di sistema aggiornati per: {file_name}")
    
    except Exception as e:
        print(f"Errore nell'elaborazione di {file_name}: {e}")

def process_directory(source_directory, destination_directory):
    """
    Copia i file JPEG dalla sorgente alla destinazione e aggiorna i metadati EXIF e i timestamp nella destinazione.
    """
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)  # Crea la cartella di destinazione se non esiste

    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
                source_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(destination_directory, file)

                # Copia il file dalla sorgente alla destinazione
                shutil.copy2(source_file_path, dest_file_path)
                print(f"File copiato: {source_file_path} -> {dest_file_path}")

                # Modifica i metadati EXIF e la data del file copiato
                modify_exif_and_file_date(dest_file_path)

# Percorsi delle directory
source_directory = "whatsapp-images-source"  # Cartella sorgente
destination_directory = "whatsapp-images-dest"  # Cartella destinazione

# Processa i file
process_directory(source_directory, destination_directory)

