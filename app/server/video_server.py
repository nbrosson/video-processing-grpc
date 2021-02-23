from concurrent import futures

import time
import cv2
import grpc
import numpy as np
from app.messages import messages_pb2_grpc, messages_pb2
from app.server.processing import process_frame
from app import CONFIG


_ONE_DAY_IN_SECONDS = 0


class VideoProcessor(messages_pb2_grpc.VideoProcessorServicer):

    def GetVideoAnalysis(self, request_iterator, context):
        print("Server started")
        for req in request_iterator:

            nparr = np.fromstring(req.img, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # the business logic (ex: face detection), should be in process_frame()
            resp = process_frame(frame)
            yield messages_pb2.ImageResponse(reply=resp)


def serve():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=int(CONFIG["application"]["NB_WORKERS"])),
        options=[
            ('grpc.max_send_message_length', int(CONFIG["application"]["MAX_MESSAGE_LENGTH"])),
            ('grpc.max_receive_message_length', int(CONFIG["application"]["MAX_MESSAGE_LENGTH"])),
        ]
    )
    messages_pb2_grpc.add_VideoProcessorServicer_to_server(VideoProcessor(), server)
    server.add_insecure_port(f'[::]:{CONFIG["application"]["SERVER_PORT"]}')
    print(f'Listening at localhost:{CONFIG["application"]["SERVER_PORT"]}')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
