:orphan:

.. sip:class:: PyQt6.Qt3DRender.QLevelOfDetail
    :inherits: :sip:ref:`~PyQt6.Qt3DCore.QComponent`
    :description: Qt3DRender/QLevelOfDetail-c.rst

    .. sip:enum:: PyQt6.Qt3DRender.QLevelOfDetail.ThresholdType
        :description: Qt3DRender/QLevelOfDetail-ThresholdType-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QLevelOfDetail.ThresholdType.DistanceToCameraThreshold
            :description: Qt3DRender/QLevelOfDetail-ThresholdType-DistanceToCameraThreshold-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QLevelOfDetail.ThresholdType.ProjectedScreenPixelSizeThreshold
            :description: Qt3DRender/QLevelOfDetail-ThresholdType-ProjectedScreenPixelSizeThreshold-v.rst

    .. sip:method:: PyQt6.Qt3DRender.QLevelOfDetail.__init__
        :args:
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DRender/QLevelOfDetail-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLevelOfDetail.camera
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QCamera`
        :description: Qt3DRender/QLevelOfDetail-camera-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLevelOfDetail.createBoundingSphere
        :args:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            float
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QLevelOfDetailBoundingSphere`
        :description: Qt3DRender/QLevelOfDetail-createBoundingSphere-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLevelOfDetail.currentIndex
        :returns:
            int
        :description: Qt3DRender/QLevelOfDetail-currentIndex-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLevelOfDetail.setCamera
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QCamera`
        :description: Qt3DRender/QLevelOfDetail-setCamera-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLevelOfDetail.setCurrentIndex
        :args:
            int
        :description: Qt3DRender/QLevelOfDetail-setCurrentIndex-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLevelOfDetail.setThresholds
        :args:
            Iterable[float]
        :description: Qt3DRender/QLevelOfDetail-setThresholds-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLevelOfDetail.setThresholdType
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QLevelOfDetail.ThresholdType`
        :description: Qt3DRender/QLevelOfDetail-setThresholdType-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLevelOfDetail.setVolumeOverride
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QLevelOfDetailBoundingSphere`
        :description: Qt3DRender/QLevelOfDetail-setVolumeOverride-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLevelOfDetail.thresholds
        :returns:
            List[float]
        :description: Qt3DRender/QLevelOfDetail-thresholds-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLevelOfDetail.thresholdType
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QLevelOfDetail.ThresholdType`
        :description: Qt3DRender/QLevelOfDetail-thresholdType-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QLevelOfDetail.volumeOverride
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QLevelOfDetailBoundingSphere`
        :description: Qt3DRender/QLevelOfDetail-volumeOverride-f.rst

    .. sip:signal:: PyQt6.Qt3DRender.QLevelOfDetail.cameraChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QCamera`
        :description: Qt3DRender/QLevelOfDetail-cameraChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QLevelOfDetail.currentIndexChanged
        :args:
            int
        :description: Qt3DRender/QLevelOfDetail-currentIndexChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QLevelOfDetail.thresholdsChanged
        :args:
            Iterable[float]
        :description: Qt3DRender/QLevelOfDetail-thresholdsChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QLevelOfDetail.thresholdTypeChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QLevelOfDetail.ThresholdType`
        :description: Qt3DRender/QLevelOfDetail-thresholdTypeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QLevelOfDetail.volumeOverrideChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QLevelOfDetailBoundingSphere`
        :description: Qt3DRender/QLevelOfDetail-volumeOverrideChanged-s.rst
