.. sip:method-description::
    :status: todo
    :pysig: dcb9ef1e48e3cecf75212871e4cdffdc
    :realsig: (GLuint,QQuickWindow*,const QSize&,QQuickWindow::CreateTextureOptions)
    :digest: f837b3deda6dd23f8762291217d35568

Creates a new :sip:ref:`~PyQt6.QtQuick.QSGTexture` wrapping an existing OpenGL texture object for *window*.

The native object specified in *textureId* is wrapped, but not owned, by the resulting :sip:ref:`~PyQt6.QtQuick.QSGTexture`. The caller of the function is responsible for deleting the returned :sip:ref:`~PyQt6.QtQuick.QSGTexture`, but that will not destroy the underlying native object.

This function is currently suitable for 2D RGBA textures only.

**Warning:** This function will return null if the scenegraph has not yet been initialized.

Use *options* to customize the texture attributes. Only the TextureHasAlphaChannel and TextureHasMipmaps are taken into account here.

*size* specifies the size in pixels.

**Note:** This function must be called on the scenegraph rendering thread.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInitialized`, :sip:ref:`~PyQt6.QtQuick.QSGTexture`, `Scene Graph - Metal Texture Import <https://doc.qt.io/qt-6/qtquick-scenegraph-metaltextureimport-example.html>`_, `Scene Graph - Vulkan Texture Import <https://doc.qt.io/qt-6/qtquick-scenegraph-vulkantextureimport-example.html>`_.
