.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: e8efc8e742745bd15b1ff295f84d12f0

Returns the maximum supported length, in bytes, for the text of the messages passed to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.logMessage`. This is also the maximum length of a debug group name, as pushing or popping groups will automatically log a message with the debug group name as the message text.

If a message text is too long, it will be automatically truncated by :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger`.

**Note:** Message texts are encoded in UTF-8 when they get passed to OpenGL, so their size in bytes does not usually match the amount of UTF-16 code units, as returned, for instance, by QString::length(). (It does if the message contains 7-bit ASCII only data, which is typical for debug messages.)
