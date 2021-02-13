.. sip:method-description::
    :status: todo
    :pysig: 0b55dee661d98093cd9a7214a4be5e95
    :realsig: (const void*,int)
    :digest: e7546dda9cc3e78c92e37d0cc686e3fa

Allocates *count* bytes of space to the buffer, initialized to the contents of *data*. Any previous contents will be removed.

It is assumed that :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.create` has been called on this buffer and that it has been bound to the current context.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.create`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.read`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.write`.
