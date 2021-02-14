.. sip:class-description::
    :status: todo
    :brief: When a Qt3DRender::QNoPicking node is present in a FrameGraph branch, this prevents the render aspect from performing picking selection for the given branch
    :realname: Qt3DRender::QNoPicking
    :digest: 08f87ffbb3099e381983d3d3e8306c54

When a :sip:ref:`~PyQt6.Qt3DRender.QNoPicking` node is present in a FrameGraph branch, this prevents the render aspect from performing picking selection for the given branch.

When disabled, a :sip:ref:`~PyQt6.Qt3DRender.QNoPicking` node won't prevent picking from being performed. Toggling the enabled property is therefore a way to make a :sip:ref:`~PyQt6.Qt3DRender.QNoPicking` active or inactive.

When using multiple subviewports in the FrameGraph, :sip:ref:`~PyQt6.Qt3DRender.QNoPicking` can be useful to prevent picking conflicts between overlapping viewports or non visual ones. It can also be used as an optimization to prevent unnecessary work for hidden viewports or for sections of the scenes which don't require any picking.

::

    Qt3DRender::QViewport *viewport = new Qt3DRender::QViewport();
    Qt3DRender::QCameraSelector *cameraSelector = new Qt3DRender::QCameraSelector(viewport);
    Qt3DRender::QNoPicking *noPicking = new Qt3DRender::QNoPicking(cameraSelector);

    Qt3DRender::QClearBuffers *clearBuffers = new Qt3DRender::QClearBuffers(noPicking);
    clearBuffers->setBuffers(Qt3DRender::QClearBuffers::ColorDepthBuffer);

    Qt3DRender::QRenderPassFilter *mainPass = new Qt3DRender::QRenderPassFilter(cameraSelector);
    ....
    Qt3DRender::QRenderPassFilter *previewPass = new Qt3DRender::QRenderPassFilter(cameraSelector);
    ....

.. seealso:: :sip:ref:`~PyQt6.Qt3DRender.QObjectPicker`, :sip:ref:`~PyQt6.Qt3DRender.QRayCaster`, :sip:ref:`~PyQt6.Qt3DRender.QScreenRayCaster`.
