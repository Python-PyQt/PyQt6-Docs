.. sip:enum-description::
    :status: todo
    :digest: 2943c6538a01d41148fc553c59a61064

This enum describes the types of elements used to connect vertices in subpaths.

Note that elements added as closed subpaths using the :sip:ref:`~PyQt6.QtGui.QPainterPath.addEllipse`, :sip:ref:`~PyQt6.QtGui.QPainterPath.addPath`, :sip:ref:`~PyQt6.QtGui.QPainterPath.addPolygon`, :sip:ref:`~PyQt6.QtGui.QPainterPath.addRect`, :sip:ref:`~PyQt6.QtGui.QPainterPath.addRegion` and :sip:ref:`~PyQt6.QtGui.QPainterPath.addText` convenience functions, is actually added to the path as a collection of separate elements using the :sip:ref:`~PyQt6.QtGui.QPainterPath.moveTo`, :sip:ref:`~PyQt6.QtGui.QPainterPath.lineTo` and :sip:ref:`~PyQt6.QtGui.QPainterPath.cubicTo` functions.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.elementAt`, :sip:ref:`~PyQt6.QtGui.QPainterPath.elementCount`.
