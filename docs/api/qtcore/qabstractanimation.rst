:orphan:

.. sip:class:: PyQt6.QtCore.QAbstractAnimation
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCore/QAbstractAnimation-c.rst

    .. sip:enum:: PyQt6.QtCore.QAbstractAnimation.DeletionPolicy
        :description: QtCore/QAbstractAnimation-DeletionPolicy-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QAbstractAnimation.DeletionPolicy.DeleteWhenStopped
            :description: QtCore/QAbstractAnimation-DeletionPolicy-DeleteWhenStopped-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QAbstractAnimation.DeletionPolicy.KeepWhenStopped
            :description: QtCore/QAbstractAnimation-DeletionPolicy-KeepWhenStopped-v.rst

    .. sip:enum:: PyQt6.QtCore.QAbstractAnimation.Direction
        :description: QtCore/QAbstractAnimation-Direction-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QAbstractAnimation.Direction.Backward
            :description: QtCore/QAbstractAnimation-Direction-Backward-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QAbstractAnimation.Direction.Forward
            :description: QtCore/QAbstractAnimation-Direction-Forward-v.rst

    .. sip:enum:: PyQt6.QtCore.QAbstractAnimation.State
        :description: QtCore/QAbstractAnimation-State-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QAbstractAnimation.State.Paused
            :description: QtCore/QAbstractAnimation-State-Paused-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QAbstractAnimation.State.Running
            :description: QtCore/QAbstractAnimation-State-Running-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QAbstractAnimation.State.Stopped
            :description: QtCore/QAbstractAnimation-State-Stopped-v.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QAbstractAnimation-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.currentLoop
        :returns:
            int
        :description: QtCore/QAbstractAnimation-currentLoop-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.currentLoopTime
        :returns:
            int
        :description: QtCore/QAbstractAnimation-currentLoopTime-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.currentTime
        :returns:
            int
        :description: QtCore/QAbstractAnimation-currentTime-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.direction
        :returns:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.Direction`
        :description: QtCore/QAbstractAnimation-direction-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.duration
        :returns:
            int
        :description: QtCore/QAbstractAnimation-duration-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtCore/QAbstractAnimation-event-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.group
        :returns:
            :sip:ref:`~PyQt6.QtCore.QAnimationGroup`
        :description: QtCore/QAbstractAnimation-group-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.loopCount
        :returns:
            int
        :description: QtCore/QAbstractAnimation-loopCount-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.pause
        :description: QtCore/QAbstractAnimation-pause-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.resume
        :description: QtCore/QAbstractAnimation-resume-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.setCurrentTime
        :args:
            int
        :description: QtCore/QAbstractAnimation-setCurrentTime-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.setDirection
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.Direction`
        :description: QtCore/QAbstractAnimation-setDirection-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.setLoopCount
        :args:
            int
        :description: QtCore/QAbstractAnimation-setLoopCount-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.setPaused
        :args:
            bool
        :description: QtCore/QAbstractAnimation-setPaused-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.start
        :args:
            policy: :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.DeletionPolicy` = :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.DeletionPolicy.KeepWhenStopped`
        :description: QtCore/QAbstractAnimation-start-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.state
        :returns:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.State`
        :description: QtCore/QAbstractAnimation-state-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.stop
        :description: QtCore/QAbstractAnimation-stop-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.totalDuration
        :returns:
            int
        :description: QtCore/QAbstractAnimation-totalDuration-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.updateCurrentTime
        :args:
            int
        :description: QtCore/QAbstractAnimation-updateCurrentTime-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.updateDirection
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.Direction`
        :description: QtCore/QAbstractAnimation-updateDirection-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractAnimation.updateState
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.State`
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.State`
        :description: QtCore/QAbstractAnimation-updateState-f.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractAnimation.currentLoopChanged
        :args:
            int
        :description: QtCore/QAbstractAnimation-currentLoopChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractAnimation.directionChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.Direction`
        :description: QtCore/QAbstractAnimation-directionChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractAnimation.finished
        :description: QtCore/QAbstractAnimation-finished-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractAnimation.stateChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.State`
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.State`
        :description: QtCore/QAbstractAnimation-stateChanged-s.rst
