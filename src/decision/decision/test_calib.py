#!/usr/bin/env python3
# 这个是AI帮我写的，用于动态调整颜色识别阈值。它不会被构建进ROS2包中，仅作为脚本用于测试
"""
Interactive LAB calibrator for color thresholds.
Run: python3 lab_calibrator.py
Keys:
  s - save thresholds to color_config.yaml
  q / ESC - quit
"""
import cv2
import numpy as np
import yaml
import os

CONFIG_PATH = "color_config.yaml"
CAM_INDEX = 0

# Colors to calibrate (order will be used in windows)
COLOR_NAMES = ['red', 'green', 'blue', 'black', 'white']

# Default initial ranges (if no config file exists)
DEFAULTS = {
    'black': {'min': [0, 0, 0], 'max': [80, 140, 140]},
    'white': {'min': [200, 0, 0], 'max': [255, 140, 140]},
    # These are starting guesses — you'll tune them interactively
    'red':   {'min': [15, 140, 120], 'max': [255, 200, 180]},
    'green': {'min': [40, 40, 60],   'max': [220, 130, 150]},
    'blue':  {'min': [0, 120, 0],    'max': [180, 170, 130]},
}

# Utility: safe load config
def load_config(path):
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                cfg = yaml.safe_load(f)
            # Ensure fields exist
            for c in COLOR_NAMES:
                if c not in cfg:
                    cfg[c] = DEFAULTS[c]
            return cfg
        except Exception as e:
            print("Failed to load existing config:", e)
    return DEFAULTS.copy()

# Utility: save config in same format user expects
def save_config(path, cfg):
    with open(path, 'w') as f:
        yaml.safe_dump(cfg, f, default_flow_style=False, sort_keys=False)
    print("Saved config to", path)

# Trackbar helpers
def make_trackbar_window():
    cv2.namedWindow('controls', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('controls', 600, 800)
    # For each color and each channel create trackbars
    for color in COLOR_NAMES:
        # Create trackbars grouped by color (names prefixed with color)
        for ch in ['Lmin','Amin','Bmin','Lmax','Amax','Bmax']:
            cv2.createTrackbar(f"{color}_{ch}", 'controls', 0, 255, lambda x: None)
    # misc params
    cv2.createTrackbar("area_min", 'controls', 1000, 20000, lambda x: None)
    cv2.createTrackbar("morph_kernel", 'controls', 5, 31, lambda x: None)
    # ensure odd kernel
    cv2.setTrackbarPos("morph_kernel", 'controls', 5)

def set_trackbar_from_cfg(cfg):
    for color in COLOR_NAMES:
        mn = cfg[color]['min']
        mx = cfg[color]['max']
        cv2.setTrackbarPos(f"{color}_Lmin", 'controls', int(mn[0]))
        cv2.setTrackbarPos(f"{color}_Amin", 'controls', int(mn[1]))
        cv2.setTrackbarPos(f"{color}_Bmin", 'controls', int(mn[2]))
        cv2.setTrackbarPos(f"{color}_Lmax", 'controls', int(mx[0]))
        cv2.setTrackbarPos(f"{color}_Amax", 'controls', int(mx[1]))
        cv2.setTrackbarPos(f"{color}_Bmax", 'controls', int(mx[2]))
    cv2.setTrackbarPos("area_min", 'controls', 2500)
    cv2.setTrackbarPos("morph_kernel", 'controls', 5)

def read_cfg_from_trackbar():
    cfg = {}
    for color in COLOR_NAMES:
        mn = [
            cv2.getTrackbarPos(f"{color}_Lmin", 'controls'),
            cv2.getTrackbarPos(f"{color}_Amin", 'controls'),
            cv2.getTrackbarPos(f"{color}_Bmin", 'controls')
        ]
        mx = [
            cv2.getTrackbarPos(f"{color}_Lmax", 'controls'),
            cv2.getTrackbarPos(f"{color}_Amax", 'controls'),
            cv2.getTrackbarPos(f"{color}_Bmax", 'controls')
        ]
        # ensure min <= max
        for i in range(3):
            if mn[i] > mx[i]:
                mn[i], mx[i] = mx[i], mn[i]
        cfg[color] = {'min': mn, 'max': mx}
    area_min = cv2.getTrackbarPos("area_min", 'controls')
    kern = cv2.getTrackbarPos("morph_kernel", 'controls')
    if kern % 2 == 0:
        kern = max(1, kern-1)
    return cfg, area_min, kern

# Color to BGR mapping for drawing boxes
DRAW_COLORS = {
    'red': (0,0,255),
    'green': (0,255,0),
    'blue': (255,0,0),
    'black': (0,0,0),
    'white': (255,255,255)
}

def main():
    cfg = load_config(CONFIG_PATH)
    cap = cv2.VideoCapture(CAM_INDEX, cv2.CAP_V4L2)
    if not cap.isOpened():
        print("Failed to open camera. Try changing CAM_INDEX.")
        return

    make_trackbar_window()
    set_trackbar_from_cfg(cfg)

    print("Interactive LAB calibrator")
    print("  s - save config")
    print("  q / ESC - quit")
    print("Tune thresholds in the 'controls' window and watch masks. Use area_min/morph_kernel to filter.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read failed")
            break

        # resize for faster preview if needed
        scale = 1.0
        h, w = frame.shape[:2]
        if w > 1280:
            scale = 1280.0 / w
            frame = cv2.resize(frame, (int(w*scale), int(h*scale)), interpolation=cv2.INTER_LINEAR)

        # Blur and convert
        gb = cv2.GaussianBlur(frame, (5,5), 3)
        lab = cv2.cvtColor(gb, cv2.COLOR_BGR2LAB)

        # read cfg from trackbars
        cfg_now, area_min, morph_k = read_cfg_from_trackbar()

        # prepare overlay
        overlay = frame.copy()
        combined_mask = np.zeros(frame.shape[:2], dtype=np.uint8)

        # for display: stack masks
        mask_vis_list = []

        for color in COLOR_NAMES:
            mn = np.array(cfg_now[color]['min'], dtype=np.uint8)
            mx = np.array(cfg_now[color]['max'], dtype=np.uint8)
            mask = cv2.inRange(lab, mn, mx)
            # morphological cleanup
            kernel = np.ones((morph_k, morph_k), np.uint8)
            opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
            mask_vis_list.append(cv2.cvtColor(closed, cv2.COLOR_GRAY2BGR))

            # find contours and draw
            contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                largest = max(contours, key=cv2.contourArea)
                area = cv2.contourArea(largest)
                if area >= max(1, area_min):
                    x,y,w_box,h_box = cv2.boundingRect(largest)
                    cv2.rectangle(overlay, (x,y), (x+w_box, y+h_box), DRAW_COLORS.get(color,(0,255,255)), 2)
                    cv2.putText(overlay, f"{color} {int(area)}", (x, max(10,y-6)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, DRAW_COLORS.get(color,(0,255,255)), 2)
            # accumulate masks for visual
            combined_mask = cv2.bitwise_or(combined_mask, closed)

        # display windows
        # combined overlay (original with boxes) and combined mask
        combined_mask_color = cv2.applyColorMap(cv2.normalize(combined_mask, None, 0,255,cv2.NORM_MINMAX), cv2.COLORMAP_JET)
        top = np.hstack([frame, overlay])
        bottom = np.hstack(mask_vis_list[:3] + mask_vis_list[3:]) if len(mask_vis_list) >= 5 else np.hstack(mask_vis_list)
        # safe stacking: resize bottom to top height
        # 强制把 bottom 缩放到和 top 完全一致（宽、高）
        bottom = cv2.resize(bottom, (top.shape[1], top.shape[0]))
        display = np.vstack([top, bottom])

        cv2.imshow("Preview (original | overlay) - bottom: masks", display)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:
            break
        elif key == ord('s'):
            # write current cfg to file in requested format
            save_cfg = {}
            for c in COLOR_NAMES:
                save_cfg[c] = {
                    'min': cfg_now[c]['min'],
                    'max': cfg_now[c]['max']
                }
            save_config(CONFIG_PATH, save_cfg)
            print("Saved thresholds.")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
