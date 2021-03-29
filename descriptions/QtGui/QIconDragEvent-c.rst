.. sip:class-description::
    :status: todo
    :brief: Indicates that a main icon drag has begun
    :digest: efa7d07e078a4071fcafa66b8ca4d228

The :sip:ref:`~PyQt6.QtGui.QIconDragEvent` class indicates that a main icon drag has begun.

Icon drag events are sent to widgets when the main icon of a window has been dragged away. On macOS, this happens when the proxy icon of a window is dragged off the title bar.

It is normal to begin using drag and drop in response to this event.

.. seealso:: `Drag and Drop <https://doc.qt.io/qt-6/dnd.html>`_, :sip:ref:`~PyQt6.QtCore.QMimeData`, :sip:ref:`~PyQt6.QtGui.QDrag`.
