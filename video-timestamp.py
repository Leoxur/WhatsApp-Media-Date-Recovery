import os
import re
import shutil
from datetime import datetime

# Percorsi delle cartelle
source_folder = "whatsapp-video-source"
dest_folder = "whatsapp-video-dest"

# Assicurarsi che la cartella di destinazione esista
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

# Regex per il formato del nome file WhatsApp
filename_pattern = re.compile(r"^VID-(\d{4})(\d{2})(\d{2})-WA\d{4}\.mp4$")

for filename in os.listdir(source_folder):
    source_path = os.path.join(source_folder, filename)

    # Verifica se il file corrisponde al naming convention
    match = filename_pattern.match(filename)
    if match:
        year, month, day = match.groups()
        
        # Estrai la data dal nome del file
        file_date = datetime(int(year), int(month), int(day))

        # Copia il file nella cartella di destinazione
        dest_path = os.path.join(dest_folder, filename)
        shutil.copy2(source_path, dest_path)

        # Modifica il timestamp del file nella cartella di destinazione
        mod_time = file_date.timestamp()
        os.utime(dest_path, (mod_time, mod_time))

        print(f"Modificato timestamp per: {filename} -> {file_date.strftime('%Y-%m-%d')}")
    else:
        print(f"Nome file non valido, ignorato: {filename}")

print("Operazione completata.")

