.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ada534e67cf50c05e0033c5be913798d

Returns ``true`` if this device is sequential; otherwise returns false.

Sequential devices, as opposed to a random-access devices, have no concept of a start, an end, a size, or a current position, and they do not support seeking. You can only read from the device when it reports that data is available. The most common example of a sequential device is a network socket. On Unix, special files such as /dev/zero and fifo pipes are sequential.

Regular files, on the other hand, do support random access. They have both a size and a current position, and they also support seeking backwards and forwards in the data stream. Regular files are non-sequential.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.bytesAvailable`.
