.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: ddd343f239c2a800bdbe6586aa0b5dfe

This signal is emitted after the scene graph is synchronized with the QML state.

This signal can be used to do preparation required after calls to :sip:ref:`~PyQt6.QtQuick.QQuickItem.updatePaintNode`, while the GUI thread is still locked.

When using OpenGL, the `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ used for rendering by the scene graph will be bound at this point.

**Warning:** This signal is emitted from the scene graph rendering thread. If your slot function needs to finish before execution continues, you must make sure that the connection is direct (see :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType`).

**Warning:** When using OpenGL, be aware that setting OpenGL 3.x or 4.x specific states and leaving these enabled or set to non-default values when returning from the connected slot can interfere with the scene graph's rendering.
