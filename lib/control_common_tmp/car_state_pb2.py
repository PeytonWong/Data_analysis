# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: car_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import geometry_pb2 as geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='car_state.proto',
  package='car.proto',
  syntax='proto2',
  serialized_pb=_b('\n\x0f\x63\x61r_state.proto\x12\tcar.proto\x1a\x0egeometry.proto\"\xa0\x07\n\x08\x43\x61rState\x12\x11\n\ttime_meas\x18\x01 \x01(\x10\x12%\n\x08position\x18\x02 \x01(\x0b\x32\x13.car.proto.Vector3f\x12)\n\x0cvelocity_enu\x18\x03 \x01(\x0b\x32\x13.car.proto.Vector3f\x12)\n\x0cvelocity_flu\x18\x04 \x01(\x0b\x32\x13.car.proto.Vector3f\x12+\n\x0eroll_pitch_yaw\x18\x05 \x01(\x0b\x32\x13.car.proto.Vector3f\x12\x31\n\x14\x61ngular_velocity_flu\x18\x06 \x01(\x0b\x32\x13.car.proto.Vector3f\x12-\n\x10\x61\x63\x63\x65leration_flu\x18\x07 \x01(\x0b\x32\x13.car.proto.Vector3f\x12\x19\n\x11\x66ront_wheel_angle\x18\x08 \x01(\x02\x12\r\n\x05speed\x18\t \x01(\x02\x12\x33\n\x0bturn_signal\x18\n \x01(\x0e\x32\x1e.car.proto.CarState.TurnSignal\x12\x1a\n\x12warning_blinker_on\x18\x0b \x01(\x08\x12,\n\x04gear\x18\x0c \x01(\x0e\x32\x1e.car.proto.CarState.GearStatus\x12\x35\n\x0c\x64riving_mode\x18\r \x01(\x0e\x32\x1f.car.proto.CarState.DrivingMode\x12\x14\n\x0clongitudinal\x18\x0e \x01(\x02\x12\x17\n\x0f\x61\x63\x63_over_ground\x18\x0f \x01(\x02\x12@\n\x12hazard_ctrl_signal\x18\x10 \x01(\x0e\x32$.car.proto.CarState.HazardCtrlSignal\"0\n\nTurnSignal\x12\r\n\tNONE_TURN\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\"b\n\nGearStatus\x12\x0b\n\x07INVALID\x10\x00\x12\x08\n\x04PARK\x10\x01\x12\x0b\n\x07REVERSE\x10\x02\x12\x0b\n\x07NEUTRAL\x10\x03\x12\t\n\x05\x44RIVE\x10\x04\x12\x07\n\x03LOW\x10\x05\x12\x0f\n\x0bUNSPECIFIED\x10\x06\"U\n\x0b\x44rivingMode\x12\n\n\x06MANUAL\x10\x00\x12\x15\n\x11LONGITUDINAL_AUTO\x10\x01\x12\x10\n\x0cLATERAL_AUTO\x10\x02\x12\x08\n\x04\x41UTO\x10\x03\x12\x07\n\x03\x41\x45\x42\x10\x07\"7\n\x10HazardCtrlSignal\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06\x43LOSED\x10\x01\x12\x08\n\x04OPEN\x10\x02')
  ,
  dependencies=[geometry__pb2.DESCRIPTOR,])



_CARSTATE_TURNSIGNAL = _descriptor.EnumDescriptor(
  name='TurnSignal',
  full_name='car.proto.CarState.TurnSignal',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE_TURN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=683,
  serialized_end=731,
)
_sym_db.RegisterEnumDescriptor(_CARSTATE_TURNSIGNAL)

_CARSTATE_GEARSTATUS = _descriptor.EnumDescriptor(
  name='GearStatus',
  full_name='car.proto.CarState.GearStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVERSE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEUTRAL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRIVE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=733,
  serialized_end=831,
)
_sym_db.RegisterEnumDescriptor(_CARSTATE_GEARSTATUS)

_CARSTATE_DRIVINGMODE = _descriptor.EnumDescriptor(
  name='DrivingMode',
  full_name='car.proto.CarState.DrivingMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MANUAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LONGITUDINAL_AUTO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LATERAL_AUTO', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTO', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AEB', index=4, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=833,
  serialized_end=918,
)
_sym_db.RegisterEnumDescriptor(_CARSTATE_DRIVINGMODE)

_CARSTATE_HAZARDCTRLSIGNAL = _descriptor.EnumDescriptor(
  name='HazardCtrlSignal',
  full_name='car.proto.CarState.HazardCtrlSignal',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=920,
  serialized_end=975,
)
_sym_db.RegisterEnumDescriptor(_CARSTATE_HAZARDCTRLSIGNAL)


_CARSTATE = _descriptor.Descriptor(
  name='CarState',
  full_name='car.proto.CarState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_meas', full_name='car.proto.CarState.time_meas', index=0,
      number=1, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='car.proto.CarState.position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity_enu', full_name='car.proto.CarState.velocity_enu', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity_flu', full_name='car.proto.CarState.velocity_flu', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roll_pitch_yaw', full_name='car.proto.CarState.roll_pitch_yaw', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_velocity_flu', full_name='car.proto.CarState.angular_velocity_flu', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acceleration_flu', full_name='car.proto.CarState.acceleration_flu', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='front_wheel_angle', full_name='car.proto.CarState.front_wheel_angle', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed', full_name='car.proto.CarState.speed', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='turn_signal', full_name='car.proto.CarState.turn_signal', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warning_blinker_on', full_name='car.proto.CarState.warning_blinker_on', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gear', full_name='car.proto.CarState.gear', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='driving_mode', full_name='car.proto.CarState.driving_mode', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitudinal', full_name='car.proto.CarState.longitudinal', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acc_over_ground', full_name='car.proto.CarState.acc_over_ground', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hazard_ctrl_signal', full_name='car.proto.CarState.hazard_ctrl_signal', index=15,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CARSTATE_TURNSIGNAL,
    _CARSTATE_GEARSTATUS,
    _CARSTATE_DRIVINGMODE,
    _CARSTATE_HAZARDCTRLSIGNAL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=975,
)

_CARSTATE.fields_by_name['position'].message_type = geometry__pb2._VECTOR3F
_CARSTATE.fields_by_name['velocity_enu'].message_type = geometry__pb2._VECTOR3F
_CARSTATE.fields_by_name['velocity_flu'].message_type = geometry__pb2._VECTOR3F
_CARSTATE.fields_by_name['roll_pitch_yaw'].message_type = geometry__pb2._VECTOR3F
_CARSTATE.fields_by_name['angular_velocity_flu'].message_type = geometry__pb2._VECTOR3F
_CARSTATE.fields_by_name['acceleration_flu'].message_type = geometry__pb2._VECTOR3F
_CARSTATE.fields_by_name['turn_signal'].enum_type = _CARSTATE_TURNSIGNAL
_CARSTATE.fields_by_name['gear'].enum_type = _CARSTATE_GEARSTATUS
_CARSTATE.fields_by_name['driving_mode'].enum_type = _CARSTATE_DRIVINGMODE
_CARSTATE.fields_by_name['hazard_ctrl_signal'].enum_type = _CARSTATE_HAZARDCTRLSIGNAL
_CARSTATE_TURNSIGNAL.containing_type = _CARSTATE
_CARSTATE_GEARSTATUS.containing_type = _CARSTATE
_CARSTATE_DRIVINGMODE.containing_type = _CARSTATE
_CARSTATE_HAZARDCTRLSIGNAL.containing_type = _CARSTATE
DESCRIPTOR.message_types_by_name['CarState'] = _CARSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CarState = _reflection.GeneratedProtocolMessageType('CarState', (_message.Message,), dict(
  DESCRIPTOR = _CARSTATE,
  __module__ = 'car_state_pb2'
  # @@protoc_insertion_point(class_scope:car.proto.CarState)
  ))
_sym_db.RegisterMessage(CarState)


# @@protoc_insertion_point(module_scope)
