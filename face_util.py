import face_recognition as fr
import base64,io
from PIL import Image
import numpy as np

def compare_faces(file1, file2):
    # Load the jpg files into numpy arrays
    image1 = file1
    image2 = fr.load_image_file(file2)
    
    # Get the face encodings for 1st face in each image file
    image1_encoding = fr.face_encodings(image1)[0]
    image2_encoding = fr.face_encodings(image2)[0]
    
    # Compare faces and return True / False
    results = fr.compare_faces([image1_encoding], image2_encoding)
    print(results)    
    return results[0]

# Each face is tuple of (Name,sample image)    
known_faces = {'1784521':'Training_images/Dhoni.jpg',
               '1784525':'Training_images/Messi.jpg',
               '1604439':'Training_images/Satyam.jpg',
               '1604425':'Training_images/Satyam.jpg'
              }
    
def face_rec(baseImage,EmpID):
    """
    Return name for a known face, otherwise return 'Uknown'.
    """
    baseImage = baseImage[23:]
    imgdata = base64.b64decode(baseImage)
    imageData = Image.open(io.BytesIO(imgdata))
    imageData = np.asarray(imageData)
    
    file = known_faces[EmpID]
    
    if compare_faces(imageData,file):
        return EmpID
    return 'Unknown' 

