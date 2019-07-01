# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from control_common_tmp/WheelSpeed.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class WheelSpeed(genpy.Message):
  _md5sum = "fbf78b57038447ad11ee627be14e9735"
  _type = "control_common_tmp/WheelSpeed"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """

# Message publishing time in microseconds.
int64 time_pub

# Measure time from canbus. In microseconds.
int64 time_meas


# Wheel speeds (rad/s)
float32 front_left
float32 front_right
float32 rear_left
float32 rear_right


"""
  __slots__ = ['time_pub','time_meas','front_left','front_right','rear_left','rear_right']
  _slot_types = ['int64','int64','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       time_pub,time_meas,front_left,front_right,rear_left,rear_right

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(WheelSpeed, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.time_pub is None:
        self.time_pub = 0
      if self.time_meas is None:
        self.time_meas = 0
      if self.front_left is None:
        self.front_left = 0.
      if self.front_right is None:
        self.front_right = 0.
      if self.rear_left is None:
        self.rear_left = 0.
      if self.rear_right is None:
        self.rear_right = 0.
    else:
      self.time_pub = 0
      self.time_meas = 0
      self.front_left = 0.
      self.front_right = 0.
      self.rear_left = 0.
      self.rear_right = 0.

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
      buff.write(_get_struct_2q4f().pack(_x.time_pub, _x.time_meas, _x.front_left, _x.front_right, _x.rear_left, _x.rear_right))
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
      end += 32
      (_x.time_pub, _x.time_meas, _x.front_left, _x.front_right, _x.rear_left, _x.rear_right,) = _get_struct_2q4f().unpack(str[start:end])
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
      buff.write(_get_struct_2q4f().pack(_x.time_pub, _x.time_meas, _x.front_left, _x.front_right, _x.rear_left, _x.rear_right))
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
      end += 32
      (_x.time_pub, _x.time_meas, _x.front_left, _x.front_right, _x.rear_left, _x.rear_right,) = _get_struct_2q4f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2q4f = None
def _get_struct_2q4f():
    global _struct_2q4f
    if _struct_2q4f is None:
        _struct_2q4f = struct.Struct("<2q4f")
    return _struct_2q4f
