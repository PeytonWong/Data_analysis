# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from control_common_tmp/Imu.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Imu(genpy.Message):
  _md5sum = "e98b4fc498ae167206a86ecc843a6650"
  _type = "control_common_tmp/Imu"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
# Vehicle reference point (VRP) is at center of rear axle.

# When this message was published. In microseconds.
int64 time_pub

# When the measurements were made. In microseconds.
int64 time_meas

# GPS time of the measurements. In microseconds.
int64 time_gps

# When duration is non-zero, the gyroscope and accelerometer measurements are averaged for the
# period from (time_meas - duration) to time_meas. Usually, duration = 1 / sampling_frequency.
# When duration is 0, the measurements are instantaneous at time_meas.
uint32 duration  # in microseconds

float32[3] angular_velocity_flu  # in rad/s

float32[3] acceleration_flu  # in m/s^2

bool healthy
"""
  __slots__ = ['time_pub','time_meas','time_gps','duration','angular_velocity_flu','acceleration_flu','healthy']
  _slot_types = ['int64','int64','int64','uint32','float32[3]','float32[3]','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       time_pub,time_meas,time_gps,duration,angular_velocity_flu,acceleration_flu,healthy

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Imu, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.time_pub is None:
        self.time_pub = 0
      if self.time_meas is None:
        self.time_meas = 0
      if self.time_gps is None:
        self.time_gps = 0
      if self.duration is None:
        self.duration = 0
      if self.angular_velocity_flu is None:
        self.angular_velocity_flu = [0.] * 3
      if self.acceleration_flu is None:
        self.acceleration_flu = [0.] * 3
      if self.healthy is None:
        self.healthy = False
    else:
      self.time_pub = 0
      self.time_meas = 0
      self.time_gps = 0
      self.duration = 0
      self.angular_velocity_flu = [0.] * 3
      self.acceleration_flu = [0.] * 3
      self.healthy = False

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
      buff.write(_get_struct_3qI().pack(_x.time_pub, _x.time_meas, _x.time_gps, _x.duration))
      buff.write(_get_struct_3f().pack(*self.angular_velocity_flu))
      buff.write(_get_struct_3f().pack(*self.acceleration_flu))
      buff.write(_get_struct_B().pack(self.healthy))
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
      end += 28
      (_x.time_pub, _x.time_meas, _x.time_gps, _x.duration,) = _get_struct_3qI().unpack(str[start:end])
      start = end
      end += 12
      self.angular_velocity_flu = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.acceleration_flu = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 1
      (self.healthy,) = _get_struct_B().unpack(str[start:end])
      self.healthy = bool(self.healthy)
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
      buff.write(_get_struct_3qI().pack(_x.time_pub, _x.time_meas, _x.time_gps, _x.duration))
      buff.write(self.angular_velocity_flu.tostring())
      buff.write(self.acceleration_flu.tostring())
      buff.write(_get_struct_B().pack(self.healthy))
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
      end += 28
      (_x.time_pub, _x.time_meas, _x.time_gps, _x.duration,) = _get_struct_3qI().unpack(str[start:end])
      start = end
      end += 12
      self.angular_velocity_flu = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.acceleration_flu = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 1
      (self.healthy,) = _get_struct_B().unpack(str[start:end])
      self.healthy = bool(self.healthy)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3qI = None
def _get_struct_3qI():
    global _struct_3qI
    if _struct_3qI is None:
        _struct_3qI = struct.Struct("<3qI")
    return _struct_3qI
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f