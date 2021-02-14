.. sip:class-description::
    :status: todo
    :brief: Encapsulates a target (usually a frame buffer object) which the renderer can render into
    :realname: Qt3DRender::QRenderTarget
    :digest: 50489cba849fed21e669837e44961f56

The :sip:ref:`~PyQt6.Qt3DRender.QRenderTarget` class encapsulates a target (usually a frame buffer object) which the renderer can render into.

A :sip:ref:`~PyQt6.Qt3DRender.QRenderTarget` comprises of :sip:ref:`~PyQt6.Qt3DRender.QRenderTargetOutput` objects, which specify the the buffers the render target is rendering to. The user can specify MRT(Multiple Render Targets) by attaching multiple textures to different attachment points. The results are undefined if the user tries to attach multiple textures to the same attachment point. At render time, only the draw buffers specified in the :sip:ref:`~PyQt6.Qt3DRender.QRenderTargetSelector` are used.
