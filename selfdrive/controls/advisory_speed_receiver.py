import cereal.messaging as messaging
import socket
import zmq

def main():
    pm = messaging.PubMaster(['advisorySpeed'])

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5090")
    print('Listen on 5090 for ZMQ')

    while True:
        try:
            #  Wait for next request from client
            message = socket.recv()
            print("Received request: %s" % message)
            #  Send reply back to client
            socket.send(b"ok")
            if message:
                advisory_speed = float(message)  # Convert the string to float
                print("send speed to " + advisory_speed)
                # Create and send the message using custom.AdvisorySpeed
                dat = messaging.new_message('customReserved1')
                dat.customReserved1.advisorySpeed = advisory_speed
                pm.send('advisorySpeed', dat)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
