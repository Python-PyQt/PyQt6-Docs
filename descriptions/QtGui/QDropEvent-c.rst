.. sip:class-description::
    :status: todo
    :brief: Event which is sent when a drag and drop action is completed
    :digest: 87fc14e25efde59f4a395e24e90a2f52

The :sip:ref:`~PyQt6.QtGui.QDropEvent` class provides an event which is sent when a drag and drop action is completed.

When a widget accepts drop events, it will receive this event if it has accepted the most recent :sip:ref:`~PyQt6.QtGui.QDragEnterEvent` or :sip:ref:`~PyQt6.QtGui.QDragMoveEvent` sent to it.

The drop event contains a proposed action, available from :sip:ref:`~PyQt6.QtGui.QDropEvent.proposedAction`, for the widget to either accept or ignore. If the action can be handled by the widget, you should call the :sip:ref:`~PyQt6.QtGui.QDropEvent.acceptProposedAction` function. Since the proposed action can be a combination of :sip:ref:`~PyQt6.QtCore.Qt.DropActions` values, it may be useful to either select one of these values as a default action or ask the user to select their preferred action.

If the proposed drop action is not suitable, perhaps because your custom widget does not support that action, you can replace it with any of the :sip:ref:`~PyQt6.QtGui.QDropEvent.possibleActions` by calling :sip:ref:`~PyQt6.QtGui.QDropEvent.setDropAction` with your preferred action. If you set a value that is not present in the bitwise OR combination of values returned by :sip:ref:`~PyQt6.QtGui.QDropEvent.possibleActions`, the default copy action will be used. Once a replacement drop action has been set, call accept() instead of :sip:ref:`~PyQt6.QtGui.QDropEvent.acceptProposedAction` to complete the drop operation.

The :sip:ref:`~PyQt6.QtGui.QDropEvent.mimeData` function provides the data dropped on the widget in a :sip:ref:`~PyQt6.QtCore.QMimeData` object. This contains information about the MIME type of the data in addition to the data itself.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMimeData`, :sip:ref:`~PyQt6.QtGui.QDrag`, `Drag and Drop <https://doc.qt.io/qt-6/dnd.html>`_.
