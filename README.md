# MouseCamTracker

## Features

- **Tracks Mouse Movement**: Continuously monitors the mouse coordinates.

- **On Left Click**:
  - **Saves Mouse Coordinates**: Records the current position of the mouse cursor.
  - **Captures Image**: Takes a snapshot from the connected webcam and saves the image.

- **Data Storage**: Stores mouse coordinates and image paths in an SQLite database.

- **Web Interface**: Displays real-time mouse data and captured images in a browser.

- **Parallel Processing**: Utilizes multiprocessing to handle mouse tracking and image capture simultaneously.
