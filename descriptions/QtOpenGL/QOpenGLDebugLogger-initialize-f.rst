.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: d9e3e5eb0fe2f1e1e317aabc1968416b

Initializes the object in the current OpenGL context. The context must support the ``GL_KHR_debug`` extension for the initialization to succeed. The object must be initialized before any logging can happen.

It is safe to call this function multiple times from the same context.

This function can also be used to change the context of a previously initialized object; note that in this case the object must not be logging when you call this function.

Returns ``true`` if the logger is successfully initialized; false otherwise.

.. seealso:: `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_.
