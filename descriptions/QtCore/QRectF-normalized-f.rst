.. sip:method-description::
    :status: todo
    :pysig: 13589a9b9c4c6c30ca426ce536937662
    :realsig: () const
    :digest: 3aafffd588faeffbef6a2802923d68cf

Returns a normalized rectangle; i.e., a rectangle that has a non-negative width and height.

If :sip:ref:`~PyQt6.QtCore.QRectF.width` < 0 the function swaps the left and right corners, and it swaps the top and bottom corners if :sip:ref:`~PyQt6.QtCore.QRectF.height` < 0.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRectF.isValid`, :sip:ref:`~PyQt6.QtCore.QRectF.isEmpty`.
