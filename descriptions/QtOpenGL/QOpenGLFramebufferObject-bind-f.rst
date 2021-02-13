.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 58269b601cbb779bc1384c66c1fd996b

Switches rendering from the default, windowing system provided framebuffer to this framebuffer object. Returns ``true`` upon success, false otherwise.

**Note:** If :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.takeTexture` was called, a new texture is created and associated with the framebuffer object. This is potentially expensive and changes the context state (the currently bound texture).

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObject.release`.
