.. sip:method-description::
    :status: todo
    :pysig: 1e7e9349b5488b3cd316afe38e65f59b
    :realsig: (QOpenGLTexture::Target,QOpenGLTexture::TextureFormat,int,int,int,int) const
    :digest: 5a53165a352629949cc33c661bc40064

Attempts to create a texture view onto this texture. A texture view is somewhat analogous to a view in SQL in that it presents a restricted or reinterpreted view of the original data. Texture views do not allocate any more server-side storage, instead relying on the storage buffer of the source texture.

Texture views are only available when using immutable storage. For more information on texture views see http://www.opengl.org/wiki/Texture_Storage#Texture_views.

The *target* argument specifies the target to use for the view. Only some targets can be used depending upon the target of the original target. For e.g. a view onto a :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.Target.Target1DArray` texture can specify either :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.Target.Target1DArray` or :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.Target.Target1D` but for the latter the number of array layers specified with *minimumLayer* and *maximumLayer* must be exactly 1.

Simpliar constraints apply for the *viewFormat*. See the above link and the specification for more details.

The *minimumMipmapLevel*, *maximumMipmapLevel*, *minimumLayer*, and *maximumLayer* arguments serve to restrict the parts of the texture accessible by the texture view.

If creation of the texture view fails this function will return 0. If the function succeeds it will return a pointer to a new :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture` object that will return ``true`` from its :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.isTextureView` function.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTexture.isTextureView`.
