# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: control_trace.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='control_trace.proto',
  package='car.proto',
  syntax='proto2',
  serialized_pb=_b('\n\x13\x63ontrol_trace.proto\x12\tcar.proto\"<\n\x0c\x43ontrolTrace\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x0f\n\x07time_ms\x18\x03 \x01(\r')
)




_CONTROLTRACE = _descriptor.Descriptor(
  name='ControlTrace',
  full_name='car.proto.ControlTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='car.proto.ControlTrace.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='car.proto.ControlTrace.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_ms', full_name='car.proto.ControlTrace.time_ms', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['ControlTrace'] = _CONTROLTRACE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ControlTrace = _reflection.GeneratedProtocolMessageType('ControlTrace', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLTRACE,
  __module__ = 'control_trace_pb2'
  # @@protoc_insertion_point(class_scope:car.proto.ControlTrace)
  ))
_sym_db.RegisterMessage(ControlTrace)


# @@protoc_insertion_point(module_scope)
