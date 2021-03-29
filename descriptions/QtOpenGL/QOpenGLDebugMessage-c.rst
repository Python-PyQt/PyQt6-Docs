.. sip:class-description::
    :status: todo
    :brief: Wraps an OpenGL debug message
    :digest: 633429275c9ff73ac2a2c1659a6eb549

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage` class wraps an OpenGL debug message.

Debug messages are usually created by the OpenGL server and then read by OpenGL clients (either from the OpenGL internal debug log, or logged in real-time). A debug message has a textual representation, a vendor-specific numeric id, a source, a type and a severity.

It's also possible for applications or third-party libraries and toolkits to create and insert messages in the debug log. In order to do so, you can use the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.createApplicationMessage` or the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.createThirdPartyMessage` static functions.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger`.
