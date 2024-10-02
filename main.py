import cv2

from config import filters_seq
from pipe import Pipe


def run_filters_seq(input_pipe: Pipe, output_pipe: Pipe) -> None:
    temp_input_pipe = Pipe()
    temp_output_pipe = Pipe()

    for i, flt_cls in enumerate(filters_seq):
        if i == 0:
            flt = flt_cls([input_pipe], [temp_output_pipe])
            temp_input_pipe = temp_output_pipe
            temp_output_pipe = Pipe()

        elif i == len(filters_seq) - 1:
            flt = flt_cls([temp_input_pipe], [output_pipe])

        else:
            flt = flt_cls([temp_input_pipe], [temp_output_pipe])
            temp_input_pipe = temp_output_pipe
            temp_output_pipe = Pipe()

        flt.run()


if __name__ == '__main__':
    input_pipe = Pipe()
    output_pipe = Pipe()

    run_filters_seq(input_pipe, output_pipe)

    vid = cv2.VideoCapture(0)
    if not vid.isOpened():
        print('Cannot open camera')
        exit()

    while True:
        ret, frame = vid.read()
        if not ret:
            print('Can not receive frame')
            break
        input_pipe.send(frame)

        cv2.imshow('Source', frame)
        cv2.imshow('WebCam', output_pipe.recv())

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()

    cv2.destroyAllWindows()
