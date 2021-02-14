.. sip:class-description::
    :status: todo
    :brief: FrameGraphNode used to insert a fence in the graphics command stream
    :realname: Qt3DRender::QSetFence
    :digest: 17cd8542b2c7bca830c11016ecd952c4

`FrameGraphNode <https://doc.qt.io/qt-6/qml-qt3d-render-framegraphnode.html>`_ used to insert a fence in the graphics command stream.

Fence allow to synchronosize GPU and CPU workloads. GPU commands usually are non-blocking. When issued, commands are inserted in command buffers which will be read at a later time by the GPU. In some cases, you want to continue processing or issue specific command only when you are sure a command has been executed by the hardware. Fences are a way to do so. This is especially important when using 3rd party engines with Qt3D, Qt3D should only access shared resources when we know the other engine command are done modifying the resource.

:sip:ref:`~PyQt6.Qt3DRender.QSetFence` is a FrameGraph node that inserts a fence into the command stream. It can then be used in conjunction with QWaitFence or by extracting the underlying handle.

The handle property will be updated once the renderer has created the underlying fence resource. The handle will remain valid as long as it remains in the unsignaled state. Once it has reached the signaled state, it will be destroyed and a new handle will be created. That means that depending on how long it takes for the fence to be signaled, the same handle could be used over several frames.
