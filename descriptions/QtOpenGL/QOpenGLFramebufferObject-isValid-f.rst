.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 153e4c2895df78759084b665288cdd2e

Returns ``true`` if the framebuffer object is valid.

The framebuffer can become invalid if the initialization process fails, the user attaches an invalid buffer to the framebuffer object, or a non-power of two width/height is specified as the texture size if the texture target is ``GL_TEXTURE_2D``. The non-power of two limitation does not apply if the OpenGL version is 2.0 or higher, or if the GL_ARB_texture_non_power_of_two extension is present.

The framebuffer can also become invalid if the `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ that the framebuffer was created within is destroyed and there are no other shared contexts that can take over ownership of the framebuffer.
