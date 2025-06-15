import os

root_dir = "pokemon_sprites"
keywords = ["Idle", "Walk", "Attack", "Hurt", "Kick", "Strike", "Rotate", "Double", "AnimData.xml"]

def should_keep(filename):
    return any(keyword.lower() in filename.lower() for keyword in keywords)

deleted_files = 0
checked_files = 0
for root, dirs, files in os.walk(root_dir):
    for file in files:
        checked_files += 1
        if not should_keep(file):
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(f"Deleted: {file_path}")
            deleted_files += 1

print(f"Done! Checked: {checked_files} files. Deleted: {deleted_files} files.")
