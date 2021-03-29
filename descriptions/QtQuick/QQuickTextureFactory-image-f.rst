.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: () const
    :digest: d429418496ce3bf43c9dc26f05e98a64

Returns an image version of this texture.

The lifespan of the returned image is unknown, so the implementation should return a self contained :sip:ref:`~PyQt6.QtGui.QImage`, not make use of the :sip:ref:`~PyQt6.QtGui.QImage`\ (uchar \*, ...) constructor.

This function is not commonly used and is expected to be slow.
