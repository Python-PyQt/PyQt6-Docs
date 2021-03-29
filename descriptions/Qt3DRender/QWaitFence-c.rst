.. sip:class-description::
    :status: todo
    :brief: FrameGraphNode used to wait for a fence in the graphics command stream to become signaled
    :realname: Qt3DRender::QWaitFence
    :digest: f0f0440c028ceba3b7ffbe89b64e6c5e

`FrameGraphNode <https://doc.qt.io/qt-6/qml-qt3d-render-framegraphnode.html>`_ used to wait for a fence in the graphics command stream to become signaled.

Fence allow to synchronosize GPU and CPU workloads. GPU commands usually are non-blocking. When issued, commands are inserted in command buffers which will be read at a later time by the GPU. In some cases, you want to continue processing or issue specific command only when you are sure a command has been executed by the hardware. Fences are a way to do so. This is especially important when using 3rd party engines with Qt3D, Qt3D should only access shared resources when we know the other engine command are done modifying the resource.

:sip:ref:`~PyQt6.Qt3DRender.QWaitFence` is a FrameGraph node that will force to wait for it to become signaled before subsequent commands are inserted into the command stream. It can then be used in conjunction with QSetFence and contains properties to configure how long it should wait and whether it should block on the CPU side.

**Note:** Qt 3D uploads GPU resources (Texture, Shaders, Buffers) before issuing draw calls.
