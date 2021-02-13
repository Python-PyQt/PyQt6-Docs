.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: (QIODevice*)
    :digest: cbb97a7c1c84de6ac6af0297129b6059

Sets the device of the :sip:ref:`~PyQt6.QtGui.QImageIOHandler` to *device*. The image handler will use this device when reading and writing images.

The device can only be set once and must be set before calling :sip:ref:`~PyQt6.QtGui.QImageIOHandler.canRead`, :sip:ref:`~PyQt6.QtGui.QImageIOHandler.read`, :sip:ref:`~PyQt6.QtGui.QImageIOHandler.write`, etc. If you need to read multiple files, construct multiple instances of the appropriate :sip:ref:`~PyQt6.QtGui.QImageIOHandler` subclass.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageIOHandler.device`.
