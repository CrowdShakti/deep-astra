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

from pydantic import BaseModel, Field
from typing import List



class FaceAnalysis(BaseModel):
    """
        age : int
        gender : str
        emotion: dict
        dominant_emotion: str
        race : dict
        dominant_race: str
    """
    age: int
    gender: str
    emotion: dict
    dominant_emotion: str
    race : dict
    dominant_race: str

class FaceLandMarks(BaseModel):
    """
        right_eye : list
        left_eye : list
        nose : list
        mouth_right : list
        mouth_left : list
    """
    right_eye : list
    left_eye : list
    nose : list
    mouth_right : list
    mouth_left : list

class Face(BaseModel):
    """
        encoding : array
        name : string
    """
    facial_area: list
    landmarks: FaceLandMarks = Field(...)
    analysis: FaceAnalysis = Field(...)

class FaceList(BaseModel):
    faces: List[Face]

