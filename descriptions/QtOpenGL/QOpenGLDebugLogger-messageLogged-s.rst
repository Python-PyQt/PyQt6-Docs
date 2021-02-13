.. sip:signal-description::
    :status: todo
    :pysig: a1b7b468f4f8c9d0aaf59d2a5677f459
    :realsig: (const QOpenGLDebugMessage&)
    :digest: e89fc1c441e585ced9636e909c9b7823

This signal is emitted when a debug message (wrapped by the *debugMessage* argument) is logged from the OpenGL server.

Depending on the OpenGL implementation, this signal can be emitted from other threads than the one(s) the receiver(s) lives in, and even different from the thread the `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ in which this object has been initialized lives in. Moreover, the signal could be emitted from multiple threads at the same time. This is normally not a problem, as Qt will utilize a queued connection for cross-thread signal emissions, but if you force the connection type to Direct then you must be aware of the potential races in the slots connected to this signal.

If logging have been started in :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.LoggingMode.SynchronousLogging` mode, OpenGL guarantees that this signal will be emitted from the same thread the `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ has been bound to, and no concurrent invocations will ever happen.

**Note:** Logging must have been started, or this signal will not be emitted.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.startLogging`.
