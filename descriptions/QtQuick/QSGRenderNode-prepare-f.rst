.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d6cc8301d3326b6104b7fb6e7f61952b

Called from the frame preparation phase. There is a call to this function before each invocation of :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render`.

Unlike :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render`, this function is called before the scenegraph starts recording the render pass for the current frame on the underlying command buffer. This is useful when doing rendering with graphics APIs, such as Vulkan, where copy type of operations will need to be recorded before the render pass.

The default implementation is empty.

When implementing a :sip:ref:`~PyQt6.QtQuick.QSGRenderNode` that uses QRhi to render, query the QRhi object from the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` via QQuickWindow::rhi(). To get a QRhiCommandBuffer for submitting work to, call commandBuffer(). To query information about the active render target, call renderTarget(). See the `{Scene Graph - Custom QSGRenderNode} <https://doc.qt.io/qt-6/qtquick-scenegraph-customrendernode-example.html>`_ example for details.
