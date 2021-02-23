from __future__ import print_function

import grpc
import cv2
from app.messages import messages_pb2, messages_pb2_grpc
from app import CONFIG


def run():
    channel = grpc.insecure_channel(
        f'localhost:{CONFIG["application"]["SERVER_PORT"]}',
        options=[
            ('grpc.max_send_message_length', int(CONFIG["application"]["MAX_MESSAGE_LENGTH"])),
            ('grpc.max_receive_message_length', int(CONFIG["application"]["MAX_MESSAGE_LENGTH"])),
        ]
    )
    stub = messages_pb2_grpc.VideoProcessorStub(channel)
    for response in stub.GetVideoAnalysis(generate_requests()):
        print(str(response.reply))


def generate_requests():

    cap = cv2.VideoCapture(CONFIG["application"]["VIDEO_URL"])
    while cap.isOpened:
        ret, frame = cap.read()
        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        yield messages_pb2.ImageRequest(img=frame)


if __name__ == '__main__':
    run()
