.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 6a11b52ed2ce642a4ba152a0243cabff

This signal is emitted when the scene graph has been invalidated.

This signal implies that the graphics rendering context used has been invalidated and all user resources tied to that context should be released.

When rendering with OpenGL, the `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ of this window will be bound when this function is called. The only exception is if the native OpenGL has been destroyed outside Qt's control, for instance through EGL_CONTEXT_LOST.

This signal will be emitted from the scene graph rendering thread.
