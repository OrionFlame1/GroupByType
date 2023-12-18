import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from helpers import filesort


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'created':
            print(f"New file created: {event.src_path}")
            filesort()


def start_watcher(folder_to_watch):
    event_handler = MyHandler()

    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=False)

    print(f"Watching '{folder_to_watch}' for new files...")

    try:
        observer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
