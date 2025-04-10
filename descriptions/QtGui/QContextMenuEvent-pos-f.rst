.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: () const
    :digest: facb128109a2ea3aa13ecfd0a7b2ef79

Returns the position of the mouse pointer relative to the widget that received the event.

**Note:** If the :sip:ref:`~PyQt6.QtGui.QContextMenuEvent` did not come from the right mouse button, ``pos()`` may be :sip:ref:`~PyQt6.QtCore.QPoint.isNull`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QContextMenuEvent.x`, :sip:ref:`~PyQt6.QtGui.QContextMenuEvent.y`, :sip:ref:`~PyQt6.QtGui.QContextMenuEvent.globalPos`.
