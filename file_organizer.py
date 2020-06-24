import os
import shutil


# Load all extension
audio = [".mp3", ".wma", ".aac", ".wav", ".mp4a"]
video = [".mp4", ".m4a", ".m4v", ".f4v", ".f4a", ".m4b", ".m4r", ".f4b", ".mov", ".avi", ".mkv", ".3gp"]
document = [".doc", ".docx", ".pdf", ".ppt", ".pptx", ".csv"]
software = [".exe", ".apk"]
zips = [".zip", ".rar"]


# Check files directory
path = "C:\\Users\\Md. Rubel Rana\\Downloads"
files = os.listdir(path)

# Create new folder
os.mkdir(path + "\\" + "Audio")
os.mkdir(path + "\\" + "Video")
os.mkdir(path + "\\" + "Documents")
os.mkdir(path + "\\" + "Software")
os.mkdir(path + "\\" + "Compressed")
os.mkdir(path + "\\" + "Unknown")

for file in files:
    extension = os.path.splitext(file)[1]
    if extension == "":
        files_1 = os.listdir(path + "\\" + file)
        for file_1 in files_1:
            ext = os.path.splitext(file_1)[1]
            new_path = path + "\\" + file + "\\"

            if ext in audio:
                shutil.move(new_path + file_1, path + "\\" + "Audio")
            elif ext in video:
                shutil.move(new_path + file_1, path + "\\" + "Video")
            elif ext in document:
                shutil.move(new_path + file_1, path + "\\" + "Documents")
            elif ext in software:
                shutil.move(new_path + file_1, path + "\\" + "Software")
            elif ext in zips:
                shutil.move(new_path + file_1, path + "\\" + "Compressed")
            else:
                shutil.move(new_path + file_1, path + "\\" + "Unknown")

    elif extension in audio:
        shutil.move(path + "\\" + file, path + "\\" + "Audio")
    elif extension in video:
        shutil.move(path + "\\" + file, path + "\\" + "Video")
    elif extension in document:
        shutil.move(path + "\\" + file, path + "\\" + "Documents")
    elif extension in software:
        shutil.move(path + "\\" + file, path + "\\" + "Software")
    elif extension in zips:
        shutil.move(path + "\\" + file, path + "\\" + "Compressed")
    else:
        shutil.move(path + "\\" + file, path + "\\" + "Unknown")