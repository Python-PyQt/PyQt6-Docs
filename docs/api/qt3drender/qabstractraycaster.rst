:orphan:

.. sip:class:: PyQt6.Qt3DRender.QAbstractRayCaster
    :inherits: :sip:ref:`~PyQt6.Qt3DCore.QComponent`
    :description: Qt3DRender/QAbstractRayCaster-c.rst

    .. sip:enum:: PyQt6.Qt3DRender.QAbstractRayCaster.FilterMode
        :description: Qt3DRender/QAbstractRayCaster-FilterMode-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QAbstractRayCaster.FilterMode.AcceptAllMatchingLayers
            :description: Qt3DRender/QAbstractRayCaster-FilterMode-AcceptAllMatchingLayers-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QAbstractRayCaster.FilterMode.AcceptAnyMatchingLayers
            :description: Qt3DRender/QAbstractRayCaster-FilterMode-AcceptAnyMatchingLayers-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QAbstractRayCaster.FilterMode.DiscardAllMatchingLayers
            :description: Qt3DRender/QAbstractRayCaster-FilterMode-DiscardAllMatchingLayers-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QAbstractRayCaster.FilterMode.DiscardAnyMatchingLayers
            :description: Qt3DRender/QAbstractRayCaster-FilterMode-DiscardAnyMatchingLayers-v.rst

    .. sip:enum:: PyQt6.Qt3DRender.QAbstractRayCaster.RunMode
        :description: Qt3DRender/QAbstractRayCaster-RunMode-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QAbstractRayCaster.RunMode.Continuous
            :description: Qt3DRender/QAbstractRayCaster-RunMode-Continuous-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QAbstractRayCaster.RunMode.SingleShot
            :description: Qt3DRender/QAbstractRayCaster-RunMode-SingleShot-v.rst

    .. sip:method:: PyQt6.Qt3DRender.QAbstractRayCaster.__init__
        :args:
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DRender/QAbstractRayCaster-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QAbstractRayCaster.addLayer
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QLayer`
        :description: Qt3DRender/QAbstractRayCaster-addLayer-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QAbstractRayCaster.filterMode
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QAbstractRayCaster.FilterMode`
        :description: Qt3DRender/QAbstractRayCaster-filterMode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QAbstractRayCaster.hits
        :returns:
            list[:sip:ref:`~PyQt6.Qt3DRender.QRayCasterHit`]
        :description: Qt3DRender/QAbstractRayCaster-hits-f-1.rst

    .. sip:method:: PyQt6.Qt3DRender.QAbstractRayCaster.layers
        :returns:
            list[:sip:ref:`~PyQt6.Qt3DRender.QLayer`]
        :description: Qt3DRender/QAbstractRayCaster-layers-f-1.rst

    .. sip:method:: PyQt6.Qt3DRender.QAbstractRayCaster.removeLayer
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QLayer`
        :description: Qt3DRender/QAbstractRayCaster-removeLayer-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QAbstractRayCaster.runMode
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QAbstractRayCaster.RunMode`
        :description: Qt3DRender/QAbstractRayCaster-runMode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QAbstractRayCaster.setFilterMode
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QAbstractRayCaster.FilterMode`
        :description: Qt3DRender/QAbstractRayCaster-setFilterMode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QAbstractRayCaster.setRunMode
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QAbstractRayCaster.RunMode`
        :description: Qt3DRender/QAbstractRayCaster-setRunMode-f.rst

    .. sip:signal:: PyQt6.Qt3DRender.QAbstractRayCaster.filterModeChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QAbstractRayCaster.FilterMode`
        :description: Qt3DRender/QAbstractRayCaster-filterModeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QAbstractRayCaster.hitsChanged
        :args:
            Iterable[:sip:ref:`~PyQt6.Qt3DRender.QRayCasterHit`]
        :description: Qt3DRender/QAbstractRayCaster-hitsChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QAbstractRayCaster.runModeChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QAbstractRayCaster.RunMode`
        :description: Qt3DRender/QAbstractRayCaster-runModeChanged-s.rst
