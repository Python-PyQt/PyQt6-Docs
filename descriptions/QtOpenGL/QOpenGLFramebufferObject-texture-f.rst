.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 1a9a5efe15b20a689d924df053cb9bc9

Returns the texture id for the texture attached as the default rendering target in this framebuffer object. This texture id can be bound as a normal texture in your own OpenGL code.

If a multisample framebuffer object is used then the value returned from this function will be invalid.

When multiple textures are attached, the return value is the ID of the first one.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.takeTexture`, `textures() <https://doc.qt.io/qt-6/qtquick3d-custom.html#textures>`_.
