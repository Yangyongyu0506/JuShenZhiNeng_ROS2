# 这个是用来可视化颜色识别效果的脚本，仅作为测试用，不会被构建进ROS2包中
import cv2
import yaml
import numpy as np

lab_config = yaml.safe_load(open('../data/color_config.yaml'))

def img_detect_color(img):
    gb_image = cv2.GaussianBlur(img, (3, 3), 3)
    lab_image = cv2.cvtColor(gb_image, cv2.COLOR_BGR2LAB) # Convert to LAB color space

    for color in ['red', 'green', 'blue']:
        mask = cv2.inRange(
            lab_image,
            (lab_config[color]['min'][0],
            lab_config[color]['min'][1],
            lab_config[color]['min'][2]),
            (lab_config[color]['max'][0],
            lab_config[color]['max'][1],
            lab_config[color]['max'][2])
        )
        opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel := np.ones((5, 5), np.uint8))  # 开运算
        closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)  # 闭运算
        contours = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]  # 找出轮廓
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            if (area := cv2.contourArea(largest_contour)) > 2500:
                x, y, w, h = cv2.boundingRect(largest_contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
                cv2.putText(img, color + f' area: {area}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
    return img

if __name__ == '__main__':
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FPS, 10)
    try:
        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imshow("Color Detection", img_detect_color(cv2.flip(frame, -1)))
                cv2.waitKey(1)
    except Exception as e:
        print(f"Error: {e}")
        cap.release()
        cv2.destroyAllWindows()
