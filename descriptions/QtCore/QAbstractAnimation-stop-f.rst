.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: b7dd05349764103b785cf781a1d22594

Stops the animation. When the animation is stopped, it emits the :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.stateChanged` signal, and :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.state` returns Stopped. The current time is not changed.

If the animation stops by itself after reaching the end (i.e., :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.currentLoopTime` == :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.duration` and :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.currentLoop` > :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.loopCount` - 1), the :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.finished` signal is emitted.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.start`, :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.state`.
