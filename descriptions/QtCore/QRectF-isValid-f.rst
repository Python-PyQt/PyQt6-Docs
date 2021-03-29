.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 6719b7cffabb18ec5945e67dcd6b0df4

Returns ``true`` if the rectangle is valid, otherwise returns ``false``.

A valid rectangle has a :sip:ref:`~PyQt6.QtCore.QRectF.width` > 0 and :sip:ref:`~PyQt6.QtCore.QRectF.height` > 0. Note that non-trivial operations like intersections are not defined for invalid rectangles. A valid rectangle is not empty (i.e.,  == !\ :sip:ref:`~PyQt6.QtCore.QRectF.isEmpty`).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRectF.isNull`, :sip:ref:`~PyQt6.QtCore.QRectF.isEmpty`, :sip:ref:`~PyQt6.QtCore.QRectF.normalized`.
