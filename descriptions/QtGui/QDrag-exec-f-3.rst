.. sip:method-description::
    :status: todo
    :pysig: 9c47151fdafc94e87987d78596ff9b71
    :realsig: (Qt::DropActions,Qt::DropAction)
    :digest: 054d3f01605ff8884674ab5ee98fc3a8

Starts the drag and drop operation and returns a value indicating the requested drop action when it is completed. The drop actions that the user can choose from are specified in *supportedActions*.

The *defaultDropAction* determines which action will be proposed when the user performs a drag without using modifier keys.

**Note:** On Linux and macOS, the drag and drop operation can take some time, but this function does not block the event loop. Other events are still delivered to the application while the operation is performed. On Windows, the Qt event loop is blocked during the operation. However, :sip:ref:`~PyQt6.QtGui.QDrag.exec` on Windows causes processEvents() to be called frequently to keep the GUI responsive. If any loops or operations are called while a drag operation is active, it will block the drag operation.
