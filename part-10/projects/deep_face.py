import cv2
from deepface import DeepFace
import numpy as np

def analyze_webcam():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        # Read frame from webcam
        ret, frame = cap.read()
        if not ret:
            break
            
        try:
            # Analyze the frame using DeepFace
            analysis = DeepFace.analyze(frame, 
                                      actions=['age', 'gender', 'emotion', 'race'],
                                      enforce_detection=False)
            
            # Extract results
            age = analysis[0]['age']
            gender = analysis[0]['gender']
            emotion = analysis[0]['dominant_emotion']
            race = analysis[0]['dominant_race']
            
            # Add text to frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, f'Age: {age}', (10, 30), font, 1, (0, 255, 0), 2)
            cv2.putText(frame, f'Gender: {gender}', (10, 70), font, 1, (0, 255, 0), 2)
            cv2.putText(frame, f'Emotion: {emotion}', (10, 110), font, 1, (0, 255, 0), 2)
            cv2.putText(frame, f'Race: {race}', (10, 150), font, 1, (0, 255, 0), 2)
            
        except Exception as e:
            # If no face is detected or other error occurs, continue to next frame
            pass
        
        # Display the frame
        cv2.imshow('Webcam Analysis', frame)
        
        # Break loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    analyze_webcam()