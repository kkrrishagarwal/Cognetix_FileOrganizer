import os
import shutil

EXTENSION_MAP = {
    ".pdf": "PDF",
    ".jpg": "JPG",
    ".jpeg": "JPG",
    ".png": "IMAGES",
    ".txt": "TEXT",
    ".mp4": "VIDEO",
    ".xlsx": "EXCEL",
    ".csv": "CSV",
    ".py": "PYTHON"
}

def get_unique_destination(dest_folder, filename):
    base, ext = os.path.splitext(filename)
    candidate = os.path.join(dest_folder, filename)
    counter = 1
    while os.path.exists(candidate):
        candidate = os.path.join(dest_folder, f"{base}_{counter}{ext}")
        counter += 1
    return candidate

def organize_folder(folder_path):
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"❌ Error: Folder '{folder_path}' does not exist.")
        return

    print("\nOrganizing...")
    files_moved = 0
    folders_created = set()

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path) or item == os.path.basename(__file__):
            continue

        _, ext = os.path.splitext(item)
        ext_lower = ext.lower()
        folder_name = EXTENSION_MAP.get(ext_lower, ext_lower.lstrip(".").upper() or "MISC")

        target_dir = os.path.join(folder_path, folder_name)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir, exist_ok=True)
            folders_created.add(folder_name)

        dest_path = get_unique_destination(target_dir, item)
        try:
            shutil.move(item_path, dest_path)
            files_moved += 1
            print(f"  ✔ Moved: {item} --> {folder_name}/{os.path.basename(dest_path)}")
        except Exception as e:
            print(f"  ❌ Failed to move {item}: {e}")

    print("\n==========================================")
    print("✅ Files moved successfully!")
    print(f"📂 Total Files Organized : {files_moved}")
    print(f"📁 New Folders Created   : {len(folders_created)}")
    print("==========================================")

def main():
    print("==========================================")
    print("      COGNETIX FILE ORGANIZER SCRIPT      ")
    print("==========================================")
    folder_path = input("Enter folder path to organize: ").strip()
    if folder_path:
        organize_folder(folder_path)

if __name__ == "__main__":
    main()
