import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request = {
    "address": "Portland, Oregon",
    "start_day": 1,
    "start_month": 1,
    "start_year": 2019,
    "end_day": 1,
    "end_month": 1,
    "end_year": 2023
}

socket.send_string(json.dumps(request))
response = socket.recv_string()
print("Server response:", response)
