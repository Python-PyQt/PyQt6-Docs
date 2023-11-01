:orphan:

.. sip:class:: PyQt6.Qt3DAnimation.QMorphingAnimation
    :inherits: :sip:ref:`~PyQt6.Qt3DAnimation.QAbstractAnimation`
    :description: Qt3DAnimation/QMorphingAnimation-c.rst

    .. sip:enum:: PyQt6.Qt3DAnimation.QMorphingAnimation.Method
        :description: Qt3DAnimation/QMorphingAnimation-Method-e.rst

        .. sip:enum-member:: PyQt6.Qt3DAnimation.QMorphingAnimation.Method.Normalized
            :description: Qt3DAnimation/QMorphingAnimation-Method-Normalized-v.rst

        .. sip:enum-member:: PyQt6.Qt3DAnimation.QMorphingAnimation.Method.Relative
            :description: Qt3DAnimation/QMorphingAnimation-Method-Relative-v.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: Qt3DAnimation/QMorphingAnimation-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.addMorphTarget
        :args:
            :sip:ref:`~PyQt6.Qt3DAnimation.QMorphTarget`
        :description: Qt3DAnimation/QMorphingAnimation-addMorphTarget-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.easing
        :returns:
            :sip:ref:`~PyQt6.QtCore.QEasingCurve`
        :description: Qt3DAnimation/QMorphingAnimation-easing-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.getWeights
        :args:
            int
        :returns:
            List[float]
        :description: Qt3DAnimation/QMorphingAnimation-getWeights-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.interpolator
        :returns:
            float
        :description: Qt3DAnimation/QMorphingAnimation-interpolator-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.method
        :returns:
            :sip:ref:`~PyQt6.Qt3DAnimation.QMorphingAnimation.Method`
        :description: Qt3DAnimation/QMorphingAnimation-method-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.morphTargetList
        :returns:
            List[:sip:ref:`~PyQt6.Qt3DAnimation.QMorphTarget`]
        :description: Qt3DAnimation/QMorphingAnimation-morphTargetList-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.removeMorphTarget
        :args:
            :sip:ref:`~PyQt6.Qt3DAnimation.QMorphTarget`
        :description: Qt3DAnimation/QMorphingAnimation-removeMorphTarget-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.setEasing
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QEasingCurve`, :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type`]
        :description: Qt3DAnimation/QMorphingAnimation-setEasing-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.setMethod
        :args:
            :sip:ref:`~PyQt6.Qt3DAnimation.QMorphingAnimation.Method`
        :description: Qt3DAnimation/QMorphingAnimation-setMethod-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.setMorphTargets
        :args:
            Iterable[:sip:ref:`~PyQt6.Qt3DAnimation.QMorphTarget`]
        :description: Qt3DAnimation/QMorphingAnimation-setMorphTargets-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.setTarget
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QGeometryRenderer`
        :description: Qt3DAnimation/QMorphingAnimation-setTarget-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.setTargetName
        :args:
            Optional[str]
        :description: Qt3DAnimation/QMorphingAnimation-setTargetName-f-1.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.setTargetPositions
        :args:
            Iterable[float]
        :description: Qt3DAnimation/QMorphingAnimation-setTargetPositions-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.setWeights
        :args:
            int
            Iterable[float]
        :description: Qt3DAnimation/QMorphingAnimation-setWeights-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.target
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QGeometryRenderer`
        :description: Qt3DAnimation/QMorphingAnimation-target-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.targetName
        :returns:
            str
        :description: Qt3DAnimation/QMorphingAnimation-targetName-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QMorphingAnimation.targetPositions
        :returns:
            List[float]
        :description: Qt3DAnimation/QMorphingAnimation-targetPositions-f.rst

    .. sip:signal:: PyQt6.Qt3DAnimation.QMorphingAnimation.easingChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QEasingCurve`, :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type`]
        :description: Qt3DAnimation/QMorphingAnimation-easingChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DAnimation.QMorphingAnimation.interpolatorChanged
        :args:
            float
        :description: Qt3DAnimation/QMorphingAnimation-interpolatorChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DAnimation.QMorphingAnimation.methodChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DAnimation.QMorphingAnimation.Method`
        :description: Qt3DAnimation/QMorphingAnimation-methodChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DAnimation.QMorphingAnimation.targetChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QGeometryRenderer`
        :description: Qt3DAnimation/QMorphingAnimation-targetChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DAnimation.QMorphingAnimation.targetNameChanged
        :args:
            Optional[str]
        :description: Qt3DAnimation/QMorphingAnimation-targetNameChanged-s-1.rst

    .. sip:signal:: PyQt6.Qt3DAnimation.QMorphingAnimation.targetPositionsChanged
        :args:
            Iterable[float]
        :description: Qt3DAnimation/QMorphingAnimation-targetPositionsChanged-s.rst
