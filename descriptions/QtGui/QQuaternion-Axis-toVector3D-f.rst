.. sip:method-description::
    :status: todo
    :pysig: b745689becad30ca8dcb68bd656eeb64
    :realsig: () const
    :digest: 6396cfe3eb901ae1b9c7e3ea506d47bb

Returns this Axis as a :sip:ref:`~PyQt6.QtGui.QVector3D`, as if by

::

    Axis a = *this;
    return QVector3D{a.x, a.y, a.z}
