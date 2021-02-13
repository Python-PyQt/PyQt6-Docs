.. sip:method-description::
    :status: todo
    :pysig: 2897ad28422feb81fb69591826b72180
    :realsig: (uint,const QSize&,int)
    :digest: db1ce1efcb99bf9b2fb4a3bd74277bb8

Returns a new :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` referencing an OpenGL texture object specified by *textureId*.

*pixelSize* specifies the size of the image, in pixels. Currently only 2D textures are supported.

*sampleCount* specific the number of samples. 0 or 1 means no multisampling, while a value like 4 or 8 states that the native object is a multisample texture.

**Note:** the resulting :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` does not own any native resources, it merely contains references and the associated metadata of the size and sample count. It is the caller's responsibility to ensure that the native resource exists as long as necessary.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setRenderTarget`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`.
