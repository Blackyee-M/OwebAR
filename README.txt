WebAR MVP — Template Matching + Video Overlay (OpenCV.js + Three.js)

How to use:
1. Replace assets/target.jpg with your real target image (card/poster).
2. Put your overlay video at assets/video.mp4 (filename must be video.mp4).
3. Serve this folder on a local HTTP server (required for camera):
   - Using Node: npx http-server
   - Using Python: python -m http.server
4. Open the page in a browser (prefer mobile/chrome) at the printed URL.
5. Tap "Tap to Start AR", allow camera, point at your card. Video should play when matched.

Notes:
- OpenCV.js is loaded from CDN (docs.opencv.org). If you need full offline, download opencv.js and update index.html.
- Tuning: adjust scales array and threshold in the script for better detection.
- This is an MVP (template matching). For robust tracking use ORB-based advanced pipeline.

