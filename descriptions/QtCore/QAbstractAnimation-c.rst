.. sip:class-description::
    :status: todo
    :brief: The base of all animations
    :digest: f5abc2ea5af3a19488dad1abdd726d4b

The :sip:ref:`~PyQt6.QtCore.QAbstractAnimation` class is the base of all animations.

The class defines the functions for the functionality shared by all animations. By inheriting this class, you can create custom animations that plug into the rest of the animation framework.

The progress of an animation is given by its current time (\ :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.currentLoopTime`), which is measured in milliseconds from the start of the animation (0) to its end (\ :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.duration`). The value is updated automatically while the animation is running. It can also be set directly with :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.setCurrentTime`.

At any point an animation is in one of three states: :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.State.Running`, :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.State.Stopped`, or :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.State.Paused`--as defined by the :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.State` enum. The current state can be changed by calling :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.start`, :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.stop`, :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.pause`, or :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.resume`. An animation will always reset its :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.currentTime` when it is started. If paused, it will continue with the same current time when resumed. When an animation is stopped, it cannot be resumed, but will keep its current time (until started again). :sip:ref:`~PyQt6.QtCore.QAbstractAnimation` will emit :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.stateChanged` whenever its state changes.

An animation can loop any number of times by setting the :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.loopCount` property. When an animation's current time reaches its :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.duration`, it will reset the current time and keep running. A loop count of 1 (the default value) means that the animation will run one time. Note that a duration of -1 means that the animation will run until stopped; the current time will increase indefinitely. When the current time equals :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.duration` and the animation is in its final loop, the :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.State.Stopped` state is entered, and the :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.finished` signal is emitted.

:sip:ref:`~PyQt6.QtCore.QAbstractAnimation` provides pure virtual functions used by subclasses to track the progress of the animation: :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.duration` and :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.updateCurrentTime`. The :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.duration` function lets you report a duration for the animation (as discussed above). The animation framework calls :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.updateCurrentTime` when current time has changed. By reimplementing this function, you can track the animation progress. Note that neither the interval between calls nor the number of calls to this function are defined; though, it will normally be 60 updates per second.

By reimplementing :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.updateState`, you can track the animation's state changes, which is particularly useful for animations that are not driven by time.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QVariantAnimation`, :sip:ref:`~PyQt6.QtCore.QPropertyAnimation`, :sip:ref:`~PyQt6.QtCore.QAnimationGroup`, `The Animation Framework <https://doc.qt.io/qt-6/animation-overview.html>`_.
