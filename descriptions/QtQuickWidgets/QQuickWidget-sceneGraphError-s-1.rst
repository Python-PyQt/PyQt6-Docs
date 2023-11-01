.. sip:signal-description::
    :status: todo
    :pysig: 67e1ec7a85cb890eeb0afd7966408178
    :realsig: (QQuickWindow::SceneGraphError, const QString&)
    :digest: a0e65b5f0702438e193f7b6e181b4e16

This signal is emitted when an *error* occurred during scene graph initialization.

Applications should connect to this signal if they wish to handle errors, like OpenGL context creation failures, in a custom way. When no slot is connected to the signal, the behavior will be different: Quick will print the *message*, or show a message box, and terminate the application.

This signal will be emitted from the GUI thread.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphError`.
