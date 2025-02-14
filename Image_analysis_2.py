import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("your_image.jpg")  # Replace with your image path

# Convert from BGR (OpenCV default) to RGB (for proper display)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(image_rgb)
plt.axis("off")  # Hide axes
plt.show()