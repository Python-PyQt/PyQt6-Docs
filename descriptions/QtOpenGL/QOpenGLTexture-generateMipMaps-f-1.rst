.. sip:method-description::
    :status: todo
    :pysig: 31bae3f7ceabcdbf1d8a45e3128d74c8
    :realsig: (int,bool)
    :digest: 41d86dbfe2c6144efc7b630a84845870

Generates mipmaps for this texture object from mipmap level *baseLevel*. If you are using a texture target and filtering option that requires mipmaps and you have disabled automatic mipmap generation then you need to call this function or the overload to create the mipmap chain.

The generation of mipmaps to above *baseLevel* is achieved by setting the mipmap base level to *baseLevel* and then generating the mipmap chain. If *resetBaseLevel* is ``true``, then the baseLevel of the texture will be reset to its previous value.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.setAutoMipMapGenerationEnabled`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.setMipLevels`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.mipLevels`.
