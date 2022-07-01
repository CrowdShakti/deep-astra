from typing import Dict, Any

from deepface import DeepFace
from retinaface import RetinaFace
from tempfile import NamedTemporaryFile
from pathlib import Path
import shutil
import json


def analyze_faces(image):
    """
    Predicts all the face from the image.
    Args:
        image (File): The image to be predicted.
    """
    face_analysis = []
    try:

        suffix = Path(image.filename).suffix
        # Save file to tmp folder
        with NamedTemporaryFile(delete=False,suffix=suffix) as tmp:
            shutil.copyfileobj(image.file, tmp)
            tmp_path = Path(tmp.name)

        # using RetinaFace get location of faces and extract faces
        all_faces_location  = RetinaFace.detect_faces(str(tmp_path))
        faces = RetinaFace.extract_faces(str(tmp_path),align = True)
        
        face_count = 1

        # process each face
        for face in faces:
            temp = all_faces_location["face_"+str(face_count)]
            temp['score'] = str(temp['score']) 
            temp['facial_area'] = [int(i) for i in temp['facial_area']]
            temp['landmarks']['right_eye'] = [int(i) for i in temp['landmarks']['right_eye']]
            temp['landmarks']['left_eye'] = [int(i) for i in temp['landmarks']['left_eye']]
            temp['landmarks']['nose'] = [int(i) for i in temp['landmarks']['nose']]
            temp['landmarks']['mouth_right'] = [int(i) for i in temp['landmarks']['mouth_right']]
            temp['landmarks']['mouth_left'] = [int(i) for i in temp['landmarks']['mouth_left']]
            temp["analysis"] = DeepFace.analyze(face, actions = ["age", "gender","emotion","race"], detector_backend = 'skip')
            face_analysis.append(temp)
            face_count += 1
    finally:
        image.file.close()
        
    return {"faces" : face_analysis}