.. sip:method-description::
    :status: todo
    :pysig: 72d5e6744060ceb4d4e08ac2501527fc
    :realsig: (Qt::DropActions)
    :digest: 5229084d67e4a3c56be0fd33c86334fb

Starts the drag and drop operation and returns a value indicating the requested drop action when it is completed. The drop actions that the user can choose from are specified in *supportedActions*. The default proposed action will be selected among the allowed actions in the following order: Move, Copy and Link.

**Note:** On Linux and macOS, the drag and drop operation can take some time, but this function does not block the event loop. Other events are still delivered to the application while the operation is performed. On Windows, the Qt event loop is blocked during the operation.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QDrag.cancel`.
