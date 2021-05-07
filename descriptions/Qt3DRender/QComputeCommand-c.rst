.. sip:class-description::
    :status: todo
    :brief: QComponent to issue work for the compute shader on GPU
    :realname: Qt3DRender::QComputeCommand
    :digest: 1034d234a47a32ea4197f5aaf046b345

QComponent to issue work for the compute shader on GPU.

A :sip:ref:`~PyQt6.Qt3DRender.QComputeCommand` is used to issue work for the compute shader. The compute shader is specified in the QMaterial component of the same entity the :sip:ref:`~PyQt6.Qt3DRender.QComputeCommand` is added to. The :sip:ref:`~PyQt6.Qt3DRender.QComputeCommand.workGroupX`, :sip:ref:`~PyQt6.Qt3DRender.QComputeCommand.workGroupY` and :sip:ref:`~PyQt6.Qt3DRender.QComputeCommand.workGroupZ` properties specify the work group sizes for the compute shader invocation. :sip:ref:`~PyQt6.Qt3DRender.QDispatchCompute` node needs to be present in the FrameGraph to actually issue the commands.

**Note:** If the rendering policy is set to :sip:ref:`~PyQt6.Qt3DRender.QRenderSettings.RenderPolicy.OnDemand` and there are no changes to the scene, the `ComputeCommand <https://doc.qt.io/qt-6/qml-qt3d-render-computecommand.html>`_ will not be invoked repeatedly. The :sip:ref:`~PyQt6.Qt3DRender.QRenderSettings.RenderPolicy.Always` render policy must be set for the `ComputeCommand <https://doc.qt.io/qt-6/qml-qt3d-render-computecommand.html>`_ to be repeatedly invoked if there are no other changes to the scene that triggers rendering a new frame.
