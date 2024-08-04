# MouseCamTracker

## Features

- **Tracks Mouse Movement**: Continuously monitors and displays the mouse coordinates ("X" and "Y").
- **On Left Click**:
  - **Saves Mouse Coordinates**: Records the current position of the mouse cursor.
  - **Captures Image**: Takes a snapshot from the connected webcam and saves the image.
- **Data Storage**: Stores mouse coordinates and image paths in an SQLite database.

## Setup and Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/Max-Vassilev/MouseCamTracker.git
cd MouseCamTracker
```
### 2. Create and activate a virtual environment
```bash
python -m venv .venv
```
## On Windows
If you encounter a script execution policy error, you can bypass it with the following command:
```bash
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```
Then activate the virtual environment:
```bash
.venv\Scripts\activate
```

### 3. Install the required packages
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Run the server
Since the application uses asynchronous functionality, you need to run the server with ASGI. Use Uvicorn with the following command:
```bash
uvicorn mousecamtracker.asgi:application --host 127.0.0.1 --port 8000
```


## Used Technologies:
1. asyncio (via Django Channels)
2. Webserver (with Uvicorn)
3. WebSockets
4. 
5.
6. SQLite
