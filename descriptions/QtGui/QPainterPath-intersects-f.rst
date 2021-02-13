.. sip:method-description::
    :status: todo
    :pysig: bf013c0872d1be9a38919916c4ae243a
    :realsig: (const QRectF&) const
    :digest: 584a99ca1e0d92087b0d06e9bab0dc8c

Returns ``true`` if any point in the given *rectangle* intersects the path; otherwise returns ``false``.

There is an intersection if any of the lines making up the rectangle crosses a part of the path or if any part of the rectangle overlaps with any area enclosed by the path. This function respects the current :sip:ref:`~PyQt6.QtGui.QPainterPath.fillRule` to determine what is considered inside the path.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.contains`.
