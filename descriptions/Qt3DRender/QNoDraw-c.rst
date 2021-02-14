.. sip:class-description::
    :status: todo
    :brief: When a Qt3DRender::QNoDraw node is present in a FrameGraph branch, this prevents the renderer from rendering any primitive
    :realname: Qt3DRender::QNoDraw
    :digest: b30f7e8bd1e2b4f3c40daa4f14aced1d

When a :sip:ref:`~PyQt6.Qt3DRender.QNoDraw` node is present in a FrameGraph branch, this prevents the renderer from rendering any primitive.

:sip:ref:`~PyQt6.Qt3DRender.QNoDraw` should be used when the FrameGraph needs to set up some render states or clear some buffers without requiring any mesh to be drawn. It has the same effect as having a :sip:ref:`~PyQt6.Qt3DRender.QRenderPassFilter` that matches none of available :sip:ref:`~PyQt6.Qt3DRender.QRenderPass` instances of the scene without the overhead cost of actually performing the filtering.

When disabled, a :sip:ref:`~PyQt6.Qt3DRender.QNoDraw` node won't prevent the scene from being rendered. Toggling the enabled property is therefore a way to make a :sip:ref:`~PyQt6.Qt3DRender.QNoDraw` active or inactive.

:sip:ref:`~PyQt6.Qt3DRender.QNoDraw` is usually used as a child of a Qt3DRendeR::QClearBuffers node to prevent from drawing the scene when there are multiple render passes.

::

    Qt3DRender::QViewport *viewport = new Qt3DRender::QViewport();
    Qt3DRender::QCameraSelector *cameraSelector = new Qt3DRender::QCameraSelector(viewport);

    Qt3DRender::QClearBuffers *clearBuffers = new Qt3DRender::QClearBuffers(cameraSelector);
    clearBuffers->setBuffers(Qt3DRender::QClearBuffers::ColorDepthBuffer);

    Qt3DRender::QNoDraw *noDraw = new Qt3DRender::QNoDraw(clearBuffers);

    Qt3DRender::QRenderPassFilter *mainPass = new Qt3DRender::QRenderPassFilter(cameraSelector);
    ....
    Qt3DRender::QRenderPassFilter *previewPass = new Qt3DRender::QRenderPassFilter(cameraSelector);
    ....
