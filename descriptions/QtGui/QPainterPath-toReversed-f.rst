.. sip:method-description::
    :status: todo
    :pysig: b53df27f41e7e1e87eded6e72ecfdeb9
    :realsig: () const
    :digest: 9ff99c969fbefb795c2b09f7be17c938

Creates and returns a reversed copy of the path.

It is the order of the elements that is reversed: If a :sip:ref:`~PyQt6.QtGui.QPainterPath` is composed by calling the :sip:ref:`~PyQt6.QtGui.QPainterPath.moveTo`, :sip:ref:`~PyQt6.QtGui.QPainterPath.lineTo` and :sip:ref:`~PyQt6.QtGui.QPainterPath.cubicTo` functions in the specified order, the reversed copy is composed by calling :sip:ref:`~PyQt6.QtGui.QPainterPath.cubicTo`, :sip:ref:`~PyQt6.QtGui.QPainterPath.lineTo` and :sip:ref:`~PyQt6.QtGui.QPainterPath.moveTo`.
