.. sip:method-description::
    :status: todo
    :pysig: 2897ad28422feb81fb69591826b72180
    :realsig: (uint,const QSize&,int)
    :digest: 6450e7b7a370f15ae2b41f8d3772cda0

Returns a new :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` referencing an OpenGL texture object specified by *textureId*. The texture is assumed to have a format of GL_RGBA (GL_RGBA8).

*pixelSize* specifies the size of the image, in pixels. Currently only 2D textures are supported.

*sampleCount* specifies the number of samples. 0 or 1 means no multisampling, while a value like 4 or 8 states that the native object is a multisample texture.

The texture is used as the first color attachment of the render target used by the Qt Quick scenegraph. A depth-stencil buffer, if applicable, is created and used automatically.

The OpenGL object name *textureId* must be a valid name in the rendering context used by the Qt Quick scenegraph.

**Note:** the resulting :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` does not own any native resources, it merely contains references and the associated metadata of the size and sample count. It is the caller's responsibility to ensure that the native resource exists as long as necessary.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setRenderTarget`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`.
