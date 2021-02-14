.. sip:class-description::
    :status: todo
    :brief: A QFrameGraphNode used to select QTechniques to use
    :realname: Qt3DRender::QTechniqueFilter
    :digest: 863320746b74a8c2b2f9f1d9178411a5

A QFrameGraphNode used to select QTechniques to use.

A :sip:ref:`~PyQt6.Qt3DRender.QTechniqueFilter` specifies which techniques are used by the FrameGraph when rendering the entities. :sip:ref:`~PyQt6.Qt3DRender.QTechniqueFilter` specifies a list of :sip:ref:`~PyQt6.Qt3DRender.QFilterKey` objects and :sip:ref:`~PyQt6.Qt3DRender.QParameter` objects. When :sip:ref:`~PyQt6.Qt3DRender.QTechniqueFilter` is present in the FrameGraph, only the techiques matching the keys in the list are used for rendering. The parameters in the list can be used to set values for shader parameters. The parameters in :sip:ref:`~PyQt6.Qt3DRender.QTechniqueFilter` are overridden by parameters in QTechnique and QRenderPass.
