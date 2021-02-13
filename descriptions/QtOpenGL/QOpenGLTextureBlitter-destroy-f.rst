.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 2d1c552e847211b2472059c75c922ef3

Frees all graphics resources held by the blitter. Assumes that the OpenGL context, or another context sharing resources with it, that was current on the thread when invoking :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTextureBlitter.create` is current.

The function has no effect when the blitter is not in created state.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTextureBlitter.create`.
