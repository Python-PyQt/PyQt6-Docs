.. sip:class-description::
    :status: todo
    :brief: Base class of all FrameGraph configuration nodes
    :realname: Qt3DRender::QFrameGraphNode
    :digest: b39ed206e3e050d97b84f6e09c24fbd8

Base class of all FrameGraph configuration nodes.

This class is rarely instanced directly since it doesn't provide any frame graph specific behavior, although it can be convenient to use for grouping other nodes together in dynamic frame graphs. The actual behavior comes from the subclasses.

The subclasses are:

+-----------------------------------------------------+---------------------------------------------------------+
| class                                               | description                                             |
+=====================================================+=========================================================+
| :sip:ref:`~PyQt6.Qt3DRender.QCameraSelector`        | Select camera from all available cameras in the scene   |
+-----------------------------------------------------+---------------------------------------------------------+
| :sip:ref:`~PyQt6.Qt3DRender.QClearBuffers`          | Specify which buffers to clear and to what values       |
+-----------------------------------------------------+---------------------------------------------------------+
| :sip:ref:`~PyQt6.Qt3DRender.QDispatchCompute`       | Specify Compute operation kernels                       |
+-----------------------------------------------------+---------------------------------------------------------+
| :sip:ref:`~PyQt6.Qt3DRender.QFrustumCulling`        | Enable frustum culling                                  |
+-----------------------------------------------------+---------------------------------------------------------+
| :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter`           | Select which layers to draw                             |
+-----------------------------------------------------+---------------------------------------------------------+
| :sip:ref:`~PyQt6.Qt3DRender.QNoDraw`                | Disable drawing                                         |
+-----------------------------------------------------+---------------------------------------------------------+
| :sip:ref:`~PyQt6.Qt3DRender.QRenderPassFilter`      | Select which render passes to draw                      |
+-----------------------------------------------------+---------------------------------------------------------+
| :sip:ref:`~PyQt6.Qt3DRender.QRenderStateSet`        | Set render states                                       |
+-----------------------------------------------------+---------------------------------------------------------+
| :sip:ref:`~PyQt6.Qt3DRender.QRenderSurfaceSelector` | Select which surface to draw to                         |
+-----------------------------------------------------+---------------------------------------------------------+
| :sip:ref:`~PyQt6.Qt3DRender.QRenderTargetSelector`  | Select which QRenderTarget to draw to                   |
+-----------------------------------------------------+---------------------------------------------------------+
| :sip:ref:`~PyQt6.Qt3DRender.QSortPolicy`            | Specify how entities are sorted to determine draw order |
+-----------------------------------------------------+---------------------------------------------------------+
| :sip:ref:`~PyQt6.Qt3DRender.QTechniqueFilter`       | Select which techniques to draw                         |
+-----------------------------------------------------+---------------------------------------------------------+
| :sip:ref:`~PyQt6.Qt3DRender.QViewport`              | Specify viewport                                        |
+-----------------------------------------------------+---------------------------------------------------------+
| :sip:ref:`~PyQt6.Qt3DRender.QMemoryBarrier`         | Places a memory barrier                                 |
+-----------------------------------------------------+---------------------------------------------------------+
