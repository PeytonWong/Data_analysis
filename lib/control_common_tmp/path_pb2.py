# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: path.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import car_state_pb2 as car__state__pb2
import geometry_pb2 as geometry__pb2
import perception_object_pb2 as perception__object__pb2
import decision_pb2 as decision__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='path.proto',
  package='car.proto',
  syntax='proto2',
  serialized_pb=_b('\n\npath.proto\x12\tcar.proto\x1a\x0f\x63\x61r_state.proto\x1a\x0egeometry.proto\x1a\x17perception_object.proto\x1a\x0e\x64\x65\x63ision.proto\"p\n\x0fTrajectoryPoint\x12\x15\n\rtime_relative\x18\x0c \x01(\x02\x12\x12\n\ns_relative\x18\r \x01(\x02\x12\x15\n\rspeed_by_time\x18\x0e \x01(\x02\x12\x1b\n\x13speed_limit_by_time\x18\x0f \x01(\x02\"\xcf\x01\n\tPathPoint\x12%\n\x08position\x18\x01 \x01(\x0b\x32\x13.car.proto.Vector3f\x12\t\n\x01k\x18\x02 \x01(\x02\x12\r\n\x05theta\x18\x03 \x01(\x02\x12\t\n\x01s\x18\x04 \x01(\x02\x12\t\n\x01l\x18\x05 \x01(\x02\x12\r\n\x05speed\x18\x06 \x01(\x02\x12\x13\n\x0bspeed_limit\x18\x07 \x01(\x02\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x08 \x01(\x02\x12\x18\n\x10\x62\x61\x63kward_driving\x18\t \x01(\x08\x12\n\n\x02\x64l\x18\n \x01(\x02\x12\x0b\n\x03\x64\x64l\x18\x0b \x01(\x02\"\xce\x02\n\x04Path\x12\x11\n\ttime_meas\x18\x01 \x01(\x10\x12)\n\x0bpath_points\x18\x02 \x03(\x0b\x32\x14.car.proto.PathPoint\x12\x33\n\x0bturn_signal\x18\x03 \x01(\x0e\x32\x1e.car.proto.CarState.TurnSignal\x12@\n\x12hazard_ctrl_signal\x18\x04 \x01(\x0e\x32$.car.proto.CarState.HazardCtrlSignal\x12\x31\n\x0clead_vehicle\x18\x05 \x01(\x0b\x32\x1b.car.proto.PerceptionObject\x12.\n\rdecision_main\x18\x06 \x01(\x0b\x32\x17.car.proto.DecisionMain\x12.\n\ntrajectory\x18\x07 \x03(\x0b\x32\x1a.car.proto.TrajectoryPoint\"(\n\x06Routes\x12\x1e\n\x05paths\x18\x01 \x03(\x0b\x32\x0f.car.proto.Path\"L\n\nSLBoundary\x12\x0f\n\x07start_s\x18\x01 \x01(\x01\x12\r\n\x05\x65nd_s\x18\x02 \x01(\x01\x12\x0f\n\x07start_l\x18\x03 \x01(\x01\x12\r\n\x05\x65nd_l\x18\x04 \x01(\x01')
  ,
  dependencies=[car__state__pb2.DESCRIPTOR,geometry__pb2.DESCRIPTOR,perception__object__pb2.DESCRIPTOR,decision__pb2.DESCRIPTOR,])




_TRAJECTORYPOINT = _descriptor.Descriptor(
  name='TrajectoryPoint',
  full_name='car.proto.TrajectoryPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_relative', full_name='car.proto.TrajectoryPoint.time_relative', index=0,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s_relative', full_name='car.proto.TrajectoryPoint.s_relative', index=1,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed_by_time', full_name='car.proto.TrajectoryPoint.speed_by_time', index=2,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed_limit_by_time', full_name='car.proto.TrajectoryPoint.speed_limit_by_time', index=3,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=99,
  serialized_end=211,
)


_PATHPOINT = _descriptor.Descriptor(
  name='PathPoint',
  full_name='car.proto.PathPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='car.proto.PathPoint.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k', full_name='car.proto.PathPoint.k', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='theta', full_name='car.proto.PathPoint.theta', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s', full_name='car.proto.PathPoint.s', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l', full_name='car.proto.PathPoint.l', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed', full_name='car.proto.PathPoint.speed', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed_limit', full_name='car.proto.PathPoint.speed_limit', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='car.proto.PathPoint.acceleration', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backward_driving', full_name='car.proto.PathPoint.backward_driving', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dl', full_name='car.proto.PathPoint.dl', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ddl', full_name='car.proto.PathPoint.ddl', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=214,
  serialized_end=421,
)


_PATH = _descriptor.Descriptor(
  name='Path',
  full_name='car.proto.Path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_meas', full_name='car.proto.Path.time_meas', index=0,
      number=1, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path_points', full_name='car.proto.Path.path_points', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='turn_signal', full_name='car.proto.Path.turn_signal', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hazard_ctrl_signal', full_name='car.proto.Path.hazard_ctrl_signal', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lead_vehicle', full_name='car.proto.Path.lead_vehicle', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decision_main', full_name='car.proto.Path.decision_main', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trajectory', full_name='car.proto.Path.trajectory', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=424,
  serialized_end=758,
)


_ROUTES = _descriptor.Descriptor(
  name='Routes',
  full_name='car.proto.Routes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paths', full_name='car.proto.Routes.paths', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=760,
  serialized_end=800,
)


_SLBOUNDARY = _descriptor.Descriptor(
  name='SLBoundary',
  full_name='car.proto.SLBoundary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_s', full_name='car.proto.SLBoundary.start_s', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_s', full_name='car.proto.SLBoundary.end_s', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_l', full_name='car.proto.SLBoundary.start_l', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_l', full_name='car.proto.SLBoundary.end_l', index=3,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=802,
  serialized_end=878,
)

_PATHPOINT.fields_by_name['position'].message_type = geometry__pb2._VECTOR3F
_PATH.fields_by_name['path_points'].message_type = _PATHPOINT
_PATH.fields_by_name['turn_signal'].enum_type = car__state__pb2._CARSTATE_TURNSIGNAL
_PATH.fields_by_name['hazard_ctrl_signal'].enum_type = car__state__pb2._CARSTATE_HAZARDCTRLSIGNAL
_PATH.fields_by_name['lead_vehicle'].message_type = perception__object__pb2._PERCEPTIONOBJECT
_PATH.fields_by_name['decision_main'].message_type = decision__pb2._DECISIONMAIN
_PATH.fields_by_name['trajectory'].message_type = _TRAJECTORYPOINT
_ROUTES.fields_by_name['paths'].message_type = _PATH
DESCRIPTOR.message_types_by_name['TrajectoryPoint'] = _TRAJECTORYPOINT
DESCRIPTOR.message_types_by_name['PathPoint'] = _PATHPOINT
DESCRIPTOR.message_types_by_name['Path'] = _PATH
DESCRIPTOR.message_types_by_name['Routes'] = _ROUTES
DESCRIPTOR.message_types_by_name['SLBoundary'] = _SLBOUNDARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrajectoryPoint = _reflection.GeneratedProtocolMessageType('TrajectoryPoint', (_message.Message,), dict(
  DESCRIPTOR = _TRAJECTORYPOINT,
  __module__ = 'path_pb2'
  # @@protoc_insertion_point(class_scope:car.proto.TrajectoryPoint)
  ))
_sym_db.RegisterMessage(TrajectoryPoint)

PathPoint = _reflection.GeneratedProtocolMessageType('PathPoint', (_message.Message,), dict(
  DESCRIPTOR = _PATHPOINT,
  __module__ = 'path_pb2'
  # @@protoc_insertion_point(class_scope:car.proto.PathPoint)
  ))
_sym_db.RegisterMessage(PathPoint)

Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), dict(
  DESCRIPTOR = _PATH,
  __module__ = 'path_pb2'
  # @@protoc_insertion_point(class_scope:car.proto.Path)
  ))
_sym_db.RegisterMessage(Path)

Routes = _reflection.GeneratedProtocolMessageType('Routes', (_message.Message,), dict(
  DESCRIPTOR = _ROUTES,
  __module__ = 'path_pb2'
  # @@protoc_insertion_point(class_scope:car.proto.Routes)
  ))
_sym_db.RegisterMessage(Routes)

SLBoundary = _reflection.GeneratedProtocolMessageType('SLBoundary', (_message.Message,), dict(
  DESCRIPTOR = _SLBOUNDARY,
  __module__ = 'path_pb2'
  # @@protoc_insertion_point(class_scope:car.proto.SLBoundary)
  ))
_sym_db.RegisterMessage(SLBoundary)


# @@protoc_insertion_point(module_scope)