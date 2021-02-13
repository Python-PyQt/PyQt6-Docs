.. sip:method-description::
    :status: todo
    :pysig: 2724ba9ed7edb69588bf719353fdf6cf
    :realsig: (QOpenGLDebugLogger::LoggingMode)
    :digest: 87fdefb58abd17181a82d36d84b6cf0c

Starts logging messages coming from the OpenGL server. When a new message is received, the signal :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.messageLogged` is emitted, carrying the logged message as argument.

*loggingMode* specifies whether the logging must be asynchronous (the default) or synchronous.

:sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger` will record the values of ``GL_DEBUG_OUTPUT`` and ``GL_DEBUG_OUTPUT_SYNCHRONOUS`` when logging is started, and set them back when logging is stopped. Moreover, any user-defined OpenGL debug callback installed when this function is invoked will be restored when logging is stopped; :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger` will ensure that the pre-existing callback will still be invoked when logging.

**Note:** It's not possible to change the logging mode without stopping and starting logging again. This might change in a future version of Qt.

**Note:** The object must be initialized before logging can happen.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.stopLogging`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.initialize`.
