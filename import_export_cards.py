import zmq

from file_tools import *

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5554")


while True:
    message = socket.recv().decode()

    if message == 'Exit':
        break

    if message.split('; ')[0] == "Check":
        result = str(check_filepath(message.split('; ')[1]))
    elif message.split('; ')[0] == "Import":
        result = read_filepath(message.split('; ')[1])
    elif message.split('; ')[0] == "Export":
        print("Cards: " + str(message.split('; ')[2]))
        write_filepath(message.split('; ')[1], message.split('; ')[2])
        result = "File successfully exported."
    else:
        result = "Invalid command."

    socket.send_string(result)
