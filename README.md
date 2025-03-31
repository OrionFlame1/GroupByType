# GroupByType, file auto-sorter based on file type

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A background service that monitors your Downloads folder and automatically organizes files based on their extension.

## Key Features
- Real-time monitoring of file changes (creation/modification)
- Automatic file sorting (via `filesort()` from helpers)
- Background operations
- Detailed console logging with timestamps

## How It Works
1. Watches your **Downloads folder** using `watchdog.Observer`
2. Triggers `filesort()` on these events:
   - New file created (`on_created`)
   - Existing file modified (`on_modified`)
3. Runs as a background service threaded file observer
4. Logs all activity to console with timestamps

## Roadmap
- [ ] Add UI
- [ ] Add file type filtering (only sort specific extensions)
- [ ] Implement custom sorting rules configuration
- [ ] Create installable package (PyPI/.exe)
- [ ] Support multiple watched folders
- [ ] Build proper error handling for file conflicts
- [ ] Add support for a group of file extension for moving to one folder

## Quick Start
```bash
pip install watchdog infi.systray
python main.py
```

## Dependencies
- watchdog - File monitoring
- infi.systray - System tray integration
