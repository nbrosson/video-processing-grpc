# video-processing-grpc
Client-Server app where videos are consumed using gRPC communication



python -m grpc_tools.protoc -I protos --python_out=./app/messages --grpc_python_out=./app/messages ./protos/messages.proto