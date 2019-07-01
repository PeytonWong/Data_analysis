# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from control_common_tmp/Gnss.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Gnss(genpy.Message):
  _md5sum = "517651e0a1d09e05546d5af9c1d55e82"
  _type = "control_common_tmp/Gnss"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
# Vehicle reference point (VRP) is at center of rear axle.

# When this message was published. In microseconds.
int64 time_pub

# When the measurements were made. In microseconds.
int64 time_meas

# GPS time of the measurements. In microseconds.
int64 time_gps

# Position of antenna phase center.
float64 longitude_deg
float64 latitude_deg
float32 height  # meters above the WGS-84 ellipsoid

# Standard deviation is in meters.
float32 east_std
float32 north_std
float32 up_std

float32 differential_age  # in seconds
float32 solution_age  # in seconds

uint8 num_sats_tracked
uint8 num_sats_in_solution

bool solution_computed

int8 TYPE_INVALID = 0
int8 TYPE_PROPAGATED = 1  # Propagated by a Kalman filter without new observations
int8 TYPE_SPS = 2  # Standard Positioning Service (SPS) without any correction
int8 TYPE_PSRDIFF = 3  # Pseudorange differential solution, including WAAS/SBAS solution
int8 TYPE_PPP = 4  # Precise Point Positioning (PPP) solution
int8 TYPE_RTK_FLOAT = 5  # Real Time Kinematic (RTK) float solution
int8 TYPE_RTK_INTEGER= 6  # RTK integer solution

int8 type
"""
  # Pseudo-constants
  TYPE_INVALID = 0
  TYPE_PROPAGATED = 1
  TYPE_SPS = 2
  TYPE_PSRDIFF = 3
  TYPE_PPP = 4
  TYPE_RTK_FLOAT = 5
  TYPE_RTK_INTEGER = 6

  __slots__ = ['time_pub','time_meas','time_gps','longitude_deg','latitude_deg','height','east_std','north_std','up_std','differential_age','solution_age','num_sats_tracked','num_sats_in_solution','solution_computed','type']
  _slot_types = ['int64','int64','int64','float64','float64','float32','float32','float32','float32','float32','float32','uint8','uint8','bool','int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       time_pub,time_meas,time_gps,longitude_deg,latitude_deg,height,east_std,north_std,up_std,differential_age,solution_age,num_sats_tracked,num_sats_in_solution,solution_computed,type

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Gnss, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.time_pub is None:
        self.time_pub = 0
      if self.time_meas is None:
        self.time_meas = 0
      if self.time_gps is None:
        self.time_gps = 0
      if self.longitude_deg is None:
        self.longitude_deg = 0.
      if self.latitude_deg is None:
        self.latitude_deg = 0.
      if self.height is None:
        self.height = 0.
      if self.east_std is None:
        self.east_std = 0.
      if self.north_std is None:
        self.north_std = 0.
      if self.up_std is None:
        self.up_std = 0.
      if self.differential_age is None:
        self.differential_age = 0.
      if self.solution_age is None:
        self.solution_age = 0.
      if self.num_sats_tracked is None:
        self.num_sats_tracked = 0
      if self.num_sats_in_solution is None:
        self.num_sats_in_solution = 0
      if self.solution_computed is None:
        self.solution_computed = False
      if self.type is None:
        self.type = 0
    else:
      self.time_pub = 0
      self.time_meas = 0
      self.time_gps = 0
      self.longitude_deg = 0.
      self.latitude_deg = 0.
      self.height = 0.
      self.east_std = 0.
      self.north_std = 0.
      self.up_std = 0.
      self.differential_age = 0.
      self.solution_age = 0.
      self.num_sats_tracked = 0
      self.num_sats_in_solution = 0
      self.solution_computed = False
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
      buff.write(_get_struct_3q2d6f3Bb().pack(_x.time_pub, _x.time_meas, _x.time_gps, _x.longitude_deg, _x.latitude_deg, _x.height, _x.east_std, _x.north_std, _x.up_std, _x.differential_age, _x.solution_age, _x.num_sats_tracked, _x.num_sats_in_solution, _x.solution_computed, _x.type))
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
      end += 68
      (_x.time_pub, _x.time_meas, _x.time_gps, _x.longitude_deg, _x.latitude_deg, _x.height, _x.east_std, _x.north_std, _x.up_std, _x.differential_age, _x.solution_age, _x.num_sats_tracked, _x.num_sats_in_solution, _x.solution_computed, _x.type,) = _get_struct_3q2d6f3Bb().unpack(str[start:end])
      self.solution_computed = bool(self.solution_computed)
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
      buff.write(_get_struct_3q2d6f3Bb().pack(_x.time_pub, _x.time_meas, _x.time_gps, _x.longitude_deg, _x.latitude_deg, _x.height, _x.east_std, _x.north_std, _x.up_std, _x.differential_age, _x.solution_age, _x.num_sats_tracked, _x.num_sats_in_solution, _x.solution_computed, _x.type))
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
      end += 68
      (_x.time_pub, _x.time_meas, _x.time_gps, _x.longitude_deg, _x.latitude_deg, _x.height, _x.east_std, _x.north_std, _x.up_std, _x.differential_age, _x.solution_age, _x.num_sats_tracked, _x.num_sats_in_solution, _x.solution_computed, _x.type,) = _get_struct_3q2d6f3Bb().unpack(str[start:end])
      self.solution_computed = bool(self.solution_computed)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3q2d6f3Bb = None
def _get_struct_3q2d6f3Bb():
    global _struct_3q2d6f3Bb
    if _struct_3q2d6f3Bb is None:
        _struct_3q2d6f3Bb = struct.Struct("<3q2d6f3Bb")
    return _struct_3q2d6f3Bb