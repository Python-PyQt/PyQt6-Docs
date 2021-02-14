.. sip:class-description::
    :status: todo
    :brief: A class implementing simple keyframe animation to a QTransform
    :realname: Qt3DAnimation::QKeyframeAnimation
    :digest: 01cccb4f30e9f62faa3439f3a6cd5f97

A class implementing simple keyframe animation to a :sip:ref:`~PyQt6.QtGui.QTransform`.

A :sip:ref:`~PyQt6.Qt3DAnimation.QKeyframeAnimation` class implements simple keyframe animation that can be used to animate :sip:ref:`~PyQt6.QtGui.QTransform`. The keyframes consists of multiple timed QTransforms, which are interpolated and applied to the target :sip:ref:`~PyQt6.QtGui.QTransform`. :sip:ref:`~PyQt6.QtCore.QEasingCurve` is used between keyframes to control the interpolator. :sip:ref:`~PyQt6.Qt3DAnimation.QKeyframeAnimation.RepeatMode.RepeatMode` can be set for when the position set to the :sip:ref:`~PyQt6.Qt3DAnimation.QKeyframeAnimation` is below or above the values defined in the keyframe positions.
