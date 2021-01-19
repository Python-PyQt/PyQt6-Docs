:orphan:

.. sip:class:: PyQt6.Qt3DRender.QPickingSettings
    :inherits: :sip:ref:`~PyQt6.Qt3DCore.QNode`
    :description: Qt3DRender/QPickingSettings-c.rst

    .. sip:enum:: PyQt6.Qt3DRender.QPickingSettings.FaceOrientationPickingMode
        :description: Qt3DRender/QPickingSettings-FaceOrientationPickingMode-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickingSettings.FaceOrientationPickingMode.BackFace
            :description: Qt3DRender/QPickingSettings-FaceOrientationPickingMode-BackFace-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickingSettings.FaceOrientationPickingMode.FrontAndBackFace
            :description: Qt3DRender/QPickingSettings-FaceOrientationPickingMode-FrontAndBackFace-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickingSettings.FaceOrientationPickingMode.FrontFace
            :description: Qt3DRender/QPickingSettings-FaceOrientationPickingMode-FrontFace-v.rst

    .. sip:enum:: PyQt6.Qt3DRender.QPickingSettings.PickMethod
        :description: Qt3DRender/QPickingSettings-PickMethod-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickingSettings.PickMethod.BoundingVolumePicking
            :description: Qt3DRender/QPickingSettings-PickMethod-BoundingVolumePicking-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickingSettings.PickMethod.LinePicking
            :description: Qt3DRender/QPickingSettings-PickMethod-LinePicking-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickingSettings.PickMethod.PointPicking
            :description: Qt3DRender/QPickingSettings-PickMethod-PointPicking-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickingSettings.PickMethod.PrimitivePicking
            :description: Qt3DRender/QPickingSettings-PickMethod-PrimitivePicking-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickingSettings.PickMethod.TrianglePicking
            :description: Qt3DRender/QPickingSettings-PickMethod-TrianglePicking-v.rst

    .. sip:enum:: PyQt6.Qt3DRender.QPickingSettings.PickResultMode
        :description: Qt3DRender/QPickingSettings-PickResultMode-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickingSettings.PickResultMode.AllPicks
            :description: Qt3DRender/QPickingSettings-PickResultMode-AllPicks-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickingSettings.PickResultMode.NearestPick
            :description: Qt3DRender/QPickingSettings-PickResultMode-NearestPick-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickingSettings.PickResultMode.NearestPriorityPick
            :description: Qt3DRender/QPickingSettings-PickResultMode-NearestPriorityPick-v.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickingSettings.__init__
        :args:
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DRender/QPickingSettings-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickingSettings.faceOrientationPickingMode
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings.FaceOrientationPickingMode`
        :description: Qt3DRender/QPickingSettings-faceOrientationPickingMode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickingSettings.pickMethod
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings.PickMethod`
        :description: Qt3DRender/QPickingSettings-pickMethod-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickingSettings.pickResultMode
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings.PickResultMode`
        :description: Qt3DRender/QPickingSettings-pickResultMode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickingSettings.setFaceOrientationPickingMode
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings.FaceOrientationPickingMode`
        :description: Qt3DRender/QPickingSettings-setFaceOrientationPickingMode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickingSettings.setPickMethod
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings.PickMethod`
        :description: Qt3DRender/QPickingSettings-setPickMethod-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickingSettings.setPickResultMode
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings.PickResultMode`
        :description: Qt3DRender/QPickingSettings-setPickResultMode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickingSettings.setWorldSpaceTolerance
        :args:
            float
        :description: Qt3DRender/QPickingSettings-setWorldSpaceTolerance-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickingSettings.worldSpaceTolerance
        :returns:
            float
        :description: Qt3DRender/QPickingSettings-worldSpaceTolerance-f.rst

    .. sip:signal:: PyQt6.Qt3DRender.QPickingSettings.faceOrientationPickingModeChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings.FaceOrientationPickingMode`
        :description: Qt3DRender/QPickingSettings-faceOrientationPickingModeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QPickingSettings.pickMethodChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings.PickMethod`
        :description: Qt3DRender/QPickingSettings-pickMethodChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QPickingSettings.pickResultModeChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QPickingSettings.PickResultMode`
        :description: Qt3DRender/QPickingSettings-pickResultModeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QPickingSettings.worldSpaceToleranceChanged
        :args:
            float
        :description: Qt3DRender/QPickingSettings-worldSpaceToleranceChanged-s.rst
