.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 54b32afce153895893246e4cdf38d863

Initializes the graphics resources used by the blitter.

Returns ``true`` if successful, ``false`` if there was a failure. Failures can occur when there is no OpenGL context current on the current thread, or when shader compilation fails for some reason.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTextureBlitter.isCreated`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTextureBlitter.destroy`.
