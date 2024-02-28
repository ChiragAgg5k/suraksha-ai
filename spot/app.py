from ast import List
from collections import defaultdict
import datetime
import math
from flask import Flask, redirect, render_template, Response, request, session, url_for
import cv2
from scipy.__config__ import show
from ultralytics import YOLO
from spot.firebase.config import auth, db

# object classes
classNames = [
    "person",
    "bicycle",
    "car",
    "motorbike",
    "aeroplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
    "umbrella",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "sofa",
    "pottedplant",
    "bed",
    "diningtable",
    "toilet",
    "tvmonitor",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush",
]

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = "secret"
app.app_context().push()

# model
model = YOLO("yolov8n.pt")


def get_cameras() -> list:
    cameras = []
    index = 0
    while True:
        camera = cv2.VideoCapture(index)
        if not camera.isOpened():
            break
        cameras.append(index)
        camera.release()
        index += 1
    return cameras


def send_analytics(data: dict, userId: str) -> None:
    if len(data) == 0:
        return

    if userId is None or userId == "":
        return

    try:
        doc = db.child("analytics").child(userId).push(data)
        print(doc)
    except Exception as e:
        print(e)


def gen_frames(user_id):
    camera = cv2.VideoCapture(0)
    next_time = datetime.datetime.now()
    delta = datetime.timedelta(seconds=30)
    objectData = {}  # person -> {freq, maxConfidence, minConfidence}

    while True:
        period = datetime.datetime.now()

        success, frame = camera.read()
        frame = cv2.flip(frame, 1)
        results = model(frame, stream=True, verbose=False)

        objectsFreq = defaultdict(List)

        # coordinates
        for r in results:
            boxes = r.boxes

            for box in boxes:
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = (
                    int(x1),
                    int(y1),
                    int(x2),
                    int(y2),
                )  # convert to int values

                # put box in cam
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # confidence
                confidence = math.ceil((box.conf[0] * 100)) / 100

                if confidence < 0.5:
                    continue

                # class name
                cls = int(box.cls[0])
                cls_name = classNames[cls]

                if cls_name in objectsFreq:
                    objectsFreq[cls_name].append(confidence)
                else:
                    objectsFreq[cls_name] = [confidence]

                # object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2

                cv2.putText(
                    frame,
                    f"{classNames[cls]} {confidence * 100:.1f}%",
                    org,
                    font,
                    fontScale,
                    color,
                    thickness,
                )

            for obj in objectsFreq:
                if obj in objectData:
                    objectData[obj]["freq"] = max(
                        objectData[obj]["freq"], len(objectsFreq[obj])
                    )
                    objectData[obj]["maxConfidence"] = max(
                        objectData[obj]["maxConfidence"], max(objectsFreq[obj])
                    )
                    objectData[obj]["minConfidence"] = min(
                        objectData[obj]["minConfidence"], min(objectsFreq[obj])
                    )

                else:
                    objectData[obj] = {
                        "freq": len(objectsFreq[obj]),
                        "maxConfidence": max(objectsFreq[obj]),
                        "minConfidence": min(objectsFreq[obj]),
                    }

        if period >= next_time:
            next_time += delta
            send_analytics(objectData, user_id)
            objectData = {}

        if not success:
            break
        else:
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video")
def video():
    if session.get("user") is None:
        return redirect("/signin")

    return render_template("video.html", cameras=get_cameras())


@app.route("/video_feed")
def video_feed():
    return Response(
        gen_frames(
            session["user"]["localId"] if session.get("user") is not None else None
        ),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if session.get("user") is not None:
        return render_template("profile.html", user=session["user"])

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if (
            first_name == ""
            or last_name == ""
            or email == ""
            or password == ""
            or confirm_password == ""
        ):
            return render_template("signup.html", error="All fields are required")

        if password != confirm_password:
            return render_template("signup.html", error="Passwords do not match")

        user = auth.create_user_with_email_and_password(email, password)
        user = auth.update_profile(
            id_token=user["idToken"], display_name=first_name + " " + last_name
        )

        session["user"] = user

        return redirect("/profile")

    return render_template("signup.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == "" or password == "":
            return render_template("signin.html", error="All fields are required")

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session["user"] = user
            return redirect("/profile")
        except:
            return render_template("signin.html", error="Invalid email or password")

    return render_template("signin.html")


@app.route("/signout")
def signout():
    session.pop("user", None)
    return render_template("signin.html")


@app.route("/profile")
def profile():
    if session.get("user") is None:
        return redirect("/signin")

    return render_template("profile.html", user=session.get("user"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)
