.. sip:class-description::
    :status: todo
    :brief: Pause for QSequentialAnimationGroup
    :digest: 905f9de2231b7a466e719a6eb8a8fcba

The :sip:ref:`~PyQt6.QtCore.QPauseAnimation` class provides a pause for :sip:ref:`~PyQt6.QtCore.QSequentialAnimationGroup`.

If you wish to introduce a delay between animations in a :sip:ref:`~PyQt6.QtCore.QSequentialAnimationGroup`, you can insert a :sip:ref:`~PyQt6.QtCore.QPauseAnimation`. This class does not animate anything, but does not :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.finished` before a specified number of milliseconds have elapsed from when it was started. You specify the duration of the pause in the constructor. It can also be set directly with :sip:ref:`~PyQt6.QtCore.QPauseAnimation.setDuration`.

It is not necessary to construct a :sip:ref:`~PyQt6.QtCore.QPauseAnimation` yourself. :sip:ref:`~PyQt6.QtCore.QSequentialAnimationGroup` provides the convenience functions :sip:ref:`~PyQt6.QtCore.QSequentialAnimationGroup.addPause` and :sip:ref:`~PyQt6.QtCore.QSequentialAnimationGroup.insertPause`. These functions simply take the number of milliseconds the pause should last.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSequentialAnimationGroup`.
