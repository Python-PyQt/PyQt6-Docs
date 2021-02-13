.. sip:method-description::
    :status: todo
    :pysig: 885cc48f6ca8281eb0bde681c1342e7f
    :realsig: () const
    :digest: 2a38c638ce8efb855535699a961a3c86

Returns the normalized unit vector form of this vector.

If this vector is null, then a null vector is returned. If the length of the vector is very close to 1, then the vector will be returned as-is. Otherwise the normalized form of the vector of length 1 will be returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QVector4D.length`, :sip:ref:`~PyQt6.QtGui.QVector4D.normalize`.
