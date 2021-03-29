.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 778bc211e0494661c0c66762f4f057ef

For random-access devices, this function returns the position that data is written to or read from. For sequential devices or closed devices, where there is no concept of a "current position", 0 is returned.

The current read/write position of the device is maintained internally by :sip:ref:`~PyQt6.QtCore.QIODevice`, so reimplementing this function is not necessary. When subclassing :sip:ref:`~PyQt6.QtCore.QIODevice`, use :sip:ref:`~PyQt6.QtCore.QIODevice.seek` to notify :sip:ref:`~PyQt6.QtCore.QIODevice` about changes in the device position.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.isSequential`, :sip:ref:`~PyQt6.QtCore.QIODevice.seek`.
