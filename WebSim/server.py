from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO
from PIL import Image
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def serve_html():
    return send_from_directory('.', 'index.html')

# API to move the car
@app.route('/move', methods=['POST'])
def move():
    data = request.json
    direction = data.get('direction')
    if direction in ["forward", "left", "right"]:
        socketio.emit('move_command', {'direction': direction})  # Send command to the client
        return {"status": "ok", "direction": direction}
    return {"status": "error", "message": "Invalid direction"}, 400

# API to request a screenshot from the client
@app.route('/screenshot', methods=['GET'])
def screenshot():
    print("Emitting capture_screenshot event")  # Debugging
    socketio.emit('capture_screenshot')  # Trigger screenshot capture
    return {"status": "ok", "message": "Screenshot requested"}

@app.route('/upload_screenshot', methods=['POST'])
def upload_screenshot():
    print("📸 Received screenshot upload request.")  # Debugging

    if 'screenshot' in request.files:
        screenshot = request.files['screenshot']
        save_path = os.path.join(os.getcwd(), "camera_view.png")  # Save in current directory
        screenshot.save(save_path)
        
        # Check if the file exists after saving
        if os.path.exists(save_path):
            print(f"✅ Screenshot successfully saved at: {save_path}")
            return {"status": "ok", "message": f"Screenshot saved at {save_path}"}
        else:
            print("❌ Error: File was not saved correctly!")
            return {"status": "error", "message": "File not found after saving"}, 500

    print("❌ Error: No file received!")
    return {"status": "error", "message": "No file received"}, 400


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
