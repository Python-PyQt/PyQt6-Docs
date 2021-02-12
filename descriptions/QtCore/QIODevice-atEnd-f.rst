.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 87c03b128b985eb7ead1cb9430ac9170

Returns ``true`` if the current read and write position is at the end of the device (i.e. there is no more data available for reading on the device); otherwise returns ``false``.

For some devices,  can return true even though there is more data to read. This special case only applies to devices that generate data in direct response to you calling :sip:ref:`~PyQt6.QtCore.QIODevice.read` (e.g., ``/dev`` or ``/proc`` files on Unix and macOS, or console input / ``stdin`` on all platforms).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.bytesAvailable`, :sip:ref:`~PyQt6.QtCore.QIODevice.read`, :sip:ref:`~PyQt6.QtCore.QIODevice.isSequential`.
