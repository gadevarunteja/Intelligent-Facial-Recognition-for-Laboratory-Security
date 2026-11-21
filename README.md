\# INTELLIGENT FACIAL RECOGNITION FOR LABORATORY SECURITY



\## 1. Project Overview



An AI-based laboratory access control system developed using Python, OpenCV, MTCNN and FaceNet. The system identifies individuals through a webcam and grants or denies access based on predefined class permissions.



\## 2. Abstract



This project implements an intelligent facial recognition system for laboratory security. It uses MTCNN for face detection and FaceNet for facial feature extraction. The extracted facial embeddings are compared with stored embeddings using cosine distance. Based on the recognized person's class, the system determines whether access should be granted or denied.



\## 3. Problem Statement



Traditional laboratory security systems rely on manual verification, identity cards and passwords. These methods can be inconvenient and may allow unauthorized access.



This project introduces an automated facial recognition system to improve laboratory security and control access based on class permissions.



\## 4. Objectives



\- Develop a facial recognition-based security system.

\- Detect faces using MTCNN.

\- Extract facial features using FaceNet.

\- Generate and store facial embeddings.

\- Recognize individuals through a webcam.

\- Allow or deny access based on class authorization.

\- Automatically close the camera after 10 seconds without face detection, as required by the project design.



\## 5. Technologies Used



| Technology | Purpose |

|---|---|

| Python 3.10 | Programming language |

| OpenCV | Webcam and image processing |

| MTCNN | Face detection |

| FaceNet | Facial feature extraction |

| PyTorch | Deep learning framework |

| NumPy | Numerical operations |

| Pillow | Image processing |

| Pickle | Embedding storage |



\## 6. Algorithms



\*\*MTCNN (Multi-task Cascaded Convolutional Networks)\*\*



Detects faces in input images.



\*\*FaceNet\*\*



Converts detected facial images into numerical feature vectors called embeddings.



\*\*Cosine Distance\*\*



Compares the similarity between live facial embeddings and stored embeddings.



\*\*Threshold-based Matching\*\*



Determines whether the detected face matches a registered individual.



\## 7. Dataset Structure



The project uses three class folders containing registered individuals.



&#x20;   dataset/

&#x20;   |

&#x20;   |-- 12/

&#x20;   |   |-- poorna/

&#x20;   |   |-- sai/

&#x20;   |

&#x20;   |-- 13/

&#x20;   |   |-- shiva/

&#x20;   |

&#x20;   |-- 14/

&#x20;       |-- charan/



Each numbered folder represents a class, and each person's folder contains their facial images.



\## 8. Project Files



\- `generate\_embeddings.py` – Generates facial embeddings from dataset images.

\- `Face recoognition.py` – Performs real-time facial recognition and access control.

\- `embeddings.pkl` – Stores generated facial embeddings locally.

\- `dataset/` – Contains class-wise facial image collections.

\- `.gitignore` – Prevents private data and unnecessary files from being uploaded.



\## 9. Installation and Dependencies



Required software:

\- Python 3.10

\- Git

\- Webcam



Install the CPU-compatible PyTorch packages:



&#x20;   python -m pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cpu



Install the remaining libraries:



&#x20;   python -m pip install opencv-python facenet-pytorch numpy pillow



\## 10. How to Run



\*\*Step 1: Clone the repository\*\*



&#x20;   git clone https://github.com/gadevarunteja/Intelligent-Facial-Recognition-for-Laboratory-Security.git



\*\*Step 2: Open the project directory\*\*



&#x20;   cd Intelligent-Facial-Recognition-for-Laboratory-Security



\*\*Step 3: Prepare the dataset\*\*



Create the dataset folder and add the registered facial images using the class-wise structure described above.



\*\*Step 4: Generate embeddings\*\*



&#x20;   python generate\_embeddings.py



\*\*Step 5: Run the project\*\*



&#x20;   python "Face recoognition.py"



\*\*Step 6: Test access control\*\*



Enter the required class number when prompted.



For example:

\- Class 12 person requesting class 12: Access granted.

\- Class 13 person requesting class 12: Access denied.

\- Class 14 person requesting class 12: Access denied.



\## 11. Expected Results



\- Recognized authorized person: ACCESS GRANTED.

\- Recognized person from another class: ACCESS DENIED.

\- Unrecognized person: UNKNOWN PERSON.

\- No face detected for 10 seconds: Camera exits with a no-face-detected message.



\## 12. Applications



\- Laboratory security.

\- Educational institutions.

\- Restricted access areas.

\- Office access management.

\- Automated identity verification.



\## 13. Future Enhancements



\- Facial liveness detection.

\- Attendance management.

\- Access history and reports.

\- Database integration.

\- Graphical user interface.

\- Automated door-lock integration.



\## 14. Security and Privacy



Facial images and facial embeddings are biometric information. Keep the dataset and generated embeddings private. Do not upload them to a public repository without appropriate consent and security measures.



\---



\*\*Project Title:\*\* Intelligent Facial Recognition for Laboratory Security



\*\*Developed Using:\*\* Python, OpenCV, MTCNN, FaceNet and PyTorch.



\*\*GitHub:\*\* https://github.com/gadevarunteja/Intelligent-Facial-Recognition-for-Laboratory-Security

