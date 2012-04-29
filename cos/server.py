from cos.messages import Request, ErrorResponse
import zmq

class Worker():

    def run(self):
        context = zmq.Context()
    
        server = context.socket(zmq.REP)
        server.bind("tcp://*:5555")
        while True:
            raw_request = server.recv()
            try:
                request = Request.from_raw(raw_request)
                # do some dispatching shizzle
                response = ErrorResponse("Fo' shizzle")
            except:
                response = ErrorResponse('Fatal error')
    
            server.send(response.bson)
