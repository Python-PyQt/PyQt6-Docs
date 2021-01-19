:orphan:

.. sip:class:: PyQt6.Qt3DRender.QLayerFilter
    :inherits: :sip:ref:`~PyQt6.Qt3DRender.QFrameGraphNode`
    :description: Qt3DRender/QLayerFilter-c.rst

    .. sip:enum:: PyQt6.Qt3DRender.QLayerFilter.FilterMode
        :description: Qt3DRender/QLayerFilter-FilterMode-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QLayerFilter.FilterMode.AcceptAllMatchingLayers
            :description: Qt3DRender/QLayerFilter-FilterMode-AcceptAllMatchingLayers-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QLayerFilter.FilterMode.AcceptAnyMatchingLayers
            :description: Qt3DRender/QLayerFilter-FilterMode-AcceptAnyMatchingLayers-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QLayerFilter.FilterMode.DiscardAllMatchingLayers
            :description: Qt3DRender/QLayerFilter-FilterMode-DiscardAllMatchingLayers-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QLayerFilter.FilterMode.DiscardAnyMatchingLayers
            :description: Qt3DRender/QLayerFilter-FilterMode-DiscardAnyMatchingLayers-v.rst

    .. sip:method:: PyQt6.Qt3DRender.QLayerFilter.__init__
        :args:
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DRender/QLayerFilter-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLayerFilter.addLayer
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QLayer`
        :description: Qt3DRender/QLayerFilter-addLayer-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLayerFilter.filterMode
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter.FilterMode`
        :description: Qt3DRender/QLayerFilter-filterMode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLayerFilter.layers
        :returns:
            List[:sip:ref:`~PyQt6.Qt3DRender.QLayer`]
        :description: Qt3DRender/QLayerFilter-layers-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLayerFilter.removeLayer
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QLayer`
        :description: Qt3DRender/QLayerFilter-removeLayer-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLayerFilter.setFilterMode
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter.FilterMode`
        :description: Qt3DRender/QLayerFilter-setFilterMode-f.rst

    .. sip:signal:: PyQt6.Qt3DRender.QLayerFilter.filterModeChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QLayerFilter.FilterMode`
        :description: Qt3DRender/QLayerFilter-filterModeChanged-s.rst
