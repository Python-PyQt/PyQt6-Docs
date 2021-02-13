.. sip:method-description::
    :status: todo
    :pysig: 43f6970fc0b4502a303decb8449afc37
    :realsig: (bool*) const
    :digest: b9bcabe949bccef143ff3f8fe9f2eebb

Returns an inverted copy of this matrix.

If the matrix is singular (not invertible), the returned matrix is the identity matrix. If *invertible* is valid (i.e. not 0), its value is set to true if the matrix is invertible, otherwise it is set to false.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTransform.isInvertible`.
