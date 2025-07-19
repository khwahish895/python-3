import cv2
import dlib
import numpy as np

# Initialize dlib's face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Download this file

def get_landmarks(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    if len(faces) == 0:
        return None
    landmarks = predictor(gray, faces[0])
    return np.array([[p.x, p.y] for p in landmarks.parts()])

def face_swap(img1, img2):
    # Get facial landmarks
    landmarks1 = get_landmarks(img1)
    landmarks2 = get_landmarks(img2)
    
    if landmarks1 is None or landmarks2 is None:
        print("Could not detect faces in one or both images")
        return None
    
    # Calculate convex hull for both faces
    hull1 = cv2.convexHull(landmarks1)
    hull2 = cv2.convexHull(landmarks2)
    
    # Create masks
    mask1 = np.zeros_like(img1)
    mask2 = np.zeros_like(img2)
    cv2.fillConvexPoly(mask1, hull1, (255, 255, 255))
    cv2.fillConvexPoly(mask2, hull2, (255, 255, 255))
    
    # Find face center and calculate affine transform
    rect1 = cv2.boundingRect(hull1)
    rect2 = cv2.boundingRect(hull2)
    center1 = (rect1[0] + rect1[2]//2, rect1[1] + rect1[3]//2)
    center2 = (rect2[0] + rect2[2]//2, rect2[1] + rect2[3]//2)
    
    # Clone seamlessly
    output1 = img1.copy()
    output2 = img2.copy()
    output1 = cv2.seamlessClone(img2, output1, mask1, center1, cv2.NORMAL_CLONE)
    output2 = cv2.seamlessClone(img1, output2, mask2, center2, cv2.NORMAL_CLONE)
    
    return output1, output2

# Load images
img1 = cv2.imread("person1.jpg")
img2 = cv2.imread("person2.jpg")

# Resize images to same size (optional)
img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))

# Perform face swap
swapped1, swapped2 = face_swap(img1, img2)

if swapped1 is not None:
    cv2.imshow("Person 1 with Person 2's Face", swapped1)
    cv2.imshow("Person 2 with Person 1's Face", swapped2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save results
    cv2.imwrite("swapped_face1.jpg", swapped1)
    cv2.imwrite("swapped_face2.jpg", swapped2)
