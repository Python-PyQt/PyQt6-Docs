.. sip:class-description::
    :status: todo
    :brief: Default FrameGraph implementation of a forward renderer
    :realname: Qt3DExtras::QForwardRenderer
    :digest: 4206a5151ab7337e73fd8fb024908da1

The :sip:ref:`~PyQt6.Qt3DExtras.QForwardRenderer` provides a default `FrameGraph <https://doc.qt.io/qt-6/qt3drender-framegraph.html>`_ implementation of a forward renderer.

Forward rendering is what OpenGL traditionally uses. It renders directly to the backbuffer one object at a time shading each one as it goes.

:sip:ref:`~PyQt6.Qt3DExtras.QForwardRenderer` is a single leaf `FrameGraph <https://doc.qt.io/qt-6/qt3drender-framegraph.html>`_ tree which contains a :sip:ref:`~PyQt6.Qt3DRender.QViewport`, a :sip:ref:`~PyQt6.Qt3DRender.QCameraSelector`, and a :sip:ref:`~PyQt6.Qt3DRender.QClearBuffers`. The :sip:ref:`~PyQt6.Qt3DExtras.QForwardRenderer` has a default requirement filter key whose name is "renderingStyle" and value "forward". If you need to filter out your techniques, you should do so based on that filter key.

By default the viewport occupies the whole screen and the clear color is white. Frustum culling is also enabled.
