.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: db1f6f5eed5be9106be21508ff5114f8

For open random-access devices, this function returns the size of the device. For open sequential devices, :sip:ref:`~PyQt6.QtCore.QIODevice.bytesAvailable` is returned.

If the device is closed, the size returned will not reflect the actual size of the device.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.isSequential`, :sip:ref:`~PyQt6.QtCore.QIODevice.pos`.
