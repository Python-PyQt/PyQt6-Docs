.. sip:class-description::
    :status: todo
    :brief: A QFrameGraphNode used to select QTechniques to use
    :realname: Qt3DRender::QTechniqueFilter
    :digest: 7c9de2e78bee7b7d7f254088b2beabbc

A QFrameGraphNode used to select QTechniques to use.

A :sip:ref:`~PyQt6.Qt3DRender.QTechniqueFilter` specifies which techniques are used by the FrameGraph when rendering the entities. :sip:ref:`~PyQt6.Qt3DRender.QTechniqueFilter` specifies a list of :sip:ref:`~PyQt6.Qt3DRender.QFilterKey` objects and :sip:ref:`~PyQt6.Qt3DRender.QParameter` objects. When :sip:ref:`~PyQt6.Qt3DRender.QTechniqueFilter` is present in the FrameGraph, only the techiques matching the keys in the list are used for rendering. The parameters in the list can be used to set values for shader parameters. The parameters in :sip:ref:`~PyQt6.Qt3DRender.QTechniqueFilter` override parameters in QMaterial, QEffect, QTechnique and QRenderPass, but are overridden by parameters in QRenderPassFilter.
