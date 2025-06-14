# Motion Detection with OpenCV

This project demonstrates real-time motion detection using OpenCV and background subtraction (MOG2). It captures live video feed from the webcam, detects moving objects, and highlights them with bounding boxes.

## 📸 Features

- Real-time video capture via webcam
- Motion detection using background subtraction (MOG2)
- Bounding boxes drawn around significant motion
- Foreground mask visualization
- Adjustable contour area threshold to ignore small movements
- Press `q` to quit

## 🛠️ Requirements

- Python 3.x
- OpenCV (`opencv-python`)

Install required libraries:
```bash
pip install opencv-python

🚀 How to Run
Clone the repository:


git clone https://github.com/your-username/motion-detection-opencv.git
cd motion-detection-opencv
Run the script:


python motion_detector.py
🧠 How It Works
A background subtractor is used to isolate moving elements in the video feed.
Foreground contours are extracted and filtered by area.
Detected objects above a set threshold (e.g., 500 pixels) are highlighted in green rectangles.
Visual output includes:
The video frame with motion boxes
The foreground mask showing motion regions
📂 File Structure

motion-detection-opencv/
│
├── motion_detector.py      # Main script
├── README.md               # Project documentation
📌 Sample Output
sample
(optional if you add an image)

💡 Future Improvements
Record video on motion
Alert via email/SMS
Person detection using YOLO or Haar cascades
Deploy on Raspberry Pi for CCTV applications
📄 License
This project is open-source and available under the MIT License.

Made with ❤️ using OpenCV


### ✅ To Use It:
1. Create a file in your project root called `README.md`
2. Paste the above content and update:
   - `your-username` in the GitHub URL and image path
   - Add a sample image if you want
   - Adjust file/script names if yours differ
