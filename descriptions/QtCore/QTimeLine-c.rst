.. sip:class-description::
    :status: todo
    :brief: Timeline for controlling animations
    :digest: 0390aadf09c0d199a8f048919b9afb79

The :sip:ref:`~PyQt6.QtCore.QTimeLine` class provides a timeline for controlling animations.

It's most commonly used to animate a GUI control by calling a slot periodically. You can construct a timeline by passing its duration in milliseconds to :sip:ref:`~PyQt6.QtCore.QTimeLine`'s constructor. The timeline's duration describes for how long the animation will run. Then you set a suitable frame range by calling :sip:ref:`~PyQt6.QtCore.QTimeLine.setFrameRange`. Finally connect the :sip:ref:`~PyQt6.QtCore.QTimeLine.frameChanged` signal to a suitable slot in the widget you wish to animate (for example, :sip:ref:`~PyQt6.QtWidgets.QProgressBar.setValue` in :sip:ref:`~PyQt6.QtWidgets.QProgressBar`). When you proceed to calling :sip:ref:`~PyQt6.QtCore.QTimeLine.start`, :sip:ref:`~PyQt6.QtCore.QTimeLine` will enter Running state, and start emitting :sip:ref:`~PyQt6.QtCore.QTimeLine.frameChanged` at regular intervals, causing your widget's connected property's value to grow from the lower end to the upper and of your frame range, at a steady rate. You can specify the update interval by calling :sip:ref:`~PyQt6.QtCore.QTimeLine.setUpdateInterval`. When done, :sip:ref:`~PyQt6.QtCore.QTimeLine` enters :sip:ref:`~PyQt6.QtCore.QTimeLine.State.NotRunning` state, and emits :sip:ref:`~PyQt6.QtCore.QTimeLine.finished`.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qtimeline.py
    :lines: 54-66

By default the timeline runs once, from its beginning to its end, upon which you must call :sip:ref:`~PyQt6.QtCore.QTimeLine.start` again to restart from the beginning. To make the timeline loop, you can call :sip:ref:`~PyQt6.QtCore.QTimeLine.setLoopCount`, passing the number of times the timeline should run before finishing. The direction can also be changed, causing the timeline to run backward, by calling :sip:ref:`~PyQt6.QtCore.QTimeLine.setDirection`. You can also pause and unpause the timeline while it's running by calling :sip:ref:`~PyQt6.QtCore.QTimeLine.setPaused`. For interactive control, the :sip:ref:`~PyQt6.QtCore.QTimeLine.setCurrentTime` function is provided, which sets the time position of the time line directly. Although most useful in :sip:ref:`~PyQt6.QtCore.QTimeLine.State.NotRunning` state (e.g., connected to a :sip:ref:`~PyQt6.QtCore.QTimeLine.valueChanged` signal in a :sip:ref:`~PyQt6.QtWidgets.QSlider`), this function can be called at any time.

The frame interface is useful for standard widgets, but :sip:ref:`~PyQt6.QtCore.QTimeLine` can be used to control any type of animation. The heart of :sip:ref:`~PyQt6.QtCore.QTimeLine` lies in the :sip:ref:`~PyQt6.QtCore.QTimeLine.valueForTime` function, which generates a *value* between 0 and 1 for a given time. This value is typically used to describe the steps of an animation, where 0 is the first step of an animation, and 1 is the last step. When running, :sip:ref:`~PyQt6.QtCore.QTimeLine` generates values between 0 and 1 by calling :sip:ref:`~PyQt6.QtCore.QTimeLine.valueForTime` and emitting :sip:ref:`~PyQt6.QtCore.QTimeLine.valueChanged`. By default, :sip:ref:`~PyQt6.QtCore.QTimeLine.valueForTime` applies an interpolation algorithm to generate these value. You can choose from a set of predefined timeline algorithms by calling :sip:ref:`~PyQt6.QtCore.QTimeLine.setEasingCurve`.

Note that, by default, :sip:ref:`~PyQt6.QtCore.QTimeLine` uses :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type.InOutSine`, which provides a value that grows slowly, then grows steadily, and finally grows slowly. For a custom timeline, you can reimplement :sip:ref:`~PyQt6.QtCore.QTimeLine.valueForTime`, in which case :sip:ref:`~PyQt6.QtCore.QTimeLine`'s :sip:ref:`~PyQt6.QtCore.QTimeLine.easingCurve` property is ignored.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QProgressBar`, :sip:ref:`~PyQt6.QtWidgets.QProgressDialog`.
