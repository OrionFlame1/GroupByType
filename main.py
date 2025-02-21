from helpers import get_download_path
from watcher import start_watcher

if __name__ == "__main__":
    start_watcher(str(get_download_path()))
