.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 72875768b81a39873068cb813ab59bd1

This signal is emitted before the scene graph is synchronized with the QML state.

Even though the signal is emitted from the scene graph rendering thread, the GUI thread is guaranteed to be blocked, like it is in :sip:ref:`~PyQt6.QtQuick.QQuickItem.updatePaintNode`. Therefore, it is safe to access GUI thread thread data in a slot or lambda that is connected with :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.DirectConnection`.

This signal can be used to do any preparation required before calls to :sip:ref:`~PyQt6.QtQuick.QQuickItem.updatePaintNode`.

When using OpenGL, the `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ used for rendering by the scene graph will be bound at this point.

**Warning:** This signal is emitted from the scene graph rendering thread. If your slot function needs to finish before execution continues, you must make sure that the connection is direct (see :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType`).

**Warning:** When using OpenGL, be aware that setting OpenGL 3.x or 4.x specific states and leaving these enabled or set to non-default values when returning from the connected slot can interfere with the scene graph's rendering.
