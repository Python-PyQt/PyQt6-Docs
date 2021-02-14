.. sip:class-description::
    :status: todo
    :brief: Controls layers drawn in a frame graph branch
    :realname: Qt3DRender::QLayerFilter
    :digest: 0d2285dfe48c04e316f077fdbab4d963

Controls layers drawn in a frame graph branch.

A :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter` can be used to instruct the renderer as to which layer(s) to draw in that branch of the frame graph. :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter` selects which entities to draw based on the QLayer instance(s) added to the :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter` and as components to :sip:ref:`~PyQt6.Qt3DCore.QEntity`.

:sip:ref:`~PyQt6.Qt3DRender.QLayerFilter` can be configured to select or discard entities with a specific QLayer depending on the :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter.filterMode` property. By default, entities referencing one of the QLayer objects that are also being referenced by the :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter` are selected (\ :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter.FilterMode.AcceptAnyMatchingLayers`).

Within the FrameGraph tree, multiple :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter` nodes can be nested within a branch going from root to a leaf. In that case the filtering will first operate on all entities of the scene using the filtering method specified by the first declared :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter`. Then the filtered subset of entities will be filtered again based on the filtering method set on the second :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter` declared. This is then repeated until all :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter` nodes of the branch have been consumed.
