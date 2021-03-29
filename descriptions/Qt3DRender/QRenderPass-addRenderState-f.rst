.. sip:method-description::
    :status: todo
    :pysig: 99d9ece0666ecbdf9c11120660c54698
    :realname: Qt3DRender::QRenderPass::addRenderState
    :realsig: (Qt3DRender::QRenderState*)
    :digest: 8fb2570e468ead415a9c37bf6b90330c

Adds a render *state* to the rendering pass. That implies that when the pass is executed at render time, the globally set render state will be modified by the states defined locally by the :sip:ref:`~PyQt6.Qt3DRender.QRenderPass`.

**Note:** not defining any :sip:ref:`~PyQt6.Qt3DRender.QRenderState` in a pass will result in the pass using the globally set render state for a given FrameGraph branch execution path.
