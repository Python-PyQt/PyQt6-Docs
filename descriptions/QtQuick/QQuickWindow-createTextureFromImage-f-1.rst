.. sip:method-description::
    :status: todo
    :pysig: 4a095f85395cd7c7c9943c25bcbdfa4c
    :realsig: (const QImage&,QQuickWindow::CreateTextureOptions) const
    :digest: d3abaa7a9538482a7ae57360bc0ef99e

Creates a new :sip:ref:`~PyQt6.QtQuick.QSGTexture` from the supplied *image*. If the image has an alpha channel, the corresponding texture will have an alpha channel.

The caller of the function is responsible for deleting the returned texture. The underlying native texture object is then destroyed together with the :sip:ref:`~PyQt6.QtQuick.QSGTexture`.

When *options* contains :sip:ref:`~PyQt6.QtQuick.QQuickWindow.CreateTextureOptions.TextureCanUseAtlas`, the engine may put the image into a texture atlas. Textures in an atlas need to rely on :sip:ref:`~PyQt6.QtQuick.QSGTexture.normalizedTextureSubRect` for their geometry and will not support :sip:ref:`~PyQt6.QtQuick.QSGTexture.WrapMode.Repeat`. Other values from :sip:ref:`~PyQt6.QtQuick.QQuickWindow.CreateTextureOptions.CreateTextureOption` are ignored.

When *options* contains :sip:ref:`~PyQt6.QtQuick.QQuickWindow.CreateTextureOptions.TextureIsOpaque`, the engine will create an RGB texture which returns false for :sip:ref:`~PyQt6.QtQuick.QSGTexture.hasAlphaChannel`. Opaque textures will in most cases be faster to render. When this flag is not set, the texture will have an alpha channel based on the image's format.

When *options* contains :sip:ref:`~PyQt6.QtQuick.QQuickWindow.CreateTextureOptions.TextureHasMipmaps`, the engine will create a texture which can use mipmap filtering. Mipmapped textures can not be in an atlas.

When the scene graph uses OpenGL, the returned texture will be using ``GL_TEXTURE_2D`` as texture target and ``GL_RGBA`` as internal format. With other graphics APIs, the texture format is typically ``RGBA8``. Reimplement :sip:ref:`~PyQt6.QtQuick.QSGTexture` to create textures with different parameters.

**Warning:** This function will return 0 if the scene graph has not yet been initialized.

**Warning:** The returned texture is not memory managed by the scene graph and must be explicitly deleted by the caller on the rendering thread. This is achieved by deleting the texture from a :sip:ref:`~PyQt6.QtQuick.QSGNode` destructor or by using deleteLater() in the case where the texture already has affinity to the rendering thread.

This function can be called from any thread.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInitialized`, :sip:ref:`~PyQt6.QtQuick.QSGTexture`.
