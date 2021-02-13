.. sip:method-description::
    :status: todo
    :pysig: 893c335706200abc185454b9c518acce
    :realsig: () const
    :digest: c9290ec6a5b1b2a3bbe8386785fe7922

Returns the normalized unit form of this quaternion.

If this quaternion is null, then a null quaternion is returned. If the length of the quaternion is very close to 1, then the quaternion will be returned as-is. Otherwise the normalized form of the quaternion of length 1 will be returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QQuaternion.normalize`, :sip:ref:`~PyQt6.QtGui.QQuaternion.length`, :sip:ref:`~PyQt6.QtGui.QQuaternion.dotProduct`.
