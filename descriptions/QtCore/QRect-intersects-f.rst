.. sip:method-description::
    :status: todo
    :pysig: 9d5a698f12441ea2f45c4b2b230fcd50
    :realsig: (const QRect&) const
    :digest: f962bcffe5d5df544f44c6564c3e377c

Returns ``true`` if this rectangle intersects with the given *rectangle* (i.e., there is at least one pixel that is within both rectangles), otherwise returns ``false``.

The intersection rectangle can be retrieved using the :sip:ref:`~PyQt6.QtCore.QRect.intersected` function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRect.contains`.
