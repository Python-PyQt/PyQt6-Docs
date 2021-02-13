.. sip:method-description::
    :status: todo
    :pysig: 825230926d80e94ecf0b60e89b634d87
    :realsig: (const QSize&)
    :digest: 0ccaaa884e64e74147e6c3a36b6b75a9

This function is called when a new FBO is needed. This happens on the initial frame. If :sip:ref:`~PyQt6.QtQuick.QQuickFramebufferObject.textureFollowsItemSize` is set to true, it is called again every time the dimensions of the item changes.

The returned FBO can have any attachment. If the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLFramebufferObjectFormat` indicates that the FBO should be multisampled, the internal implementation of the Renderer will allocate a second FBO and blit the multisampled FBO into the FBO used to display the texture.

**Note:** Some hardware has issues with small FBO sizes. *size* takes that into account, so be cautious when overriding the size with a fixed size. A minimal size of 64x64 should always work.

**Note:** *size* takes the device pixel ratio into account, meaning that it is already multiplied by the correct scale factor. When moving the window containing the :sip:ref:`~PyQt6.QtQuick.QQuickFramebufferObject` item to a screen with different settings, the FBO is automatically recreated and this function is invoked with the correct size.
