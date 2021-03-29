.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 55176553d43f09fecb20703150dad333

Returns ``true`` if this matrix is affine matrix; false otherwise.

An affine matrix is a 4x4 matrix with row 3 equal to (0, 0, 0, 1), e.g. no projective coefficients.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QMatrix4x4.isIdentity`.
