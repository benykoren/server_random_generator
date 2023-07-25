# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import random_pb2 as random__pb2


class RandomStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AskForRandom = channel.unary_unary(
                '/Random/AskForRandom',
                request_serializer=random__pb2.RandomRequest.SerializeToString,
                response_deserializer=random__pb2.RandomReply.FromString,
                )


class RandomServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AskForRandom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RandomServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AskForRandom': grpc.unary_unary_rpc_method_handler(
                    servicer.AskForRandom,
                    request_deserializer=random__pb2.RandomRequest.FromString,
                    response_serializer=random__pb2.RandomReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Random', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Random(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AskForRandom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Random/AskForRandom',
            random__pb2.RandomRequest.SerializeToString,
            random__pb2.RandomReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
