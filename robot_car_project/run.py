from .controllers.camera_controller import CameraController

app=CameraController()
while True:
    try:
        app.startCamera()
    except:
        print("Error Run the app")
    