import cv2

# 打开摄像头
cap = cv2.VideoCapture(0)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # 读取一帧图像
    ret, frame = cap.read()

    # 显示实时图像
    cv2.imshow('Camera', frame)

    # 检测按键
    key = cv2.waitKey(1) & 0xFF

    # 按下 'c' 键拍照并保存
    if key == ord('c'):
        # 自定义文件名
        file_name = input("请输入“ID.姓名（英文）”:")
        file_name = file_name + ".jpg"

        # 保存图像
        cv2.imwrite(f"data/Temp-Information/{file_name}", frame)

        print(f"图像已保存为 {file_name}")

# 释放摄像头
cap.release()

# 关闭所有窗口
cv2.destroyAllWindows()
