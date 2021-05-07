.. sip:method-description::
    :status: todo
    :pysig: 469b2c2ac573b3f3ead6d96aee5244d2
    :realsig: (qint64,qint64,QFileDevice::MemoryMapFlags)
    :digest: 0b6ccde8349c528de71bd54be6dc011a

Maps *size* bytes of the file into memory starting at *offset*. A file should be open for a map to succeed but the file does not need to stay open after the memory has been mapped. When the :sip:ref:`~PyQt6.QtCore.QFile` is destroyed or a new file is opened with this object, any maps that have not been unmapped will automatically be unmapped.

The mapping will have the same open mode as the file (read and/or write), except when using :sip:ref:`~PyQt6.QtCore.QFileDevice.MemoryMapFlag.MapPrivateOption`, in which case it is always possible to write to the mapped memory.

Any mapping options can be passed through *flags*.

Returns a pointer to the memory or ``nullptr`` if there is an error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileDevice.unmap`.
