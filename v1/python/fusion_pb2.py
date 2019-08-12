# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fusion.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
import analytic_pb2 as analytic__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fusion.proto',
  package='mediforproto',
  syntax='proto3',
  serialized_options=_b('\n\030com.mediforprogram.protoB\013FusionProtoZ@gitlab.mediforprogram.com/medifor/medifor-proto/pkg/mediforproto'),
  serialized_pb=_b('\n\x0c\x66usion.proto\x12\x0cmediforproto\x1a\x17google/rpc/status.proto\x1a\x0e\x61nalytic.proto\"\xdf\x04\n\x06\x46usion\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12\x19\n\x11start_time_millis\x18\x02 \x01(\x03\x12\x17\n\x0f\x65nd_time_millis\x18\x03 \x01(\x03\x12\x43\n\rimg_manip_req\x18\x0b \x01(\x0b\x32*.mediforproto.FuseImageManipulationRequestH\x00\x12\x43\n\rvid_manip_req\x18\x0c \x01(\x0b\x32*.mediforproto.FuseVideoManipulationRequestH\x00\x12>\n\x0eimg_splice_req\x18\r \x01(\x0b\x32$.mediforproto.FuseImageSpliceRequestH\x00\x12\x46\n\x11img_cam_match_req\x18\x0e \x01(\x0b\x32).mediforproto.FuseImageCameraMatchRequestH\x00\x12\x34\n\timg_manip\x18\x15 \x01(\x0b\x32\x1f.mediforproto.ImageManipulationH\x01\x12\x34\n\tvid_manip\x18\x16 \x01(\x0b\x32\x1f.mediforproto.VideoManipulationH\x01\x12/\n\nimg_splice\x18\x17 \x01(\x0b\x32\x19.mediforproto.ImageSpliceH\x01\x12\x37\n\rimg_cam_match\x18\x18 \x01(\x0b\x32\x1e.mediforproto.ImageCameraMatchH\x01\x42\t\n\x07requestB\n\n\x08response\"h\n\x1a\x41nnotatedImageManipulation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12-\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1f.mediforproto.ImageManipulation\"\xd3\x01\n\x1c\x46useImageManipulationRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0f\n\x07out_dir\x18\x02 \x01(\t\x12=\n\rimg_manip_req\x18\x03 \x01(\x0b\x32&.mediforproto.ImageManipulationRequest\x12;\n\timg_manip\x18\x04 \x03(\x0b\x32(.mediforproto.AnnotatedImageManipulation\x12\x12\n\nwant_masks\x18\x05 \x01(\x08\"h\n\x1a\x41nnotatedVideoManipulation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12-\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1f.mediforproto.VideoManipulation\"\xd3\x01\n\x1c\x46useVideoManipulationRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0f\n\x07out_dir\x18\x02 \x01(\t\x12=\n\rvid_manip_req\x18\x03 \x01(\x0b\x32&.mediforproto.VideoManipulationRequest\x12;\n\tvid_manip\x18\x04 \x03(\x0b\x32(.mediforproto.AnnotatedVideoManipulation\x12\x12\n\nwant_masks\x18\x05 \x01(\x08\"\\\n\x14\x41nnotatedImageSplice\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\'\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x19.mediforproto.ImageSplice\"\xc3\x01\n\x16\x46useImageSpliceRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0f\n\x07out_dir\x18\x02 \x01(\t\x12\x38\n\x0eimg_splice_req\x18\x03 \x01(\x0b\x32 .mediforproto.ImageSpliceRequest\x12\x36\n\nimg_splice\x18\x04 \x03(\x0b\x32\".mediforproto.AnnotatedImageSplice\x12\x12\n\nwant_masks\x18\x05 \x01(\x08\"f\n\x19\x41nnotatedImageCameraMatch\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12,\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1e.mediforproto.ImageCameraMatch\"\xd8\x01\n\x1b\x46useImageCameraMatchRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0f\n\x07out_dir\x18\x02 \x01(\t\x12@\n\x11img_cam_match_req\x18\x03 \x01(\x0b\x32%.mediforproto.ImageCameraMatchRequest\x12>\n\rimg_cam_match\x18\x04 \x03(\x0b\x32\'.mediforproto.AnnotatedImageCameraMatch\x12\x12\n\nwant_masks\x18\x05 \x01(\x08\x32\xbc\x03\n\x05\x46user\x12\x64\n\x15\x46useImageManipulation\x12*.mediforproto.FuseImageManipulationRequest\x1a\x1f.mediforproto.ImageManipulation\x12R\n\x0f\x46useImageSplice\x12$.mediforproto.FuseImageSpliceRequest\x1a\x19.mediforproto.ImageSplice\x12\x64\n\x15\x46useVideoManipulation\x12*.mediforproto.FuseVideoManipulationRequest\x1a\x1f.mediforproto.VideoManipulation\x12\x61\n\x14\x46useImageCameraMatch\x12).mediforproto.FuseImageCameraMatchRequest\x1a\x1e.mediforproto.ImageCameraMatch\x12\x30\n\x04Kill\x12\x13.mediforproto.Empty\x1a\x13.mediforproto.EmptyBi\n\x18\x63om.mediforprogram.protoB\x0b\x46usionProtoZ@gitlab.mediforprogram.com/medifor/medifor-proto/pkg/mediforprotob\x06proto3')
  ,
  dependencies=[google_dot_rpc_dot_status__pb2.DESCRIPTOR,analytic__pb2.DESCRIPTOR,])




_FUSION = _descriptor.Descriptor(
  name='Fusion',
  full_name='mediforproto.Fusion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='mediforproto.Fusion.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time_millis', full_name='mediforproto.Fusion.start_time_millis', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time_millis', full_name='mediforproto.Fusion.end_time_millis', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_manip_req', full_name='mediforproto.Fusion.img_manip_req', index=3,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vid_manip_req', full_name='mediforproto.Fusion.vid_manip_req', index=4,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_splice_req', full_name='mediforproto.Fusion.img_splice_req', index=5,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_cam_match_req', full_name='mediforproto.Fusion.img_cam_match_req', index=6,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_manip', full_name='mediforproto.Fusion.img_manip', index=7,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vid_manip', full_name='mediforproto.Fusion.vid_manip', index=8,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_splice', full_name='mediforproto.Fusion.img_splice', index=9,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_cam_match', full_name='mediforproto.Fusion.img_cam_match', index=10,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='request', full_name='mediforproto.Fusion.request',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='response', full_name='mediforproto.Fusion.response',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=72,
  serialized_end=679,
)


_ANNOTATEDIMAGEMANIPULATION = _descriptor.Descriptor(
  name='AnnotatedImageManipulation',
  full_name='mediforproto.AnnotatedImageManipulation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mediforproto.AnnotatedImageManipulation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='mediforproto.AnnotatedImageManipulation.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='mediforproto.AnnotatedImageManipulation.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=681,
  serialized_end=785,
)


_FUSEIMAGEMANIPULATIONREQUEST = _descriptor.Descriptor(
  name='FuseImageManipulationRequest',
  full_name='mediforproto.FuseImageManipulationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='mediforproto.FuseImageManipulationRequest.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_dir', full_name='mediforproto.FuseImageManipulationRequest.out_dir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_manip_req', full_name='mediforproto.FuseImageManipulationRequest.img_manip_req', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_manip', full_name='mediforproto.FuseImageManipulationRequest.img_manip', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='want_masks', full_name='mediforproto.FuseImageManipulationRequest.want_masks', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=788,
  serialized_end=999,
)


_ANNOTATEDVIDEOMANIPULATION = _descriptor.Descriptor(
  name='AnnotatedVideoManipulation',
  full_name='mediforproto.AnnotatedVideoManipulation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mediforproto.AnnotatedVideoManipulation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='mediforproto.AnnotatedVideoManipulation.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='mediforproto.AnnotatedVideoManipulation.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1001,
  serialized_end=1105,
)


_FUSEVIDEOMANIPULATIONREQUEST = _descriptor.Descriptor(
  name='FuseVideoManipulationRequest',
  full_name='mediforproto.FuseVideoManipulationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='mediforproto.FuseVideoManipulationRequest.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_dir', full_name='mediforproto.FuseVideoManipulationRequest.out_dir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vid_manip_req', full_name='mediforproto.FuseVideoManipulationRequest.vid_manip_req', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vid_manip', full_name='mediforproto.FuseVideoManipulationRequest.vid_manip', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='want_masks', full_name='mediforproto.FuseVideoManipulationRequest.want_masks', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1108,
  serialized_end=1319,
)


_ANNOTATEDIMAGESPLICE = _descriptor.Descriptor(
  name='AnnotatedImageSplice',
  full_name='mediforproto.AnnotatedImageSplice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mediforproto.AnnotatedImageSplice.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='mediforproto.AnnotatedImageSplice.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='mediforproto.AnnotatedImageSplice.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1321,
  serialized_end=1413,
)


_FUSEIMAGESPLICEREQUEST = _descriptor.Descriptor(
  name='FuseImageSpliceRequest',
  full_name='mediforproto.FuseImageSpliceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='mediforproto.FuseImageSpliceRequest.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_dir', full_name='mediforproto.FuseImageSpliceRequest.out_dir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_splice_req', full_name='mediforproto.FuseImageSpliceRequest.img_splice_req', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_splice', full_name='mediforproto.FuseImageSpliceRequest.img_splice', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='want_masks', full_name='mediforproto.FuseImageSpliceRequest.want_masks', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1416,
  serialized_end=1611,
)


_ANNOTATEDIMAGECAMERAMATCH = _descriptor.Descriptor(
  name='AnnotatedImageCameraMatch',
  full_name='mediforproto.AnnotatedImageCameraMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mediforproto.AnnotatedImageCameraMatch.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='mediforproto.AnnotatedImageCameraMatch.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='mediforproto.AnnotatedImageCameraMatch.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1613,
  serialized_end=1715,
)


_FUSEIMAGECAMERAMATCHREQUEST = _descriptor.Descriptor(
  name='FuseImageCameraMatchRequest',
  full_name='mediforproto.FuseImageCameraMatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='mediforproto.FuseImageCameraMatchRequest.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_dir', full_name='mediforproto.FuseImageCameraMatchRequest.out_dir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_cam_match_req', full_name='mediforproto.FuseImageCameraMatchRequest.img_cam_match_req', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_cam_match', full_name='mediforproto.FuseImageCameraMatchRequest.img_cam_match', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='want_masks', full_name='mediforproto.FuseImageCameraMatchRequest.want_masks', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1718,
  serialized_end=1934,
)

_FUSION.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_FUSION.fields_by_name['img_manip_req'].message_type = _FUSEIMAGEMANIPULATIONREQUEST
_FUSION.fields_by_name['vid_manip_req'].message_type = _FUSEVIDEOMANIPULATIONREQUEST
_FUSION.fields_by_name['img_splice_req'].message_type = _FUSEIMAGESPLICEREQUEST
_FUSION.fields_by_name['img_cam_match_req'].message_type = _FUSEIMAGECAMERAMATCHREQUEST
_FUSION.fields_by_name['img_manip'].message_type = analytic__pb2._IMAGEMANIPULATION
_FUSION.fields_by_name['vid_manip'].message_type = analytic__pb2._VIDEOMANIPULATION
_FUSION.fields_by_name['img_splice'].message_type = analytic__pb2._IMAGESPLICE
_FUSION.fields_by_name['img_cam_match'].message_type = analytic__pb2._IMAGECAMERAMATCH
_FUSION.oneofs_by_name['request'].fields.append(
  _FUSION.fields_by_name['img_manip_req'])
_FUSION.fields_by_name['img_manip_req'].containing_oneof = _FUSION.oneofs_by_name['request']
_FUSION.oneofs_by_name['request'].fields.append(
  _FUSION.fields_by_name['vid_manip_req'])
_FUSION.fields_by_name['vid_manip_req'].containing_oneof = _FUSION.oneofs_by_name['request']
_FUSION.oneofs_by_name['request'].fields.append(
  _FUSION.fields_by_name['img_splice_req'])
_FUSION.fields_by_name['img_splice_req'].containing_oneof = _FUSION.oneofs_by_name['request']
_FUSION.oneofs_by_name['request'].fields.append(
  _FUSION.fields_by_name['img_cam_match_req'])
_FUSION.fields_by_name['img_cam_match_req'].containing_oneof = _FUSION.oneofs_by_name['request']
_FUSION.oneofs_by_name['response'].fields.append(
  _FUSION.fields_by_name['img_manip'])
_FUSION.fields_by_name['img_manip'].containing_oneof = _FUSION.oneofs_by_name['response']
_FUSION.oneofs_by_name['response'].fields.append(
  _FUSION.fields_by_name['vid_manip'])
_FUSION.fields_by_name['vid_manip'].containing_oneof = _FUSION.oneofs_by_name['response']
_FUSION.oneofs_by_name['response'].fields.append(
  _FUSION.fields_by_name['img_splice'])
_FUSION.fields_by_name['img_splice'].containing_oneof = _FUSION.oneofs_by_name['response']
_FUSION.oneofs_by_name['response'].fields.append(
  _FUSION.fields_by_name['img_cam_match'])
_FUSION.fields_by_name['img_cam_match'].containing_oneof = _FUSION.oneofs_by_name['response']
_ANNOTATEDIMAGEMANIPULATION.fields_by_name['data'].message_type = analytic__pb2._IMAGEMANIPULATION
_FUSEIMAGEMANIPULATIONREQUEST.fields_by_name['img_manip_req'].message_type = analytic__pb2._IMAGEMANIPULATIONREQUEST
_FUSEIMAGEMANIPULATIONREQUEST.fields_by_name['img_manip'].message_type = _ANNOTATEDIMAGEMANIPULATION
_ANNOTATEDVIDEOMANIPULATION.fields_by_name['data'].message_type = analytic__pb2._VIDEOMANIPULATION
_FUSEVIDEOMANIPULATIONREQUEST.fields_by_name['vid_manip_req'].message_type = analytic__pb2._VIDEOMANIPULATIONREQUEST
_FUSEVIDEOMANIPULATIONREQUEST.fields_by_name['vid_manip'].message_type = _ANNOTATEDVIDEOMANIPULATION
_ANNOTATEDIMAGESPLICE.fields_by_name['data'].message_type = analytic__pb2._IMAGESPLICE
_FUSEIMAGESPLICEREQUEST.fields_by_name['img_splice_req'].message_type = analytic__pb2._IMAGESPLICEREQUEST
_FUSEIMAGESPLICEREQUEST.fields_by_name['img_splice'].message_type = _ANNOTATEDIMAGESPLICE
_ANNOTATEDIMAGECAMERAMATCH.fields_by_name['data'].message_type = analytic__pb2._IMAGECAMERAMATCH
_FUSEIMAGECAMERAMATCHREQUEST.fields_by_name['img_cam_match_req'].message_type = analytic__pb2._IMAGECAMERAMATCHREQUEST
_FUSEIMAGECAMERAMATCHREQUEST.fields_by_name['img_cam_match'].message_type = _ANNOTATEDIMAGECAMERAMATCH
DESCRIPTOR.message_types_by_name['Fusion'] = _FUSION
DESCRIPTOR.message_types_by_name['AnnotatedImageManipulation'] = _ANNOTATEDIMAGEMANIPULATION
DESCRIPTOR.message_types_by_name['FuseImageManipulationRequest'] = _FUSEIMAGEMANIPULATIONREQUEST
DESCRIPTOR.message_types_by_name['AnnotatedVideoManipulation'] = _ANNOTATEDVIDEOMANIPULATION
DESCRIPTOR.message_types_by_name['FuseVideoManipulationRequest'] = _FUSEVIDEOMANIPULATIONREQUEST
DESCRIPTOR.message_types_by_name['AnnotatedImageSplice'] = _ANNOTATEDIMAGESPLICE
DESCRIPTOR.message_types_by_name['FuseImageSpliceRequest'] = _FUSEIMAGESPLICEREQUEST
DESCRIPTOR.message_types_by_name['AnnotatedImageCameraMatch'] = _ANNOTATEDIMAGECAMERAMATCH
DESCRIPTOR.message_types_by_name['FuseImageCameraMatchRequest'] = _FUSEIMAGECAMERAMATCHREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Fusion = _reflection.GeneratedProtocolMessageType('Fusion', (_message.Message,), dict(
  DESCRIPTOR = _FUSION,
  __module__ = 'fusion_pb2'
  # @@protoc_insertion_point(class_scope:mediforproto.Fusion)
  ))
_sym_db.RegisterMessage(Fusion)

AnnotatedImageManipulation = _reflection.GeneratedProtocolMessageType('AnnotatedImageManipulation', (_message.Message,), dict(
  DESCRIPTOR = _ANNOTATEDIMAGEMANIPULATION,
  __module__ = 'fusion_pb2'
  # @@protoc_insertion_point(class_scope:mediforproto.AnnotatedImageManipulation)
  ))
_sym_db.RegisterMessage(AnnotatedImageManipulation)

FuseImageManipulationRequest = _reflection.GeneratedProtocolMessageType('FuseImageManipulationRequest', (_message.Message,), dict(
  DESCRIPTOR = _FUSEIMAGEMANIPULATIONREQUEST,
  __module__ = 'fusion_pb2'
  # @@protoc_insertion_point(class_scope:mediforproto.FuseImageManipulationRequest)
  ))
_sym_db.RegisterMessage(FuseImageManipulationRequest)

AnnotatedVideoManipulation = _reflection.GeneratedProtocolMessageType('AnnotatedVideoManipulation', (_message.Message,), dict(
  DESCRIPTOR = _ANNOTATEDVIDEOMANIPULATION,
  __module__ = 'fusion_pb2'
  # @@protoc_insertion_point(class_scope:mediforproto.AnnotatedVideoManipulation)
  ))
_sym_db.RegisterMessage(AnnotatedVideoManipulation)

FuseVideoManipulationRequest = _reflection.GeneratedProtocolMessageType('FuseVideoManipulationRequest', (_message.Message,), dict(
  DESCRIPTOR = _FUSEVIDEOMANIPULATIONREQUEST,
  __module__ = 'fusion_pb2'
  # @@protoc_insertion_point(class_scope:mediforproto.FuseVideoManipulationRequest)
  ))
_sym_db.RegisterMessage(FuseVideoManipulationRequest)

AnnotatedImageSplice = _reflection.GeneratedProtocolMessageType('AnnotatedImageSplice', (_message.Message,), dict(
  DESCRIPTOR = _ANNOTATEDIMAGESPLICE,
  __module__ = 'fusion_pb2'
  # @@protoc_insertion_point(class_scope:mediforproto.AnnotatedImageSplice)
  ))
_sym_db.RegisterMessage(AnnotatedImageSplice)

FuseImageSpliceRequest = _reflection.GeneratedProtocolMessageType('FuseImageSpliceRequest', (_message.Message,), dict(
  DESCRIPTOR = _FUSEIMAGESPLICEREQUEST,
  __module__ = 'fusion_pb2'
  # @@protoc_insertion_point(class_scope:mediforproto.FuseImageSpliceRequest)
  ))
_sym_db.RegisterMessage(FuseImageSpliceRequest)

AnnotatedImageCameraMatch = _reflection.GeneratedProtocolMessageType('AnnotatedImageCameraMatch', (_message.Message,), dict(
  DESCRIPTOR = _ANNOTATEDIMAGECAMERAMATCH,
  __module__ = 'fusion_pb2'
  # @@protoc_insertion_point(class_scope:mediforproto.AnnotatedImageCameraMatch)
  ))
_sym_db.RegisterMessage(AnnotatedImageCameraMatch)

FuseImageCameraMatchRequest = _reflection.GeneratedProtocolMessageType('FuseImageCameraMatchRequest', (_message.Message,), dict(
  DESCRIPTOR = _FUSEIMAGECAMERAMATCHREQUEST,
  __module__ = 'fusion_pb2'
  # @@protoc_insertion_point(class_scope:mediforproto.FuseImageCameraMatchRequest)
  ))
_sym_db.RegisterMessage(FuseImageCameraMatchRequest)


DESCRIPTOR._options = None

_FUSER = _descriptor.ServiceDescriptor(
  name='Fuser',
  full_name='mediforproto.Fuser',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1937,
  serialized_end=2381,
  methods=[
  _descriptor.MethodDescriptor(
    name='FuseImageManipulation',
    full_name='mediforproto.Fuser.FuseImageManipulation',
    index=0,
    containing_service=None,
    input_type=_FUSEIMAGEMANIPULATIONREQUEST,
    output_type=analytic__pb2._IMAGEMANIPULATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FuseImageSplice',
    full_name='mediforproto.Fuser.FuseImageSplice',
    index=1,
    containing_service=None,
    input_type=_FUSEIMAGESPLICEREQUEST,
    output_type=analytic__pb2._IMAGESPLICE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FuseVideoManipulation',
    full_name='mediforproto.Fuser.FuseVideoManipulation',
    index=2,
    containing_service=None,
    input_type=_FUSEVIDEOMANIPULATIONREQUEST,
    output_type=analytic__pb2._VIDEOMANIPULATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FuseImageCameraMatch',
    full_name='mediforproto.Fuser.FuseImageCameraMatch',
    index=3,
    containing_service=None,
    input_type=_FUSEIMAGECAMERAMATCHREQUEST,
    output_type=analytic__pb2._IMAGECAMERAMATCH,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Kill',
    full_name='mediforproto.Fuser.Kill',
    index=4,
    containing_service=None,
    input_type=analytic__pb2._EMPTY,
    output_type=analytic__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FUSER)

DESCRIPTOR.services_by_name['Fuser'] = _FUSER

# @@protoc_insertion_point(module_scope)
