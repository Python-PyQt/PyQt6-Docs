.. sip:method-description::
    :status: todo
    :pysig: 7d38cafd49881113072a25f94c4fa5b3
    :realsig: (const QPainterPath&) const
    :digest: 893563449a811e3c2267217c950bf921

Generates a new path that is a fillable area representing the outline of the given *path*.

The various design aspects of the outline are based on the stroker's properties: :sip:ref:`~PyQt6.QtGui.QPainterPathStroker.width`, :sip:ref:`~PyQt6.QtGui.QPainterPathStroker.capStyle`, :sip:ref:`~PyQt6.QtGui.QPainterPathStroker.joinStyle`, :sip:ref:`~PyQt6.QtGui.QPainterPathStroker.dashPattern`, :sip:ref:`~PyQt6.QtGui.QPainterPathStroker.curveThreshold` and :sip:ref:`~PyQt6.QtGui.QPainterPathStroker.miterLimit`.

The generated path should only be used for outlining the given painter path. Otherwise it may cause unexpected behavior. Generated outlines also require the :sip:ref:`~PyQt6.QtCore.Qt.FillRule.WindingFill` rule which is set by default.
