import logging
import random
import sys
from concurrent import futures
from os.path import abspath, dirname

import grpc

parent_dir = abspath(dirname(dirname(__file__)))
sys.path.append(parent_dir)

import random_pb2 as pb2
import random_pb2_grpc as pb2_grpc
from database.database import DataBaseForRandoms

LOWER_BOUND = 1
UPPER_BOUND = 10000

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class RandomService(pb2_grpc.RandomServicer):
    def __init__(self):
        self.data_base_for_randoms = DataBaseForRandoms()

    def AskForRandom(self, request: pb2.RandomRequest, context: grpc.ServicerContext) -> pb2.RandomReply:
        result = random.randint(LOWER_BOUND, UPPER_BOUND)
        logging.info(f"Generated random number: {result}")
        self.store_random_number(result)
        result = {'random_number': result}
        return pb2.RandomReply(**result)

    def store_random_number(self, random_number: int) -> bool:
        return self.data_base_for_randoms.store_random_number(random_number=random_number)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    pb2_grpc.add_RandomServicer_to_server(RandomService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("Starting the server, waiting for requests...")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
