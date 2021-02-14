.. sip:method-description::
    :status: todo
    :pysig: e73150d4bce6aecb259fb91a869af338
    :realname: Qt3DRender::QBlitFramebuffer::setDestination
    :realsig: (Qt3DRender::QRenderTarget*)
    :digest: a477e5374725ab435fc4223ec6d72a09

Sets the destination render target. The default value is nullptr, in which case the destination is assumed to be be the default framebuffer (i.e. the backbuffer of the current surface), if there is one.

**Note:** the source and destination must not refer to the same render target.

**Note:** As with other nodes, *destination* gets automatically parented to the :sip:ref:`~PyQt6.Qt3DRender.QBlitFramebuffer` instance when no parent has been set. The lifetime is also tracked, meaning the destination reverts to nullptr in case the currently set *destination* is destroyed.

.. seealso:: :sip:ref:`~PyQt6.Qt3DRender.QBlitFramebuffer.destination`.
