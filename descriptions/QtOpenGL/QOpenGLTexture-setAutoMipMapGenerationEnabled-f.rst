.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 5dd543fea623fb0520ead408a044faad

If *enabled* is ``true``, enables automatic mipmap generation for this texture object to occur whenever the level 0 mipmap data is set via :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.setData`.

The automatic mipmap generation is enabled by default.

**Note:** Mipmap generation is not supported for compressed textures with OpenGL ES 2.0.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.isAutoMipMapGenerationEnabled`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.generateMipMaps`.
