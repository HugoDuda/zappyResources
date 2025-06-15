import os
import requests
import zipfile

zip_dir = "sprites_zips"
extract_dir = "pokemon_sprites"
os.makedirs(zip_dir, exist_ok=True)
os.makedirs(extract_dir, exist_ok=True)

for i in range(1, 901):
    sprite_id = f"{i:04d}"
    url = f"https://spriteserver.pmdcollab.org/resources/{sprite_id}/sprites.zip"
    zip_path = os.path.join(zip_dir, f"sprites_{sprite_id}.zip")
    extract_path = os.path.join(extract_dir, sprite_id)

    print(f"Downloading {url} ...")
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            with open(zip_path, "wb") as f:
                f.write(r.content)
            print(f"Saved as {zip_path}")
            os.makedirs(extract_path, exist_ok=True)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            print(f"Extracted to {extract_path}")
            os.remove(zip_path)
            print(f"Deleted {zip_path}")

        else:
            print(f"ID {sprite_id} not found (status {r.status_code})")
    except Exception as e:
        print(f"Error with ID {sprite_id}: {e}")

print("Download, extraction, and cleanup finished.")
