.. sip:method-description::
    :status: todo
    :pysig: 055e1ee1c7356e7227d22fbf5ce0fbc2
    :realsig: (QAbstractAnimation::DeletionPolicy)
    :digest: 8f108c7986848cc0f7f1724ff67413f4

Starts the animation. The *policy* argument says whether or not the animation should be deleted when it's done. When the animation starts, the :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.stateChanged` signal is emitted, and :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.state` returns Running. When control reaches the event loop, the animation will run by itself, periodically calling :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.updateCurrentTime` as the animation progresses.

If the animation is currently stopped or has already reached the end, calling  will rewind the animation and start again from the beginning. When the animation reaches the end, the animation will either stop, or if the loop level is more than 1, it will rewind and continue from the beginning.

If the animation is already running, this function does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.stop`, :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.state`.
