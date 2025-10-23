.. sip:method-description::
    :status: todo
    :pysig: 06c647d5dc3aec482fcc4048c9f2772d
    :realsig: (uint, uint, QSize, int, int, QQuickRenderTarget::Flags)
    :digest: cfa5236ad9c8e317e0ab1afac39997a4

Returns a new :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` referencing an OpenGL 2D texture or texture array object specified by *textureId*.

*format* specifies the native internal format of the texture. Only texture formats that are supported by Qt's rendering infrastructure should be used.

*pixelSize* specifies the size of the image, in pixels. Currently only 2D textures and 2D texture arrays are supported.

*sampleCount* specifies the number of samples. 0 or 1 means no multisampling, while a value like 4 or 8 states that the native object is a multisample texture, except when *flags* contains :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget.Flag.MultisampleResolve`. In that case, *textureId* is assumed to be a non-multisample 2D texture or 2D texture array, and *sampleCount* defines the number of samples desired. The resulting :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` will use an intermediate, automatically created multisample texture (or texture array) as its color attachment, and will resolve the samples into *textureId*. This is the recommended approach to perform MSAA when the native OpenGL texture is not already multisample.

When *arraySize* is greater than 1, it implies multiview rendering (`GL_OVR_multiview <https://registry.khronos.org/OpenGL/extensions/OVR/OVR_multiview.txt>`_, QRhiColorAttachment::setMultiViewCount()), which can be relevant with VR/AR especially. In this case *arraySize* is the number of views, typically ``2``. See :sip:ref:`~PyQt6.QtQuick.QSGMaterial.viewCount` for details on enabling multiview rendering within the Qt Quick scenegraph.

A depth-stencil buffer, if applicable, is created and used automatically. When the color buffer is multisample, the depth-stencil buffer will automatically be multisample too. For multiview rendering, the depth-stencil texture will automatically be made an array with a matching *arraySize*.

The OpenGL object name *textureId* must be a valid 2D texture name in the rendering context used by the Qt Quick scenegraph. When *arraySize* is greater than 1, *textureId* must be a valid 2D texture array name.

**Note:** the resulting :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` does not own any native resources, it merely contains references and the associated metadata of the size and sample count. It is the caller's responsibility to ensure that the native resource exists as long as necessary.

**Note:** The implementation of this overload is not compatible with OpenGL ES 2.0 or 3.0, and requires OpenGL ES 3.1 at minimum. (or OpenGL 3.0 on desktop)

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setRenderTarget`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget.fromOpenGLTexture`.
