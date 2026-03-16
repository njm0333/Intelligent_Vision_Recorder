import cv2 as cv
import time
import utils
from detector import ObjectDetector

def main():
    detector = ObjectDetector()

    rtsp_url = 'rtsp://210.99.70.120:1935/live/cctv006.stream'
    cap = cv.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("비디오 스트림 에러")
        return

    cv.namedWindow('My Video Recorder')
    cv.setMouseCallback('My Video Recorder', utils.mouse_handler)

    out = None
    is_recording = False
    contrast = 1.0
    brightness = 0
    is_flipped = False
    record_start_time = 0

    while True:
        valid, frame = cap.read()
        if not valid:
            print("프레임을 읽어올 수 없습니다.")
            break

        if is_flipped:
            frame = cv.flip(frame, 1)
        frame = cv.convertScaleAbs(frame, alpha=contrast, beta=brightness)
        display_frame = detector.detect_and_draw(frame)

        if utils.drawing and not utils.is_zoomed:
            cv.rectangle(display_frame, (utils.ix, utils.iy), (utils.fx, utils.fy), (255, 0, 0), 2)

        if utils.is_zoomed and utils.zoom_rect is not None:
            x1, y1, x2, y2 = utils.zoom_rect
            orig_h, orig_w = display_frame.shape[:2]
            cropped_roi = display_frame[y1:y2, x1:x2]
            display_frame = cv.resize(cropped_roi, (orig_w, orig_h))
            cv.putText(display_frame, "ZOOMED IN (Right-click to reset)", (20, orig_h - 30),
                       cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        if is_recording:
            if out is None:
                record_start_time = time.time()
                h, w, _ = display_frame.shape
                fourcc = cv.VideoWriter_fourcc(*'XVID')
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                filename = f"record_{timestamp}.avi"
                out = cv.VideoWriter(filename, fourcc, 30.0, (w, h))
                print(f"녹화 시작: {filename}")

            elapsed_time = int(time.time() - record_start_time)
            mins, secs = divmod(elapsed_time, 60)
            time_str = f"REC {mins:02d}:{secs:02d}"

            if int(time.time() * 2) % 2 == 0:
                cv.circle(display_frame, (50, 120), 10, (0, 0, 255), -1)

            cv.putText(display_frame, time_str, (75, 130), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 3)
            cv.putText(display_frame, time_str, (75, 130), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            out.write(display_frame)
        else:
            if out is not None:
                out.release()
                out = None
                print("녹화 중지 및 파일 저장 성공.")

        cv.imshow('My Video Recorder', display_frame)

        key = cv.waitKey(1) & 0xFF
        if key == 27:
            break
        elif key == ord(' '):
            is_recording = not is_recording
        elif key == ord('f'):
            is_flipped = not is_flipped
        elif key == ord('='):
            contrast = min(contrast + 0.1, 3.0)
        elif key == ord('-'):
            contrast = max(contrast - 0.1, 0.1)
        elif key == ord(']'):
            brightness = min(brightness + 10, 100)
        elif key == ord('['):
            brightness = max(brightness - 10, -100)

    cap.release()
    if out is not None:
        out.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()