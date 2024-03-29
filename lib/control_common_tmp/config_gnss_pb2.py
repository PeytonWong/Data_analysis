# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config_gnss.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import map_projection_pb2 as map__projection__pb2
import geometry_pb2 as geometry__pb2
import stream_pb2 as stream__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='config_gnss.proto',
  package='car.proto',
  syntax='proto2',
  serialized_pb=_b('\n\x11\x63onfig_gnss.proto\x12\tcar.proto\x1a\x14map_projection.proto\x1a\x0egeometry.proto\x1a\x0cstream.proto\"\xf3\x01\n\x03Imu\x12!\n\x04type\x18\x01 \x01(\x0e\x32\x13.car.proto.Imu.Type\x12\x12\n\ngyro_scale\x18\x02 \x01(\x01\x12\x13\n\x0b\x61\x63\x63\x65l_scale\x18\x03 \x01(\x01\x12\x15\n\rsampling_rate\x18\x04 \x01(\x01\"\x88\x01\n\x04Type\x12\r\n\tXW_GI7660\x10\x00\x12\r\n\tIMAR_FSAS\x10\r\x12\x0b\n\x07ISA100C\x10\x1a\x12\r\n\tADIS16488\x10\x1f\x12\x0b\n\x07STIM300\x10 \x12\n\n\x06ISA100\x10\"\x12\x10\n\x0cISA100_400HZ\x10&\x12\x11\n\rISA100C_400HZ\x10\'\x12\x08\n\x04G320\x10)\"\x9b\x05\n\nConfigGnss\x12\x1f\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x11.car.proto.Stream\x12\"\n\x07\x63ommand\x18\x02 \x01(\x0b\x32\x11.car.proto.Stream\x12#\n\x08rtk_from\x18\x03 \x01(\x0b\x32\x11.car.proto.Stream\x12!\n\x06rtk_to\x18\x04 \x01(\x0b\x32\x11.car.proto.Stream\x12\x13\n\x0brtk_request\x18\x05 \x01(\x0c\x12\x16\n\x0elogin_commands\x18\x06 \x03(\x0c\x12\x17\n\x0flogout_commands\x18\x07 \x03(\x0c\x12/\n\x12vehicle_to_antenna\x18\x08 \x01(\x0b\x32\x13.car.proto.Vector3f\x12+\n\x0evehicle_to_imu\x18\t \x01(\x0b\x32\x13.car.proto.Vector3f\x12\x1b\n\x03imu\x18\n \x01(\x0b\x32\x0e.car.proto.Imu\x12,\n\nprojection\x18\x0b \x01(\x0b\x32\x18.car.proto.MapProjection\x12\x30\n\x07novatel\x18\x0c \x01(\x0b\x32\x1d.car.proto.ConfigGnss.NovatelH\x00\x12,\n\x05ublox\x18\r \x01(\x0b\x32\x1b.car.proto.ConfigGnss.UbloxH\x00\x12\x32\n\x08starneto\x18\x0e \x01(\x0b\x32\x1e.car.proto.ConfigGnss.StarnetoH\x00\x1a\x44\n\x07Novatel\x12\x1a\n\x0fimu_orientation\x18\x01 \x01(\x05:\x01\x35\x12\x1d\n\x10\x63orrimudata_rate\x18\x02 \x01(\x01:\x03\x32\x30\x30\x1a\x07\n\x05Ublox\x1a&\n\x08Starneto\x12\x1a\n\x0fimu_orientation\x18\x01 \x01(\x05:\x01\x35\x42\x06\n\x04type')
  ,
  dependencies=[map__projection__pb2.DESCRIPTOR,geometry__pb2.DESCRIPTOR,stream__pb2.DESCRIPTOR,])



_IMU_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='car.proto.Imu.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='XW_GI7660', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAR_FSAS', index=1, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISA100C', index=2, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADIS16488', index=3, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STIM300', index=4, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISA100', index=5, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISA100_400HZ', index=6, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISA100C_400HZ', index=7, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='G320', index=8, number=41,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=192,
  serialized_end=328,
)
_sym_db.RegisterEnumDescriptor(_IMU_TYPE)


_IMU = _descriptor.Descriptor(
  name='Imu',
  full_name='car.proto.Imu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='car.proto.Imu.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gyro_scale', full_name='car.proto.Imu.gyro_scale', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accel_scale', full_name='car.proto.Imu.accel_scale', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sampling_rate', full_name='car.proto.Imu.sampling_rate', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _IMU_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=328,
)


_CONFIGGNSS_NOVATEL = _descriptor.Descriptor(
  name='Novatel',
  full_name='car.proto.ConfigGnss.Novatel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='imu_orientation', full_name='car.proto.ConfigGnss.Novatel.imu_orientation', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='corrimudata_rate', full_name='car.proto.ConfigGnss.Novatel.corrimudata_rate', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(200),
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
  serialized_start=873,
  serialized_end=941,
)

_CONFIGGNSS_UBLOX = _descriptor.Descriptor(
  name='Ublox',
  full_name='car.proto.ConfigGnss.Ublox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=943,
  serialized_end=950,
)

_CONFIGGNSS_STARNETO = _descriptor.Descriptor(
  name='Starneto',
  full_name='car.proto.ConfigGnss.Starneto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='imu_orientation', full_name='car.proto.ConfigGnss.Starneto.imu_orientation', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=5,
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
  serialized_start=952,
  serialized_end=990,
)

_CONFIGGNSS = _descriptor.Descriptor(
  name='ConfigGnss',
  full_name='car.proto.ConfigGnss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='car.proto.ConfigGnss.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='car.proto.ConfigGnss.command', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rtk_from', full_name='car.proto.ConfigGnss.rtk_from', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rtk_to', full_name='car.proto.ConfigGnss.rtk_to', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rtk_request', full_name='car.proto.ConfigGnss.rtk_request', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='login_commands', full_name='car.proto.ConfigGnss.login_commands', index=5,
      number=6, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logout_commands', full_name='car.proto.ConfigGnss.logout_commands', index=6,
      number=7, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vehicle_to_antenna', full_name='car.proto.ConfigGnss.vehicle_to_antenna', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vehicle_to_imu', full_name='car.proto.ConfigGnss.vehicle_to_imu', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imu', full_name='car.proto.ConfigGnss.imu', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='projection', full_name='car.proto.ConfigGnss.projection', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='novatel', full_name='car.proto.ConfigGnss.novatel', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ublox', full_name='car.proto.ConfigGnss.ublox', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='starneto', full_name='car.proto.ConfigGnss.starneto', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONFIGGNSS_NOVATEL, _CONFIGGNSS_UBLOX, _CONFIGGNSS_STARNETO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='car.proto.ConfigGnss.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=331,
  serialized_end=998,
)

_IMU.fields_by_name['type'].enum_type = _IMU_TYPE
_IMU_TYPE.containing_type = _IMU
_CONFIGGNSS_NOVATEL.containing_type = _CONFIGGNSS
_CONFIGGNSS_UBLOX.containing_type = _CONFIGGNSS
_CONFIGGNSS_STARNETO.containing_type = _CONFIGGNSS
_CONFIGGNSS.fields_by_name['data'].message_type = stream__pb2._STREAM
_CONFIGGNSS.fields_by_name['command'].message_type = stream__pb2._STREAM
_CONFIGGNSS.fields_by_name['rtk_from'].message_type = stream__pb2._STREAM
_CONFIGGNSS.fields_by_name['rtk_to'].message_type = stream__pb2._STREAM
_CONFIGGNSS.fields_by_name['vehicle_to_antenna'].message_type = geometry__pb2._VECTOR3F
_CONFIGGNSS.fields_by_name['vehicle_to_imu'].message_type = geometry__pb2._VECTOR3F
_CONFIGGNSS.fields_by_name['imu'].message_type = _IMU
_CONFIGGNSS.fields_by_name['projection'].message_type = map__projection__pb2._MAPPROJECTION
_CONFIGGNSS.fields_by_name['novatel'].message_type = _CONFIGGNSS_NOVATEL
_CONFIGGNSS.fields_by_name['ublox'].message_type = _CONFIGGNSS_UBLOX
_CONFIGGNSS.fields_by_name['starneto'].message_type = _CONFIGGNSS_STARNETO
_CONFIGGNSS.oneofs_by_name['type'].fields.append(
  _CONFIGGNSS.fields_by_name['novatel'])
_CONFIGGNSS.fields_by_name['novatel'].containing_oneof = _CONFIGGNSS.oneofs_by_name['type']
_CONFIGGNSS.oneofs_by_name['type'].fields.append(
  _CONFIGGNSS.fields_by_name['ublox'])
_CONFIGGNSS.fields_by_name['ublox'].containing_oneof = _CONFIGGNSS.oneofs_by_name['type']
_CONFIGGNSS.oneofs_by_name['type'].fields.append(
  _CONFIGGNSS.fields_by_name['starneto'])
_CONFIGGNSS.fields_by_name['starneto'].containing_oneof = _CONFIGGNSS.oneofs_by_name['type']
DESCRIPTOR.message_types_by_name['Imu'] = _IMU
DESCRIPTOR.message_types_by_name['ConfigGnss'] = _CONFIGGNSS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Imu = _reflection.GeneratedProtocolMessageType('Imu', (_message.Message,), dict(
  DESCRIPTOR = _IMU,
  __module__ = 'config_gnss_pb2'
  # @@protoc_insertion_point(class_scope:car.proto.Imu)
  ))
_sym_db.RegisterMessage(Imu)

ConfigGnss = _reflection.GeneratedProtocolMessageType('ConfigGnss', (_message.Message,), dict(

  Novatel = _reflection.GeneratedProtocolMessageType('Novatel', (_message.Message,), dict(
    DESCRIPTOR = _CONFIGGNSS_NOVATEL,
    __module__ = 'config_gnss_pb2'
    # @@protoc_insertion_point(class_scope:car.proto.ConfigGnss.Novatel)
    ))
  ,

  Ublox = _reflection.GeneratedProtocolMessageType('Ublox', (_message.Message,), dict(
    DESCRIPTOR = _CONFIGGNSS_UBLOX,
    __module__ = 'config_gnss_pb2'
    # @@protoc_insertion_point(class_scope:car.proto.ConfigGnss.Ublox)
    ))
  ,

  Starneto = _reflection.GeneratedProtocolMessageType('Starneto', (_message.Message,), dict(
    DESCRIPTOR = _CONFIGGNSS_STARNETO,
    __module__ = 'config_gnss_pb2'
    # @@protoc_insertion_point(class_scope:car.proto.ConfigGnss.Starneto)
    ))
  ,
  DESCRIPTOR = _CONFIGGNSS,
  __module__ = 'config_gnss_pb2'
  # @@protoc_insertion_point(class_scope:car.proto.ConfigGnss)
  ))
_sym_db.RegisterMessage(ConfigGnss)
_sym_db.RegisterMessage(ConfigGnss.Novatel)
_sym_db.RegisterMessage(ConfigGnss.Ublox)
_sym_db.RegisterMessage(ConfigGnss.Starneto)


# @@protoc_insertion_point(module_scope)
