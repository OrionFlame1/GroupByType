import time
import threading
from datetime import datetime
from infi.systray import SysTrayIcon
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from helpers import filesort, get_download_path

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'created':
            print(f"[{datetime.now()}] New file created: {event.src_path}")
            filesort()
    def on_modified(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'modified':
            print(f"[{datetime.now()}] File modified: {event.src_path}")
            filesort()


def on_quit_callback(systray):
    observer.stop()
    observer.join()
    systray.shutdown()

def start_observer():
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    folder_to_watch = str(get_download_path())
    event_handler = MyHandler()

    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=False)

    menu_options = ()

    systray = SysTrayIcon("icon.ico", "File Watcher", menu_options, on_quit=on_quit_callback)

    print(f"Watching '{folder_to_watch}' for new files...")

    observer_thread = threading.Thread(target=start_observer)

    try:
        observer_thread.start()
        systray.start()
    except KeyboardInterrupt:
        observer_thread.join()
        systray.shutdown()

