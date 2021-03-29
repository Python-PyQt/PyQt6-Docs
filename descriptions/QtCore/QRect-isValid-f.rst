.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 561851bb7021c4b8e9fff1018302542d

Returns ``true`` if the rectangle is valid, otherwise returns ``false``.

A valid rectangle has a :sip:ref:`~PyQt6.QtCore.QRect.left` <= :sip:ref:`~PyQt6.QtCore.QRect.right` and :sip:ref:`~PyQt6.QtCore.QRect.top` <= :sip:ref:`~PyQt6.QtCore.QRect.bottom`. Note that non-trivial operations like intersections are not defined for invalid rectangles. A valid rectangle is not empty (i.e.,  == !\ :sip:ref:`~PyQt6.QtCore.QRect.isEmpty`).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRect.isNull`, :sip:ref:`~PyQt6.QtCore.QRect.isEmpty`, :sip:ref:`~PyQt6.QtCore.QRect.normalized`.
