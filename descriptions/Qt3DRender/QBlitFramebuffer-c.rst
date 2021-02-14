.. sip:class-description::
    :status: todo
    :brief: FrameGraph node to transfer a rectangle of pixel values from one region of a render target to another
    :realname: Qt3DRender::QBlitFramebuffer
    :digest: c6647fb2f06442acf44c5b94f915d40d

FrameGraph node to transfer a rectangle of pixel values from one region of a render target to another.

This node inserts a ``glBlitFrameBuffer`` or an equivalent into the command stream. This provides a more efficient method for copying rectangles between textures or surface backbuffers wrapped by QRenderTarget than drawing textured quads. It also supports scaling with the specified interpolation method.

**Note:** In practice the :sip:ref:`~PyQt6.Qt3DRender.QBlitFramebuffer` node will often be used in combination with QNoDraw since a blit should not involve issuing draw calls for any entities.
