from numpy import argmax, array, expand_dims
import cv2
from keras.models import load_model

model = load_model("Resources/SLmodel.keras")

alphabet_elements = [chr(ord('a') + i) for i in range(26)]
numeric_elements = [str(i) for i in range(10)]
combined_array = alphabet_elements + numeric_elements
sign = array(combined_array)
print(sign)

# Access the computer's camera (usually the default camera, 0)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    normalized_frame = cv2.normalize(gray_frame, None, 0, 255, cv2.NORM_MINMAX)
    resized_frame = cv2.resize(normalized_frame, (28, 28))
    reshaped_frame = expand_dims(resized_frame, axis=-1)
    
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Processed Frame", reshaped_frame)

    processed_frame = reshaped_frame / 255.0  # Normalize to [0, 1]
    processed_frame = expand_dims(processed_frame, axis=0)
    processed_frame = processed_frame.reshape((1, 28, 28, 1))

    prediction = model.predict(processed_frame)
    print(sign[argmax(prediction, axis=1)])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
