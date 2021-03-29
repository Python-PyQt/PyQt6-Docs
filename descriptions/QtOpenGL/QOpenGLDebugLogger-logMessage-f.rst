.. sip:method-description::
    :status: todo
    :pysig: a1b7b468f4f8c9d0aaf59d2a5677f459
    :realsig: (const QOpenGLDebugMessage&)
    :digest: dadc229fd2f7e896f1be7ca5e981758b

Inserts the message *debugMessage* into the OpenGL debug log. This provides a way for applications or libraries to insert custom messages that can ease the debugging of OpenGL applications.

**Note:** *debugMessage* must have :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Sources.ApplicationSource` or :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Sources.ThirdPartySource` as its source, and a valid type and severity, otherwise it will not be inserted into the log.

**Note:** The object must be initialized before logging can happen.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.initialize`.
