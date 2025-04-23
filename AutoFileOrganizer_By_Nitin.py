import os
import shutil

# Get current folder path
source = os.path.dirname(os.path.abspath(__file__))
dest = os.path.join(source, "organized_files")

types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav"],
    "Code": [".py", ".java", ".cpp", ".html", ".css", ".js"],
    "Archives": [".zip", ".rar", ".7z"],
    "Others": []
}

os.makedirs(dest, exist_ok=True)

for t in types:
    os.makedirs(os.path.join(dest, t), exist_ok=True)

# Loop through files in the current directory
for f in os.listdir(source):
    p = os.path.join(source, f)
    if os.path.isfile(p) and f != os.path.basename(__file__):  # Ignore this script
        e = os.path.splitext(f)[1].lower()
        placed = False
        for cat, exts in types.items():
            if e in exts:
                shutil.move(p, os.path.join(dest, cat, f))
                print(f"📁 {f} → {cat}")
                placed = True
                break
        if not placed:
            shutil.move(p, os.path.join(dest, "Others", f))
            print(f"📁 {f} → Others")

print("\n✅ Done Organizing!")
