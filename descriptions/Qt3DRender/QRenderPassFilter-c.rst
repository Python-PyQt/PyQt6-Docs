.. sip:class-description::
    :status: todo
    :brief: Provides storage for vectors of Filter Keys and Parameters
    :realname: Qt3DRender::QRenderPassFilter
    :digest: 486d8817f43b8df2a9d7105c345d6ee4

Provides storage for vectors of Filter Keys and Parameters.

A :sip:ref:`~PyQt6.Qt3DRender.QRenderPassFilter` FrameGraph node is used to select which :sip:ref:`~PyQt6.Qt3DRender.QRenderPass` objects are selected for drawing. :sip:ref:`~PyQt6.Qt3DRender.QRenderPassFilter` specifies a list of :sip:ref:`~PyQt6.Qt3DRender.QFilterKey` objects and :sip:ref:`~PyQt6.Qt3DRender.QParameter` objects. When :sip:ref:`~PyQt6.Qt3DRender.QRenderPassFilter` is present in the FrameGraph, only the QRenderPass objects, whose :sip:ref:`~PyQt6.Qt3DRender.QFilterKey` objects match the keys in :sip:ref:`~PyQt6.Qt3DRender.QRenderPassFilter` are selected for rendering. If no :sip:ref:`~PyQt6.Qt3DRender.QRenderPassFilter` is present, then all QRenderPass objects are selected for rendering. The parameters in the list can be used to set values for shader parameters. The parameters in :sip:ref:`~PyQt6.Qt3DRender.QRenderPassFilter` are overridden by parameters in QTechniqueFilter, QTechnique and QRenderPass.
