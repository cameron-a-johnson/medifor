# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from medifor.v1 import provenance_pb2 as medifor_dot_v1_dot_provenance__pb2


class ProvenanceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ProvenanceFiltering = channel.unary_unary(
        '/mediforproto.Provenance/ProvenanceFiltering',
        request_serializer=medifor_dot_v1_dot_provenance__pb2.ImageFilterRequest.SerializeToString,
        response_deserializer=medifor_dot_v1_dot_provenance__pb2.ImageFilter.FromString,
        )
    self.ProvenanceGraphBuilding = channel.unary_unary(
        '/mediforproto.Provenance/ProvenanceGraphBuilding',
        request_serializer=medifor_dot_v1_dot_provenance__pb2.ProvenanceGraphRequest.SerializeToString,
        response_deserializer=medifor_dot_v1_dot_provenance__pb2.ProvenanceGraph.FromString,
        )


class ProvenanceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ProvenanceFiltering(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ProvenanceGraphBuilding(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProvenanceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ProvenanceFiltering': grpc.unary_unary_rpc_method_handler(
          servicer.ProvenanceFiltering,
          request_deserializer=medifor_dot_v1_dot_provenance__pb2.ImageFilterRequest.FromString,
          response_serializer=medifor_dot_v1_dot_provenance__pb2.ImageFilter.SerializeToString,
      ),
      'ProvenanceGraphBuilding': grpc.unary_unary_rpc_method_handler(
          servicer.ProvenanceGraphBuilding,
          request_deserializer=medifor_dot_v1_dot_provenance__pb2.ProvenanceGraphRequest.FromString,
          response_serializer=medifor_dot_v1_dot_provenance__pb2.ProvenanceGraph.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'mediforproto.Provenance', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
