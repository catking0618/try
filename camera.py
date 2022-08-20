import cv2

video = cv2.VideoCapture(0)     # 调用摄像头，PC电脑中0为内置摄像头，1为外接摄像头
judge = video.isOpened()      # 判断video是否打开
frame_size = (int(video.get(3)), int(video.get(4)))    # 获取摄像头分辨率

FPS = video.get(5)    # 获取摄像头帧率
print("FPS: ", FPS)

# 保存视频
code = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')    # 编码格式
fps = 25   # 保存视频的帧率
filename = "video.avi"    # 保存视频的路径和名字
out = cv2.VideoWriter(filename, code, fps, frame_size, isColor=True)    # 保存视频的视频流

if not(out.isOpened()):     # 判断视频流是否创建成功
    print('out is not opened')

while judge:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)  # flip():图像翻转函数   第二个参数 小于0: 180°旋转，等于0: 上下颠倒，大于0: 水平颠倒(镜像图)
    out.write(frame)     # 将图像写入视频流，生成视频
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# 释放窗口和视频流
video.release()
out.release()
cv2.destroyAllWindows()

