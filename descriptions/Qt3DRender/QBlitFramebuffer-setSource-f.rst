.. sip:method-description::
    :status: todo
    :pysig: e73150d4bce6aecb259fb91a869af338
    :realname: Qt3DRender::QBlitFramebuffer::setSource
    :realsig: (Qt3DRender::QRenderTarget*)
    :digest: 25931e22ca7d26659aec493dd9be35b8

Sets the source render target. The default value is nullptr, in which case the source is assumed to be be the default framebuffer (i.e. the backbuffer of the current surface), if there is one.

**Note:** the source and destination must not refer to the same render target.

**Note:** As with other nodes, *source* gets automatically parented to the :sip:ref:`~PyQt6.Qt3DRender.QBlitFramebuffer` instance when no parent has been set. The lifetime is also tracked, meaning the source reverts to nullptr in case the currently set *source* is destroyed.

.. seealso:: :sip:ref:`~PyQt6.Qt3DRender.QBlitFramebuffer.source`.
