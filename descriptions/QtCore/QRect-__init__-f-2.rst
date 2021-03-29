.. sip:method-description::
    :status: todo
    :pysig: a8722baadb47abef4a1e6616c2778b95
    :realsig: (const QPoint&,const QPoint&)
    :digest: 993619c88971f21f764084f43bf7f839

Constructs a rectangle with the given *topLeft* and *bottomRight* corners, both included.

If *bottomRight* is to higher and to the left of *topLeft*, the rectangle defined is instead non-inclusive of the corners.

**Note:** To ensure both points are included regardless of relative order, use :sip:ref:`~PyQt6.QtCore.QRect.span`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRect.setTopLeft`, :sip:ref:`~PyQt6.QtCore.QRect.setBottomRight`, :sip:ref:`~PyQt6.QtCore.QRect.span`.
