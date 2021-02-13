.. sip:class-description::
    :status: todo
    :brief: Event which is sent to a widget when a drag and drop action enters it
    :digest: 9ca4c8f22e24dcf853d6d762f2ab2eab

The :sip:ref:`~PyQt6.QtGui.QDragEnterEvent` class provides an event which is sent to a widget when a drag and drop action enters it.

A widget must accept this event in order to receive the :sip:ref:`~PyQt6.QtGui.QDragMoveEvent` that are sent while the drag and drop action is in progress. The drag enter event is always immediately followed by a drag move event.

:sip:ref:`~PyQt6.QtGui.QDragEnterEvent` inherits most of its functionality from :sip:ref:`~PyQt6.QtGui.QDragMoveEvent`, which in turn inherits most of its functionality from :sip:ref:`~PyQt6.QtGui.QDropEvent`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QDragLeaveEvent`, :sip:ref:`~PyQt6.QtGui.QDragMoveEvent`, :sip:ref:`~PyQt6.QtGui.QDropEvent`.
