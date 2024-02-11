import cv2
import face_recognition


known_face_encodings = []
known_face_names = []

known_person1_image = face_recognition.load_image_file("image/PHOTO.jpg")
known_person2_image = face_recognition.load_image_file("image/avi-photo.jpg")
known_person3_image = face_recognition.load_image_file("image/bhavika.jpg")

known_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]
known_person3_encoding = face_recognition.face_encodings(known_person3_image)[0]

known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person3_encoding)

known_face_names.append("kuljeet")
known_face_names.append("ayush")
known_face_names.append("bhavu my love")

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    if not ret:
        print("Error: Failed to capture frame from the video source.")
        break

    face_locations = face_recognition.face_locations(frame)
    if not face_locations:
        print("No faces detected in the frame.")
        continue

    face_encodings = face_recognition.face_encodings(frame, face_locations)

    headcount = len(face_locations) # heads

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        color = (0, 0, 255)  # criminal face harshita

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            if name == "kuljeet":
                color = (0, 255, 0)  # Green color for kuljeet
            elif name == "ayush":
                color = (0, 0, 0)  # Black color for ayush
            elif name == "bhavu my love":
                color = (255, 153, 255)  # Pink color for bhavu baby





        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)


    cv2.putText(frame, f"Headcount: {headcount}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
