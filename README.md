# MouseCamTracker

## Features

- **Tracks Mouse Movement**: Continuously monitors and displays the mouse coordinates ("X" and "Y"):
  <img width="250" alt="image" src="https://github.com/user-attachments/assets/a0ccf2ff-18a0-4bc0-8ebd-9c346d115f3a">

- **On Left Click**:
  - **Saves Mouse Coordinates**: Records the current position of the mouse cursor and creates instance for it in the database.
  - **Captures Image**: Takes a snapshot from the connected webcam and saves the image.
   
- **Data Storage**: Stores mouse coordinates and image paths in an SQLite database.
  <img width="700" alt="image" src="https://github.com/user-attachments/assets/d263e8c1-daa3-4d51-878d-d95f0ff9837c">

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
While running the server with Uvicorn is necessary for asynchronous tasks, you might encounter issues with the Django admin panel's frontend appearance. If you experience such issues, you can run the server using Django’s development server as a temporary workaround:
```bash
python manage.py runserver
```
However, please note that running the server this way will not support asynchronous tasks. This method should only be used for administrative purposes.


## Used Technologies
1. asyncio (via Django Channels for real-time asynchronous features)
2. Webserver (with Uvicorn for ASGI)
3. WebSockets (mouse_tracking and mouse_click)
5. OpenCV - image/media processing
6. SQLite

## Note:
Images are not stored in the database but are saved in a media folder, which is not uploaded to GitHub. The project is configured so that when an image is captured after a left click, it is stored in the media folder. The database only records the image path along with the X and Y coordinates.
