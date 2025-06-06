import cv2
import os

# === CHANGE THIS TO THE LABEL YOU'RE RECORDING ===
label = "A"
save_dir = f"dataset/{label}"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

cap = cv2.VideoCapture(0)
count = 0

print("[INFO] Press 'c' to capture image, 'q' to quit.")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Flip for mirror image
    cv2.rectangle(frame, (100, 100), (300, 300), (255, 0, 0), 2)
    roi = frame[100:300, 100:300]
    
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        file_path = os.path.join(save_dir, f"{count}.jpg")
        cv2.imwrite(file_path, roi)
        print(f"[INFO] Saved: {file_path}")
        count += 1

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
