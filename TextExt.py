# download Libraries
!pip install easyocr 
!pip install opencv-python
!pip install matplotlib

#import Modules
import easyocr
import cv2
import matplotlib.pyplot as plt
 
# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])
 
# Load image
image_path = "p5.jpeg" #give path to image 
image = cv2.imread(image_path)
 
# Perform OCR on the image
result = reader.readtext(image)
 
# Save the extracted text to a file
output_file = 'out1'
with open(output_file, 'w') as file:
    for bbox, text, prob in result:
        file.write(f"Detected text: {text} (Probability: {prob:.2f})\n")
 
# Draw bounding boxes and display the results
for (bbox, text, prob) in result:
    # Convert the bbox points to integers
    top_left = tuple([int(val) for val in bbox[0]])
    bottom_right = tuple([int(val) for val in bbox[2]])
   
    # Draw the bounding box on the image
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
   
    # Put the recognized text on the image
    cv2.putText(image, text, (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
 
# Display the image with bounding boxes
plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
 
print(f"Extracted text has been saved to {output_file}")
