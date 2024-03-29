# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from control_common_tmp/Pose.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Pose(genpy.Message):
  _md5sum = "fd4f63fedf36d874a1f5095980d2a348"
  _type = "control_common_tmp/Pose"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """ 

# Vehicle reference point (VRP) is at center of rear axle.

# When this message was published. In microseconds.
int64 time_pub

# When the measurements were made. In microseconds.
int64 time_meas

# GPS time of the measurements. In microseconds.
int64 time_gps

# East/north/up with respect to the map origin.
# Horizontal offsets x and y are 0 if VRP is right at the map origin.
# Height z is with respect to WGS-84 ellipsoid.
float32[3] position  # in meters

# Euler angles (intrinsic sequence z-y-x).
# Yaw is 0 when the car points to east, and is pi/2 when the car points to north.
float32[3] roll_pitch_yaw  # in rad

float32[3] velocity_enu  # in m/s

float32[3] velocity_flu  # in m/s

float32[3] angular_velocity_flu  # in rad/s

float32[3] acceleration_flu  # in m/s^2

# Standard deviation estimates.
float32[3] position_std  # in meters

float32[3] roll_pitch_yaw_std  # in rad

float32[3] velocity_enu_std  # in m/s

# Invalid solution. Do NOT use.
int8 TYPE_INVALID = 0

# High-variance solution, in which the covariance matrix may be incorrect. Use with caution.
int8 TYPE_CONVERGING = 1

# Fully converged solution. Safe to use.
int8 TYPE_GOOD = 2

int8 type
"""
  # Pseudo-constants
  TYPE_INVALID = 0
  TYPE_CONVERGING = 1
  TYPE_GOOD = 2

  __slots__ = ['time_pub','time_meas','time_gps','position','roll_pitch_yaw','velocity_enu','velocity_flu','angular_velocity_flu','acceleration_flu','position_std','roll_pitch_yaw_std','velocity_enu_std','type']
  _slot_types = ['int64','int64','int64','float32[3]','float32[3]','float32[3]','float32[3]','float32[3]','float32[3]','float32[3]','float32[3]','float32[3]','int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       time_pub,time_meas,time_gps,position,roll_pitch_yaw,velocity_enu,velocity_flu,angular_velocity_flu,acceleration_flu,position_std,roll_pitch_yaw_std,velocity_enu_std,type

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Pose, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.time_pub is None:
        self.time_pub = 0
      if self.time_meas is None:
        self.time_meas = 0
      if self.time_gps is None:
        self.time_gps = 0
      if self.position is None:
        self.position = [0.] * 3
      if self.roll_pitch_yaw is None:
        self.roll_pitch_yaw = [0.] * 3
      if self.velocity_enu is None:
        self.velocity_enu = [0.] * 3
      if self.velocity_flu is None:
        self.velocity_flu = [0.] * 3
      if self.angular_velocity_flu is None:
        self.angular_velocity_flu = [0.] * 3
      if self.acceleration_flu is None:
        self.acceleration_flu = [0.] * 3
      if self.position_std is None:
        self.position_std = [0.] * 3
      if self.roll_pitch_yaw_std is None:
        self.roll_pitch_yaw_std = [0.] * 3
      if self.velocity_enu_std is None:
        self.velocity_enu_std = [0.] * 3
      if self.type is None:
        self.type = 0
    else:
      self.time_pub = 0
      self.time_meas = 0
      self.time_gps = 0
      self.position = [0.] * 3
      self.roll_pitch_yaw = [0.] * 3
      self.velocity_enu = [0.] * 3
      self.velocity_flu = [0.] * 3
      self.angular_velocity_flu = [0.] * 3
      self.acceleration_flu = [0.] * 3
      self.position_std = [0.] * 3
      self.roll_pitch_yaw_std = [0.] * 3
      self.velocity_enu_std = [0.] * 3
      self.type = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3q().pack(_x.time_pub, _x.time_meas, _x.time_gps))
      buff.write(_get_struct_3f().pack(*self.position))
      buff.write(_get_struct_3f().pack(*self.roll_pitch_yaw))
      buff.write(_get_struct_3f().pack(*self.velocity_enu))
      buff.write(_get_struct_3f().pack(*self.velocity_flu))
      buff.write(_get_struct_3f().pack(*self.angular_velocity_flu))
      buff.write(_get_struct_3f().pack(*self.acceleration_flu))
      buff.write(_get_struct_3f().pack(*self.position_std))
      buff.write(_get_struct_3f().pack(*self.roll_pitch_yaw_std))
      buff.write(_get_struct_3f().pack(*self.velocity_enu_std))
      buff.write(_get_struct_b().pack(self.type))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.time_pub, _x.time_meas, _x.time_gps,) = _get_struct_3q().unpack(str[start:end])
      start = end
      end += 12
      self.position = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.roll_pitch_yaw = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.velocity_enu = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.velocity_flu = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.angular_velocity_flu = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.acceleration_flu = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.position_std = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.roll_pitch_yaw_std = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.velocity_enu_std = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 1
      (self.type,) = _get_struct_b().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3q().pack(_x.time_pub, _x.time_meas, _x.time_gps))
      buff.write(self.position.tostring())
      buff.write(self.roll_pitch_yaw.tostring())
      buff.write(self.velocity_enu.tostring())
      buff.write(self.velocity_flu.tostring())
      buff.write(self.angular_velocity_flu.tostring())
      buff.write(self.acceleration_flu.tostring())
      buff.write(self.position_std.tostring())
      buff.write(self.roll_pitch_yaw_std.tostring())
      buff.write(self.velocity_enu_std.tostring())
      buff.write(_get_struct_b().pack(self.type))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.time_pub, _x.time_meas, _x.time_gps,) = _get_struct_3q().unpack(str[start:end])
      start = end
      end += 12
      self.position = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.roll_pitch_yaw = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.velocity_enu = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.velocity_flu = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.angular_velocity_flu = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.acceleration_flu = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.position_std = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.roll_pitch_yaw_std = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.velocity_enu_std = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 1
      (self.type,) = _get_struct_b().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3q = None
def _get_struct_3q():
    global _struct_3q
    if _struct_3q is None:
        _struct_3q = struct.Struct("<3q")
    return _struct_3q
_struct_b = None
def _get_struct_b():
    global _struct_b
    if _struct_b is None:
        _struct_b = struct.Struct("<b")
    return _struct_b
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
