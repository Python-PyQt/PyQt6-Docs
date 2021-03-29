.. sip:class-description::
    :status: todo
    :brief: The base class for types providing animation playback capabilities
    :realname: Qt3DAnimation::QAbstractClipAnimator
    :digest: 5b5a3811ba52d37e59a2ff454caaa255

:sip:ref:`~PyQt6.Qt3DAnimation.QAbstractClipAnimator` is the base class for types providing animation playback capabilities.

Subclasses of :sip:ref:`~PyQt6.Qt3DAnimation.QAbstractClipAnimator` can be aggregated by a QEntity to provide animation capabilities. The animator components provide an interface for controlling the animation (e.g. start, stop). Each animator type requires some form of animation data such as a QAbstractAnimationClip as well as a QChannelMapper which describes how the channels in the animation clip should be mapped onto the properties of the objects you wish to animate.

The following subclasses are available:

* :sip:ref:`~PyQt6.Qt3DAnimation.QClipAnimator`

* :sip:ref:`~PyQt6.Qt3DAnimation.QBlendedClipAnimator`
