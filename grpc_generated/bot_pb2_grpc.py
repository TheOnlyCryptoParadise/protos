# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import bot_comm_pb2 as bot__comm__pb2
import transaction_pb2 as transaction__pb2


class BotCommunicatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RemoveBot = channel.unary_unary(
                '/BotCommunicator/RemoveBot',
                request_serializer=bot__comm__pb2.BotRequest.SerializeToString,
                response_deserializer=bot__comm__pb2.BotResponse.FromString,
                )
        self.ResumeBot = channel.unary_unary(
                '/BotCommunicator/ResumeBot',
                request_serializer=bot__comm__pb2.BotRequest.SerializeToString,
                response_deserializer=bot__comm__pb2.BotResponse.FromString,
                )
        self.PauseBot = channel.unary_unary(
                '/BotCommunicator/PauseBot',
                request_serializer=bot__comm__pb2.BotRequest.SerializeToString,
                response_deserializer=bot__comm__pb2.BotResponse.FromString,
                )
        self.StopBot = channel.unary_unary(
                '/BotCommunicator/StopBot',
                request_serializer=bot__comm__pb2.BotRequest.SerializeToString,
                response_deserializer=bot__comm__pb2.BotResponse.FromString,
                )
        self.Ping = channel.unary_unary(
                '/BotCommunicator/Ping',
                request_serializer=bot__comm__pb2.BotRequest.SerializeToString,
                response_deserializer=bot__comm__pb2.BotResponse.FromString,
                )
        self.ResponseForRequestedTrade = channel.unary_unary(
                '/BotCommunicator/ResponseForRequestedTrade',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=bot__comm__pb2.BotResponse.FromString,
                )
        self.SendOpenTrades = channel.unary_unary(
                '/BotCommunicator/SendOpenTrades',
                request_serializer=transaction__pb2.Transactions.SerializeToString,
                response_deserializer=bot__comm__pb2.BotResponse.FromString,
                )


class BotCommunicatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RemoveBot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResumeBot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PauseBot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopBot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResponseForRequestedTrade(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendOpenTrades(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BotCommunicatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RemoveBot': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveBot,
                    request_deserializer=bot__comm__pb2.BotRequest.FromString,
                    response_serializer=bot__comm__pb2.BotResponse.SerializeToString,
            ),
            'ResumeBot': grpc.unary_unary_rpc_method_handler(
                    servicer.ResumeBot,
                    request_deserializer=bot__comm__pb2.BotRequest.FromString,
                    response_serializer=bot__comm__pb2.BotResponse.SerializeToString,
            ),
            'PauseBot': grpc.unary_unary_rpc_method_handler(
                    servicer.PauseBot,
                    request_deserializer=bot__comm__pb2.BotRequest.FromString,
                    response_serializer=bot__comm__pb2.BotResponse.SerializeToString,
            ),
            'StopBot': grpc.unary_unary_rpc_method_handler(
                    servicer.StopBot,
                    request_deserializer=bot__comm__pb2.BotRequest.FromString,
                    response_serializer=bot__comm__pb2.BotResponse.SerializeToString,
            ),
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=bot__comm__pb2.BotRequest.FromString,
                    response_serializer=bot__comm__pb2.BotResponse.SerializeToString,
            ),
            'ResponseForRequestedTrade': grpc.unary_unary_rpc_method_handler(
                    servicer.ResponseForRequestedTrade,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=bot__comm__pb2.BotResponse.SerializeToString,
            ),
            'SendOpenTrades': grpc.unary_unary_rpc_method_handler(
                    servicer.SendOpenTrades,
                    request_deserializer=transaction__pb2.Transactions.FromString,
                    response_serializer=bot__comm__pb2.BotResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BotCommunicator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BotCommunicator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RemoveBot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotCommunicator/RemoveBot',
            bot__comm__pb2.BotRequest.SerializeToString,
            bot__comm__pb2.BotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResumeBot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotCommunicator/ResumeBot',
            bot__comm__pb2.BotRequest.SerializeToString,
            bot__comm__pb2.BotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PauseBot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotCommunicator/PauseBot',
            bot__comm__pb2.BotRequest.SerializeToString,
            bot__comm__pb2.BotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopBot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotCommunicator/StopBot',
            bot__comm__pb2.BotRequest.SerializeToString,
            bot__comm__pb2.BotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotCommunicator/Ping',
            bot__comm__pb2.BotRequest.SerializeToString,
            bot__comm__pb2.BotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResponseForRequestedTrade(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotCommunicator/ResponseForRequestedTrade',
            transaction__pb2.Transaction.SerializeToString,
            bot__comm__pb2.BotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendOpenTrades(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotCommunicator/SendOpenTrades',
            transaction__pb2.Transactions.SerializeToString,
            bot__comm__pb2.BotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
