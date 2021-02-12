.. sip:method-description::
    :status: todo
    :pysig: 992e8d0e5b57a6e4e940f41b84286512
    :realsig: ()
    :digest: b278d9561929813290be9c53e92cbf19

Returns a unique ID for this machine's boot, if one can be determined. If no unique ID could be determined, this function returns an empty byte array. This value is expected to change after every boot and can be considered globally unique.

This function is currently only implemented for Linux and Apple operating systems.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSysInfo.machineUniqueId`.
