# Copyright 2021 CrowdShakti
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Dict, Any

from fastapi import APIRouter, UploadFile, File, WebSocket, BackgroundTasks
from starlette.websockets import WebSocketDisconnect

from app.models.face import Face

# LOGGER = logger.for_handler('face_recognition')

faces_router = r = APIRouter()


@r.post('/face-processor/faces')
def add_face(face: Face):
    """
    Registers the face into the database.
    Args:
        face (Face): Consists of the face encoding and the name of the person.
    """
    pass

@r.delete('/face-processor/faces')
def delete_face(face: Face):
    """
    Deletes the face from the database.
    Args:
        face (Face): Consists of the face image and the name of the person.
    """
    pass

@r.get('/face-processor/faces')
def get_faces():
    """
    Retrieves all faces from the database.
    """
    pass

@r.post('/face-processor/predict')
def predict():
    """
    Predicts all the face from the image.
    Args:
        image (File): The image to be predicted.
    """
    pass
