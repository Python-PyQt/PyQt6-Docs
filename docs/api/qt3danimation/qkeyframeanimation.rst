:orphan:

.. sip:class:: PyQt6.Qt3DAnimation.QKeyframeAnimation
    :inherits: :sip:ref:`~PyQt6.Qt3DAnimation.QAbstractAnimation`
    :description: Qt3DAnimation/QKeyframeAnimation-c.rst

    .. sip:enum:: PyQt6.Qt3DAnimation.QKeyframeAnimation.RepeatMode
        :description: Qt3DAnimation/QKeyframeAnimation-RepeatMode-e.rst

        .. sip:enum-member:: PyQt6.Qt3DAnimation.QKeyframeAnimation.RepeatMode.Constant
            :description: Qt3DAnimation/QKeyframeAnimation-RepeatMode-Constant-v.rst

        .. sip:enum-member:: PyQt6.Qt3DAnimation.QKeyframeAnimation.RepeatMode.None_
            :description: Qt3DAnimation/QKeyframeAnimation-RepeatMode-None_-v.rst

        .. sip:enum-member:: PyQt6.Qt3DAnimation.QKeyframeAnimation.RepeatMode.Repeat
            :description: Qt3DAnimation/QKeyframeAnimation-RepeatMode-Repeat-v.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: Qt3DAnimation/QKeyframeAnimation-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.addKeyframe
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QTransform`
        :description: Qt3DAnimation/QKeyframeAnimation-addKeyframe-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.easing
        :returns:
            :sip:ref:`~PyQt6.QtCore.QEasingCurve`
        :description: Qt3DAnimation/QKeyframeAnimation-easing-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.endMode
        :returns:
            :sip:ref:`~PyQt6.Qt3DAnimation.QKeyframeAnimation.RepeatMode`
        :description: Qt3DAnimation/QKeyframeAnimation-endMode-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.framePositions
        :returns:
            List[float]
        :description: Qt3DAnimation/QKeyframeAnimation-framePositions-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.keyframeList
        :returns:
            List[:sip:ref:`~PyQt6.Qt3DCore.QTransform`]
        :description: Qt3DAnimation/QKeyframeAnimation-keyframeList-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.removeKeyframe
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QTransform`
        :description: Qt3DAnimation/QKeyframeAnimation-removeKeyframe-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.setEasing
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QEasingCurve`, :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type`]
        :description: Qt3DAnimation/QKeyframeAnimation-setEasing-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.setEndMode
        :args:
            :sip:ref:`~PyQt6.Qt3DAnimation.QKeyframeAnimation.RepeatMode`
        :description: Qt3DAnimation/QKeyframeAnimation-setEndMode-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.setFramePositions
        :args:
            Iterable[float]
        :description: Qt3DAnimation/QKeyframeAnimation-setFramePositions-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.setKeyframes
        :args:
            Iterable[:sip:ref:`~PyQt6.Qt3DCore.QTransform`]
        :description: Qt3DAnimation/QKeyframeAnimation-setKeyframes-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.setStartMode
        :args:
            :sip:ref:`~PyQt6.Qt3DAnimation.QKeyframeAnimation.RepeatMode`
        :description: Qt3DAnimation/QKeyframeAnimation-setStartMode-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.setTarget
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QTransform`
        :description: Qt3DAnimation/QKeyframeAnimation-setTarget-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.setTargetName
        :args:
            str
        :description: Qt3DAnimation/QKeyframeAnimation-setTargetName-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.startMode
        :returns:
            :sip:ref:`~PyQt6.Qt3DAnimation.QKeyframeAnimation.RepeatMode`
        :description: Qt3DAnimation/QKeyframeAnimation-startMode-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.target
        :returns:
            :sip:ref:`~PyQt6.Qt3DCore.QTransform`
        :description: Qt3DAnimation/QKeyframeAnimation-target-f.rst

    .. sip:method:: PyQt6.Qt3DAnimation.QKeyframeAnimation.targetName
        :returns:
            str
        :description: Qt3DAnimation/QKeyframeAnimation-targetName-f.rst

    .. sip:signal:: PyQt6.Qt3DAnimation.QKeyframeAnimation.easingChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QEasingCurve`, :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type`]
        :description: Qt3DAnimation/QKeyframeAnimation-easingChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DAnimation.QKeyframeAnimation.endModeChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DAnimation.QKeyframeAnimation.RepeatMode`
        :description: Qt3DAnimation/QKeyframeAnimation-endModeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DAnimation.QKeyframeAnimation.framePositionsChanged
        :args:
            Iterable[float]
        :description: Qt3DAnimation/QKeyframeAnimation-framePositionsChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DAnimation.QKeyframeAnimation.startModeChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DAnimation.QKeyframeAnimation.RepeatMode`
        :description: Qt3DAnimation/QKeyframeAnimation-startModeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DAnimation.QKeyframeAnimation.targetChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QTransform`
        :description: Qt3DAnimation/QKeyframeAnimation-targetChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DAnimation.QKeyframeAnimation.targetNameChanged
        :args:
            str
        :description: Qt3DAnimation/QKeyframeAnimation-targetNameChanged-s.rst
