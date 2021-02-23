# Dependencies

- OpenCV installed
- Python 3+

# Get started

```
python -m venv venv
pip install -r requirements.txt 
```

In two distinct terminals:
```
// Start the server
python -m app.server.video_server

// Start the client
python -m app.client.video_client
```



# video-processing-grpc

Client-Server app where videos are consumed using gRPC communication. You are free to add the processing business logic
in the processing.py file. 



python -m grpc_tools.protoc -I protos --python_out=./app/messages --grpc_python_out=./app/messages ./protos/messages.proto