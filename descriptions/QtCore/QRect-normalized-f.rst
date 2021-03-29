.. sip:method-description::
    :status: todo
    :pysig: f036f485eb055d6ec1bb498745801d23
    :realsig: () const
    :digest: 3aafffd588faeffbef6a2802923d68cf

Returns a normalized rectangle; i.e., a rectangle that has a non-negative width and height.

If :sip:ref:`~PyQt6.QtCore.QRect.width` < 0 the function swaps the left and right corners, and it swaps the top and bottom corners if :sip:ref:`~PyQt6.QtCore.QRect.height` < 0. The corners are at the same time changed from being non-inclusive to inclusive.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRect.isValid`, :sip:ref:`~PyQt6.QtCore.QRect.isEmpty`.
