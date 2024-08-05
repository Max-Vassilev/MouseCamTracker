# MouseCamTracker

## Features

- **Tracks Mouse Movement**: Continuously monitors and displays the mouse coordinates ("X" and "Y"):
<img width="250" alt="image" src="https://github.com/user-attachments/assets/a0ccf2ff-18a0-4bc0-8ebd-9c346d115f3a">

- **On Left Click**:
  - **Saves Mouse Coordinates**: Records the current position of the mouse cursor.
 <img width="400" alt="image" src="https://github.com/user-attachments/assets/33dd7e6f-76e9-4ba6-951e-08e1807e5079">

  - **Captures Image**: Takes a snapshot from the connected webcam and saves the image.
- **Data Storage**: Stores mouse coordinates and image paths in an SQLite database.

## How to Setup and Run the Project on Windows

### 1. Clone the repository

```bash
git clone https://github.com/Max-Vassilev/MouseCamTracker.git
cd MouseCamTracker
```
### 2. Create and activate a virtual environment
```bash
python -m venv .venv
```
Then activate the virtual environment:
```bash
.venv\Scripts\activate
```
If you encounter a script execution policy error, you can bypass it with the following command:
```bash
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```
### 3. Enter the Django project
```bash
cd mousecamtracker
```
### 4. Install the required packages
```bash
pip install -r requirements.txt
```

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Run the server
Since the application uses asynchronous functionality, you need to run the server with ASGI. Use Uvicorn with the following command:
```bash
uvicorn mousecamtracker.asgi:application --host 127.0.0.1 --port 8000
```

## Used Technologies:
1. asyncio (via Django Channels for real-time asynchronous features)
2. Webserver (with Uvicorn for USGI)
3. WebSockets
4. 
5.
6. SQLite
