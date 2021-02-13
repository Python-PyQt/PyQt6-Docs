.. sip:method-description::
    :status: todo
    :pysig: 1c44c6b73b0b64ab5b4756a9a43a3033
    :realsig: (const QPolygon&,Qt::FillRule)
    :digest: 0482cf2a06dadb4e3a4f9371a5686e5a

Constructs a polygon region from the point array *a* with the fill rule specified by *fillRule*.

If *fillRule* is :sip:ref:`~PyQt6.QtCore.Qt.FillRule.WindingFill`, the polygon region is defined using the winding algorithm; if it is :sip:ref:`~PyQt6.QtCore.Qt.FillRule.OddEvenFill`, the odd-even fill algorithm is used.

**Warning:** This constructor can be used to create complex regions that will slow down painting when used.
