.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 51796bd179e15a6241015189c56287d5

This signal is emitted on the render thread when the scene graph is about to stop rendering. This happens usually because the window has been hidden.

Applications may use this signal to release resources, but should be prepared to reinstantiated them again fast. The scene graph and the graphics context are not released at this time.

**Warning:** This signal is emitted from the scene graph rendering thread. If your slot function needs to finish before execution continues, you must make sure that the connection is direct (see :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType`).

**Warning:** Make very sure that a signal handler for  leaves the graphics context in the same state as it was when the signal handler was entered. Failing to do so can result in the scene not rendering properly.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInvalidated`.
