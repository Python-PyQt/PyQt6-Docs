.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: cf6496749a7c0c8673aed0d425c187c7

Sets the number of samples per pixel for a multisample framebuffer object to *samples*. The default sample count of 0 represents a regular non-multisample framebuffer object.

If the desired amount of samples per pixel is not supported by the hardware then the maximum number of samples per pixel will be used. Note that multisample framebuffer objects cannot be bound as textures. Also, the ``GL_EXT_framebuffer_multisample`` extension is required to create a framebuffer with more than one sample per pixel.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObjectFormat.samples`.
