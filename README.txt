ORB WebAR (Business Card — full-card video)
-----------------------------------------

Files created in this package:
- index.html          : WebAR viewer (client)
- webar.js            : client-side ORB matcher + Three.js overlay
- compile.py          : server-side ORB extractor (Python + OpenCV)
- target/target.jpg   : default high-feature business-card style target
- target/target.json  : ORB keypoints & descriptors (generated)
- assets/video.mp4    : placeholder overlay video
- README.txt          : this file

How to run (client only):
1. Serve this folder over HTTP (GitHub Pages or local server recommended):
   - python -m http.server 8000
   - or: npx http-server

2. Open http://localhost:8000 in your mobile browser (HTTPS recommended for camera on mobile)

3. Tap "Tap to Start AR", allow camera, point at the printed card (or the displayed target).
   The video will play mapped to the full card when detected.

How to regenerate target.json from a new image (server-side compile):
1. Install OpenCV for Python: pip install opencv-python
2. Run: python compile.py target/newcard.jpg target/newcard.json
3. Replace target/target.jpg and target/target.json on the client.

Notes:
- This is an MVP ORB-based tracker. Performance varies across devices.
- For better robustness increase ORB features or use AKAZE/SIFT (compile.py can be adapted).
- If you want, I can swap 'target/target.jpg' with your real business card and generate the target.json for you.

