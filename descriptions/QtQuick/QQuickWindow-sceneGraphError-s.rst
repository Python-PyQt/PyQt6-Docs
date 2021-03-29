.. sip:signal-description::
    :status: todo
    :pysig: 2349d2ced140ebc547e1207b10415d04
    :realsig: (QQuickWindow::SceneGraphError,const QString&)
    :digest: 96e5a3a9a9e5cac77b115da8452f561a

This signal is emitted when an *error* occurred during scene graph initialization.

Applications should connect to this signal if they wish to handle errors, like graphics context creation failures, in a custom way. When no slot is connected to the signal, the behavior will be different: Quick will print the *message*, or show a message box, and terminate the application.

This signal will be emitted from the GUI thread.
