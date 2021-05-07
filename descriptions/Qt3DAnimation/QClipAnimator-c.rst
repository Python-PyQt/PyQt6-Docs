.. sip:class-description::
    :status: todo
    :brief: Component providing simple animation playback capabilities
    :realname: Qt3DAnimation::QClipAnimator
    :digest: 7982440da7f89a503d3b93d2b3ddfc0d

:sip:ref:`~PyQt6.Qt3DAnimation.QClipAnimator` is a component providing simple animation playback capabilities.

An instance of :sip:ref:`~PyQt6.Qt3DAnimation.QClipAnimator` can be aggregated by a QEntity to add the ability to play back animation clips and to apply the calculated animation values to properties of QObjects.

The animation key frame data is provided via the clip property. This can be created programmatically with QAnimationClip or loaded from file with QAnimationClipLoader.

In order to apply the values played back from the channels of data in the animation clip, the clip animator needs to have a QChannelMapper object assigned to the channelMapper property.

The properties for controlling the animator are provided by the QAbstractClipAnimator base class.

.. seealso:: :sip:ref:`~PyQt6.Qt3DAnimation.QAbstractClipAnimator`, :sip:ref:`~PyQt6.Qt3DAnimation.QAbstractAnimationClip`, :sip:ref:`~PyQt6.Qt3DAnimation.QChannelMapper`, :sip:ref:`~PyQt6.Qt3DAnimation.QBlendedClipAnimator`.
