import os
import shutil


def filesort():
    path = str(get_download_path())
    out_path = path

    unique_types = []
    excluded_types = ['tmp', 'crdownload']

    for filename in os.listdir(path):  # iterating files and folder in downloads folder
        f = os.path.join(path, filename)  # concatenate path with filename
        if os.path.isfile(f):  # check if current iteration is a file
            ext = str(filename.split(".")[-1])
            if ext in excluded_types:
                continue

            if ext not in unique_types:  # check if filetype of current iteration is already found
                unique_types.append(ext)  # adding unique filetype to create folder
            new_folder = os.path.join(out_path, str(filename.split(".")[-1]))

            if not os.path.exists(new_folder):  # check if folder for extension exists already
                os.makedirs(new_folder)  # create new folder using extension name
            dest_path = os.path.join(new_folder, str(filename))

            if not os.path.exists(dest_path):
                print(f"Moving {f} to {dest_path}")
                shutil.move(f, dest_path)


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')
