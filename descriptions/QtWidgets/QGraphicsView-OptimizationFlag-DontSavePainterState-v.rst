.. sip:enum-member-description::
    :status: todo
    :value: 0x1
    :digest: 61ffeefbf123825c5f899e6e54be7424

When rendering, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` protects the painter state (see :sip:ref:`~PyQt6.QtGui.QPainter.save`) when rendering the background or foreground, and when rendering each item. This allows you to leave the painter in an altered state (i.e., you can call :sip:ref:`~PyQt6.QtGui.QPainter.setPen` or :sip:ref:`~PyQt6.QtGui.QPainter.setBrush` without restoring the state after painting). However, if the items consistently do restore the state, you should enable this flag to prevent :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` from doing the same.
