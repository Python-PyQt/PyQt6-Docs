.. sip:method-description::
    :status: todo
    :pysig: 607401df0e81e7ef41d576d4da31b5d7
    :realsig: (uint,uint,const QSize&,int)
    :digest: 4edcc2552907e7f81250afa0fabce7a0

Returns a new :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` referencing an OpenGL texture object specified by *textureId*.

*format* specifies the native internal format of the texture. Only texture formats that are supported by Qt's rendering infrastructure should be used.

*pixelSize* specifies the size of the image, in pixels. Currently only 2D textures are supported.

*sampleCount* specific the number of samples. 0 or 1 means no multisampling, while a value like 4 or 8 states that the native object is a multisample texture.

The texture is used as the first color attachment of the render target used by the Qt Quick scenegraph. A depth-stencil buffer, if applicable, is created and used automatically.

The OpenGL object name *textureId* must be a valid name in the rendering context used by the Qt Quick scenegraph.

**Note:** the resulting :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` does not own any native resources, it merely contains references and the associated metadata of the size and sample count. It is the caller's responsibility to ensure that the native resource exists as long as necessary.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setRenderTarget`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`.
