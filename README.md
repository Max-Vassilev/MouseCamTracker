# MouseCamTracker

## Features

- **Tracks Mouse Movement**: Continuously monitors and displays the mouse coordinates ("X" and "Y").
- **On Left Click**:
  - **Saves Mouse Coordinates**: Records the current position of the mouse cursor.
  - **Captures Image**: Takes a snapshot from the connected webcam and saves the image.
- **Data Storage**: Stores mouse coordinates and image paths in an SQLite database.

## Running the Server

Since the application uses asynchronous functionality, you need to run the server with ASGI. Use Uvicorn with the following command:

```bash
uvicorn mousecamtracker.asgi:application --host 127.0.0.1 --port 8000

## Used Technologies:
**1.
