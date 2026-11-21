import cv2
import pickle
import numpy as np
import torch
import time
from facenet_pytorch import InceptionResnetV1, MTCNN
from collections import deque
# ---------------- INIT ----------------
device = 'cuda' if torch.cuda.is_available() else 'cpu'
mtcnn = MTCNN(keep_all=True, device=device)
model = InceptionResnetV1(pretrained='vggface2').eval().to(device)

with open("embeddings.pkl", "rb") as f:
    database = pickle.load(f)

# ---------------- PARAMETERS ----------------
THRESHOLD = 0.45
FRAME_BUFFER = 5

recent_predictions = deque(maxlen=FRAME_BUFFER)

# ---------------- NEW TIMER ----------------
no_face_start_time = time.time()

# ---------------- FUNCTIONS ----------------
def cosine_distance(a, b):
    return 1 - np.dot(a, b)

def recognize(face_embedding):
    min_dist = float("inf")
    identity = None
    identity_class = None

    for entry in database:
        dist = cosine_distance(face_embedding, entry["embedding"])
        if dist < min_dist:
            min_dist = dist
            identity = entry["name"]
            identity_class = entry["class"]

    if min_dist < THRESHOLD:
        confidence = (1 - min_dist) * 100
        return identity, identity_class, confidence
    else:
        return "Unknown", None, None

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print(" Camera not accessible")
    exit()

INPUT_CLASS = input("Enter required class (e.g., 12): ")

face_detected_time = None
AUTHORIZED = False
UNAUTHORIZED = False

print(" Starting camera...")

# ---------------- MAIN LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        print(" Frame not captured")
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes, _ = mtcnn.detect(rgb)

    # ---------------- FACE DETECTED ----------------
    if boxes is not None:
        no_face_start_time = None  #  Reset no-face timer

        if face_detected_time is None:
            face_detected_time = time.time()

        for box in boxes:
            x1, y1, x2, y2 = map(int, box)

            face = rgb[y1:y2, x1:x2]
            if face.size == 0:
                continue

            face = cv2.resize(face, (160, 160))
            face = face / 255.0

            face_tensor = torch.tensor(face).permute(2, 0, 1).float().unsqueeze(0).to(device)

            with torch.no_grad():
                embedding = model(face_tensor).cpu().numpy()[0]

            embedding = embedding / np.linalg.norm(embedding)

            name, person_class, confidence = recognize(embedding)

            # Stability smoothing
            recent_predictions.append(name if name != "Unknown" else None)
            stable_name = max(set(recent_predictions), key=recent_predictions.count)

            current_time = time.time()

            # ---------------- DECISION ----------------
            if stable_name is None:
                label = "UNKNOWN | ACCESS DENIED"
                color = (0, 0, 255)

                if current_time - face_detected_time > 10:
                    print("\n ACCESS DENIED: Unknown person")
                    UNAUTHORIZED = True

            else:
                if person_class == INPUT_CLASS:
                    label = f"{stable_name} | ACCESS GRANTED"
                    color = (0, 255, 0)

                    if current_time - face_detected_time > 10:
                        print(f"\n ACCESS GRANTED TO: {stable_name} (CLASS {person_class})")
                        AUTHORIZED = True

                else:
                    #  MODIFIED OUTPUT
                    label = f"CLASS {person_class} PERSON | ACCESS DENIED"
                    color = (0, 0, 255)

                    if current_time - face_detected_time > 10:
                        print(f"\n ACCESS DENIED: CLASS {person_class} person cannot enter CLASS {INPUT_CLASS}")
                        UNAUTHORIZED = True

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # ---------------- NO FACE DETECTED ----------------
    else:
        if no_face_start_time is None:
            no_face_start_time = time.time()

        elapsed_no_face = time.time() - no_face_start_time

        cv2.putText(frame, "No Face Detected", (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        if elapsed_no_face > 10:
            print("\n NO FACE DETECTED FOR 10 SECONDS. EXITING...")
            break

        face_detected_time = None
        recent_predictions.clear()

    cv2.imshow("Face Access Control", frame)

    if AUTHORIZED or UNAUTHORIZED:
        break

    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()