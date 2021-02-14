.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realname: Qt3DAnimation::QAbstractClipAnimator::loopCount
    :realsig: () const
    :digest: 3b04b8b4535318ea19676443476343bf

Returns the number of times the animation should play.

The value is 1 by default: the animation will play through once and then stop.

If set to :sip:ref:`~PyQt6.Qt3DAnimation.QAbstractClipAnimator.Loops.Infinite`, the animation will continuously repeat until it is explicitly stopped.

.. seealso:: :sip:ref:`~PyQt6.Qt3DAnimation.QAbstractClipAnimator.setLoopCount`.
