; Auto-generated. Do not edit!


(cl:in-package lab3-srv)


;//! \htmlinclude Pathsrv-request.msg.html

(cl:defclass <Pathsrv-request> (roslisp-msg-protocol:ros-message)
  ((gridMap
    :reader gridMap
    :initarg :gridMap
    :type nav_msgs-msg:OccupancyGrid
    :initform (cl:make-instance 'nav_msgs-msg:OccupancyGrid))
   (start
    :reader start
    :initarg :start
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (goal
    :reader goal
    :initarg :goal
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point)))
)

(cl:defclass Pathsrv-request (<Pathsrv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Pathsrv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Pathsrv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lab3-srv:<Pathsrv-request> is deprecated: use lab3-srv:Pathsrv-request instead.")))

(cl:ensure-generic-function 'gridMap-val :lambda-list '(m))
(cl:defmethod gridMap-val ((m <Pathsrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lab3-srv:gridMap-val is deprecated.  Use lab3-srv:gridMap instead.")
  (gridMap m))

(cl:ensure-generic-function 'start-val :lambda-list '(m))
(cl:defmethod start-val ((m <Pathsrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lab3-srv:start-val is deprecated.  Use lab3-srv:start instead.")
  (start m))

(cl:ensure-generic-function 'goal-val :lambda-list '(m))
(cl:defmethod goal-val ((m <Pathsrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lab3-srv:goal-val is deprecated.  Use lab3-srv:goal instead.")
  (goal m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Pathsrv-request>) ostream)
  "Serializes a message object of type '<Pathsrv-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'gridMap) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'start) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Pathsrv-request>) istream)
  "Deserializes a message object of type '<Pathsrv-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'gridMap) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'start) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Pathsrv-request>)))
  "Returns string type for a service object of type '<Pathsrv-request>"
  "lab3/PathsrvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Pathsrv-request)))
  "Returns string type for a service object of type 'Pathsrv-request"
  "lab3/PathsrvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Pathsrv-request>)))
  "Returns md5sum for a message object of type '<Pathsrv-request>"
  "f1fa7bf596f4be272e361a20bf7c865c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Pathsrv-request)))
  "Returns md5sum for a message object of type 'Pathsrv-request"
  "f1fa7bf596f4be272e361a20bf7c865c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Pathsrv-request>)))
  "Returns full string definition for message of type '<Pathsrv-request>"
  (cl:format cl:nil "nav_msgs/OccupancyGrid gridMap~%geometry_msgs/Point start~%geometry_msgs/Point goal~%~%================================================================================~%MSG: nav_msgs/OccupancyGrid~%# This represents a 2-D grid map, in which each cell represents the probability of~%# occupancy.~%~%Header header ~%~%#MetaData for the map~%MapMetaData info~%~%# The map data, in row-major order, starting with (0,0).  Occupancy~%# probabilities are in the range [0,100].  Unknown is -1.~%int8[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: nav_msgs/MapMetaData~%# This hold basic information about the characterists of the OccupancyGrid~%~%# The time at which the map was loaded~%time map_load_time~%# The map resolution [m/cell]~%float32 resolution~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Pathsrv-request)))
  "Returns full string definition for message of type 'Pathsrv-request"
  (cl:format cl:nil "nav_msgs/OccupancyGrid gridMap~%geometry_msgs/Point start~%geometry_msgs/Point goal~%~%================================================================================~%MSG: nav_msgs/OccupancyGrid~%# This represents a 2-D grid map, in which each cell represents the probability of~%# occupancy.~%~%Header header ~%~%#MetaData for the map~%MapMetaData info~%~%# The map data, in row-major order, starting with (0,0).  Occupancy~%# probabilities are in the range [0,100].  Unknown is -1.~%int8[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: nav_msgs/MapMetaData~%# This hold basic information about the characterists of the OccupancyGrid~%~%# The time at which the map was loaded~%time map_load_time~%# The map resolution [m/cell]~%float32 resolution~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Pathsrv-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'gridMap))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'start))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Pathsrv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Pathsrv-request
    (cl:cons ':gridMap (gridMap msg))
    (cl:cons ':start (start msg))
    (cl:cons ':goal (goal msg))
))
;//! \htmlinclude Pathsrv-response.msg.html

(cl:defclass <Pathsrv-response> (roslisp-msg-protocol:ros-message)
  ((path
    :reader path
    :initarg :path
    :type nav_msgs-msg:Path
    :initform (cl:make-instance 'nav_msgs-msg:Path)))
)

(cl:defclass Pathsrv-response (<Pathsrv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Pathsrv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Pathsrv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lab3-srv:<Pathsrv-response> is deprecated: use lab3-srv:Pathsrv-response instead.")))

(cl:ensure-generic-function 'path-val :lambda-list '(m))
(cl:defmethod path-val ((m <Pathsrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lab3-srv:path-val is deprecated.  Use lab3-srv:path instead.")
  (path m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Pathsrv-response>) ostream)
  "Serializes a message object of type '<Pathsrv-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'path) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Pathsrv-response>) istream)
  "Deserializes a message object of type '<Pathsrv-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'path) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Pathsrv-response>)))
  "Returns string type for a service object of type '<Pathsrv-response>"
  "lab3/PathsrvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Pathsrv-response)))
  "Returns string type for a service object of type 'Pathsrv-response"
  "lab3/PathsrvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Pathsrv-response>)))
  "Returns md5sum for a message object of type '<Pathsrv-response>"
  "f1fa7bf596f4be272e361a20bf7c865c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Pathsrv-response)))
  "Returns md5sum for a message object of type 'Pathsrv-response"
  "f1fa7bf596f4be272e361a20bf7c865c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Pathsrv-response>)))
  "Returns full string definition for message of type '<Pathsrv-response>"
  (cl:format cl:nil "nav_msgs/Path path~%~%~%================================================================================~%MSG: nav_msgs/Path~%#An array of poses that represents a Path for a robot to follow~%Header header~%geometry_msgs/PoseStamped[] poses~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Pathsrv-response)))
  "Returns full string definition for message of type 'Pathsrv-response"
  (cl:format cl:nil "nav_msgs/Path path~%~%~%================================================================================~%MSG: nav_msgs/Path~%#An array of poses that represents a Path for a robot to follow~%Header header~%geometry_msgs/PoseStamped[] poses~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Pathsrv-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'path))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Pathsrv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Pathsrv-response
    (cl:cons ':path (path msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Pathsrv)))
  'Pathsrv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Pathsrv)))
  'Pathsrv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Pathsrv)))
  "Returns string type for a service object of type '<Pathsrv>"
  "lab3/Pathsrv")