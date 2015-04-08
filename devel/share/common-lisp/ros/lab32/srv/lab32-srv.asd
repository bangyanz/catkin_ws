
(cl:in-package :asdf)

(defsystem "lab32-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :nav_msgs-msg
)
  :components ((:file "_package")
    (:file "Pathsrv" :depends-on ("_package_Pathsrv"))
    (:file "_package_Pathsrv" :depends-on ("_package"))
  ))