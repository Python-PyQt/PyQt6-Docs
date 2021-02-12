.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: d06c0d2984b3d13cd15f24eb1c99f155

Returns ``true`` if the rectangle is empty, otherwise returns ``false``.

An empty rectangle has :sip:ref:`~PyQt6.QtCore.QRectF.width` <= 0 or :sip:ref:`~PyQt6.QtCore.QRectF.height` <= 0. An empty rectangle is not valid (i.e.,  == !\ :sip:ref:`~PyQt6.QtCore.QRectF.isValid`).

Use the :sip:ref:`~PyQt6.QtCore.QRectF.normalized` function to retrieve a rectangle where the corners are swapped.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRectF.isNull`, :sip:ref:`~PyQt6.QtCore.QRectF.isValid`, :sip:ref:`~PyQt6.QtCore.QRectF.normalized`.
