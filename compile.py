import cv2, json, sys
from pathlib import Path

def extract_orb(inpath, outpath, nfeatures=2000):
    img = cv2.imread(str(inpath), cv2.IMREAD_GRAYSCALE)
    orb = cv2.ORB_create(nfeatures)
    kps, des = orb.detectAndCompute(img, None)
    kps_list = []
    for k in kps:
        kps_list.append({'pt':[float(k.pt[0]), float(k.pt[1])],
                         'size':float(k.size),
                         'angle':float(k.angle),
                         'response':float(k.response),
                         'octave':int(k.octave)})
    des_list = des.tolist() if des is not None else []
    out = {'width': img.shape[1], 'height': img.shape[0], 'keypoints': kps_list, 'descriptors': des_list}
    Path(outpath).write_text(json.dumps(out))
    print('Wrote', outpath, 'keypoints:', len(kps_list))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python compile.py input.jpg output.json')
        sys.exit(1)
    extract_orb(sys.argv[1], sys.argv[2])
