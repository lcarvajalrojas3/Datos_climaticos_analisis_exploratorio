import zipfile
import requests
import os

# Obtener la ruta del directorio donde está el script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Definir las carpetas relativas al directorio del script
temp_folder = os.path.join(script_dir, "temp")
selenium_folder = os.path.join(script_dir, "selenium")

if not os.path.exists(temp_folder):
    os.makedirs(temp_folder)
if not os.path.exists(selenium_folder):
    os.makedirs(selenium_folder)

nombre_archivo = f"{temp_folder}\chromedriver-win64.zip"

url = "https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.98/win64/chromedriver-win64.zip"

# Descargar el archivo
try:
    response = requests.get(url)
    response.raise_for_status()  # Lanza un error si la descarga falla
    
    # Guardar el archivo
    with open(nombre_archivo, "wb") as file:
        file.write(response.content)
    
    print(f"Descargado: {nombre_archivo}")

    # Descomprimir el archivo ZIP
    with zipfile.ZipFile(nombre_archivo, 'r') as zip_ref:
        zip_ref.extractall(selenium_folder)
        print(f"Archivo descomprimido")

    # Eliminar el archivo ZIP
    os.remove(nombre_archivo)
    print(f"Archivo eliminado: {nombre_archivo}")

    print(f"Descargado: {nombre_archivo}")

except requests.exceptions.RequestException as e:
    print(f"Error al descargar {url}: {e}")
except zipfile.BadZipFile:
    print(f"Error: El archivo descargado no es un archivo ZIP válido.")
except Exception as e:
    print(f"Error inesperado: {e}")