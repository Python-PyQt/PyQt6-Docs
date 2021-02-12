.. sip:method-description::
    :status: todo
    :pysig: 992e8d0e5b57a6e4e940f41b84286512
    :realsig: ()
    :digest: 674953ff523099091ef2758abceb9474

Returns a unique ID for this machine, if one can be determined. If no unique ID could be determined, this function returns an empty byte array. Unlike :sip:ref:`~PyQt6.QtCore.QSysInfo.machineHostName`, the value returned by this function is likely globally unique.

A unique ID is useful in network operations to identify this machine for an extended period of time, when the IP address could change or if this machine could have more than one IP address. For example, the ID could be used when communicating with a server or when storing device-specific data in shared network storage.

Note that on some systems, this value will persist across reboots and on some it will not. Applications should not blindly depend on this fact without verifying the OS capabilities. In particular, on Linux systems, this ID is usually permanent and it matches the D-Bus machine ID, except for nodes without their own storage (replicated nodes).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSysInfo.machineHostName`, :sip:ref:`~PyQt6.QtCore.QSysInfo.bootUniqueId`.
