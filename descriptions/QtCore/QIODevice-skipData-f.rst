.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (qint64)
    :digest: 558101a82414599813983e6338b8829a

Skips up to *maxSize* bytes from the device. Returns the number of bytes actually skipped, or -1 on error.

This function is called by :sip:ref:`~PyQt6.QtCore.QIODevice`. Consider reimplementing it when creating a subclass of :sip:ref:`~PyQt6.QtCore.QIODevice`.

The base implementation discards the data by reading into a dummy buffer. This is slow, but works for all types of devices. Subclasses can reimplement this function to improve on that.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.skip`, :sip:ref:`~PyQt6.QtCore.QIODevice.peek`, :sip:ref:`~PyQt6.QtCore.QIODevice.seek`, :sip:ref:`~PyQt6.QtCore.QIODevice.read`.
