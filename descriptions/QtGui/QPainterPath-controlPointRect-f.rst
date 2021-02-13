.. sip:method-description::
    :status: todo
    :pysig: 13589a9b9c4c6c30ca426ce536937662
    :realsig: () const
    :digest: 1d03a3c5c817ed5c8b6b33851640e234

Returns the rectangle containing all the points and control points in this path.

This function is significantly faster to compute than the exact :sip:ref:`~PyQt6.QtGui.QPainterPath.boundingRect`, and the returned rectangle is always a superset of the rectangle returned by :sip:ref:`~PyQt6.QtGui.QPainterPath.boundingRect`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.boundingRect`.
