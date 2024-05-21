from flask import Flask, Response, render_template
import cv2
import requests
class ShareCameraController:
    def startServer():
        app = Flask(__name__)
        video_stream = None

        @app.route('/')
        def index():
            return render_template('index.html')

        def generate_frames():
            global video_stream
            while True:
                success, frame = video_stream.read()
                if not success:
                    break
                else:
                    ret, buffer = cv2.imencode('.jpg', frame)
                    frame = buffer.tobytes()
                    yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


        @app.route('/video_feed')
        def video_feed():
            return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
        app.run(debug=True)
    def sendFrame(frame):
        server_url = "http://localhost:5000/video_feed"
        _, img_encoded = cv2.imencode('.jpg', frame)
        response = requests.post(server_url, data=img_encoded.tostring(), headers={'Content-Type': 'application/octet-stream'})



