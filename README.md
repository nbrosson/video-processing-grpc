# Dependencies

- OpenCV installed
- Python 3+

# Get started

1. Install Python dependencies
```
python -m venv venv
pip install -r requirements.txt 
```

2. Generate the protobuf code:
```
python -m grpc_tools.protoc -I protos --python_out=./app/messages --grpc_python_out=./app/messages ./protos/messages.proto
```

3. Start the server and the app (in distinct terminals):
```
// Start the server
python -m app.server.video_server

// Start the client
python -m app.client.video_client
```



# The project

This is a Client-Server app where videos are consumed using gRPC communication. 
In this code, there is no processing business logic. You must add your business logic
for the processing in the processing.py file (process_frame function). 

### Scalability

You can add more workers to your application, if you need to have more clients. 
Each worker will have their own memory. 

