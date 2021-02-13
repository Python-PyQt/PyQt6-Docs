.. sip:method-description::
    :status: todo
    :pysig: 22129251b88267f51c8f630979b39081
    :realsig: () const
    :digest: b97f50699df5de2e5eca100fab436219

Returns the format of the underlying platform context, if :sip:ref:`~PyQt6.QtGui.QOpenGLContext.create` has been called.

Otherwise, returns the requested format.

The requested and the actual format may differ. Requesting a given OpenGL version does not mean the resulting context will target exactly the requested version. It is only guaranteed that the version/profile/options combination for the created context is compatible with the request, as long as the driver is able to provide such a context.

For example, requesting an OpenGL version 3.x core profile context may result in an OpenGL 4.x core profile context. Similarly, a request for OpenGL 2.1 may result in an OpenGL 3.0 context with deprecated functions enabled. Finally, depending on the driver, unsupported versions may result in either a context creation failure or in a context for the highest supported version.

Similar differences are possible in the buffer sizes, for example, the resulting context may have a larger depth buffer than requested. This is perfectly normal.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QOpenGLContext.setFormat`.
