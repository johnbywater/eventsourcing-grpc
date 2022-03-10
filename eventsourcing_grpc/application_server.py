from concurrent.futures import ThreadPoolExecutor

import grpc

from eventsourcing_grpc.application_pb2 import Empty
from eventsourcing_grpc.application_pb2_grpc import (
    ApplicationServicer,
    add_ApplicationServicer_to_server,
)


class ApplicationServer(ApplicationServicer):
    def __init__(self, address):
        self.address = address

    def start(self):
        """
        Starts gRPC server.
        """
        self.executor = ThreadPoolExecutor(max_workers=10)
        self.server = grpc.server(self.executor)
        # logging.info(self.application_class)
        add_ApplicationServicer_to_server(self, self.server)
        self.server.add_insecure_port(self.address)
        self.server.start()

    def stop(self, grace=1):
        print("Stopping application server")
        self.server.stop(grace=grace)

    def Ping(self, request: Empty, context):
        return Empty()
