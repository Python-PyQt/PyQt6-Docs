:orphan:

.. sip:class:: PyQt6.QtStateMachine.QStateMachine
    :inherits: :sip:ref:`~PyQt6.QtStateMachine.QState`
    :description: QtStateMachine/QStateMachine-c.rst

    .. sip:enum:: PyQt6.QtStateMachine.QStateMachine.Error
        :description: QtStateMachine/QStateMachine-Error-e.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QStateMachine.Error.NoCommonAncestorForTransitionError
            :description: QtStateMachine/QStateMachine-Error-NoCommonAncestorForTransitionError-v.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QStateMachine.Error.NoDefaultStateInHistoryStateError
            :description: QtStateMachine/QStateMachine-Error-NoDefaultStateInHistoryStateError-v.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QStateMachine.Error.NoError
            :description: QtStateMachine/QStateMachine-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QStateMachine.Error.NoInitialStateError
            :description: QtStateMachine/QStateMachine-Error-NoInitialStateError-v.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QStateMachine.Error.StateMachineChildModeSetToParallelError
            :description: QtStateMachine/QStateMachine-Error-StateMachineChildModeSetToParallelError-v.rst

    .. sip:enum:: PyQt6.QtStateMachine.QStateMachine.EventPriority
        :description: QtStateMachine/QStateMachine-EventPriority-e.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QStateMachine.EventPriority.HighPriority
            :description: QtStateMachine/QStateMachine-EventPriority-HighPriority-v.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QStateMachine.EventPriority.NormalPriority
            :description: QtStateMachine/QStateMachine-EventPriority-NormalPriority-v.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtStateMachine/QStateMachine-__init__-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.__init__
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QState.ChildMode`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtStateMachine/QStateMachine-__init__-f-1.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.addDefaultAnimation
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation`
        :description: QtStateMachine/QStateMachine-addDefaultAnimation-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.addState
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractState`
        :description: QtStateMachine/QStateMachine-addState-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.cancelDelayedEvent
        :args:
            int
        :returns:
            bool
        :description: QtStateMachine/QStateMachine-cancelDelayedEvent-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.clearError
        :description: QtStateMachine/QStateMachine-clearError-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.configuration
        :returns:
            set[:sip:ref:`~PyQt6.QtStateMachine.QAbstractState`]
        :description: QtStateMachine/QStateMachine-configuration-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.defaultAnimations
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QAbstractAnimation`]
        :description: QtStateMachine/QStateMachine-defaultAnimations-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.error
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QStateMachine.Error`
        :description: QtStateMachine/QStateMachine-error-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.errorString
        :returns:
            str
        :description: QtStateMachine/QStateMachine-errorString-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtStateMachine/QStateMachine-event-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.eventFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtStateMachine/QStateMachine-eventFilter-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.globalRestorePolicy
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QState.RestorePolicy`
        :description: QtStateMachine/QStateMachine-globalRestorePolicy-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.isAnimated
        :returns:
            bool
        :description: QtStateMachine/QStateMachine-isAnimated-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.isRunning
        :returns:
            bool
        :description: QtStateMachine/QStateMachine-isRunning-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.onEntry
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtStateMachine/QStateMachine-onEntry-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.onExit
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtStateMachine/QStateMachine-onExit-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.postDelayedEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
            int
        :returns:
            int
        :description: QtStateMachine/QStateMachine-postDelayedEvent-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.postEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
            priority: :sip:ref:`~PyQt6.QtStateMachine.QStateMachine.EventPriority` = :sip:ref:`~PyQt6.QtStateMachine.QStateMachine.EventPriority.NormalPriority`
        :description: QtStateMachine/QStateMachine-postEvent-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.removeDefaultAnimation
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation`
        :description: QtStateMachine/QStateMachine-removeDefaultAnimation-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.removeState
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractState`
        :description: QtStateMachine/QStateMachine-removeState-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.setAnimated
        :args:
            bool
        :description: QtStateMachine/QStateMachine-setAnimated-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.setGlobalRestorePolicy
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QState.RestorePolicy`
        :description: QtStateMachine/QStateMachine-setGlobalRestorePolicy-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.setRunning
        :args:
            bool
        :description: QtStateMachine/QStateMachine-setRunning-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.start
        :description: QtStateMachine/QStateMachine-start-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QStateMachine.stop
        :description: QtStateMachine/QStateMachine-stop-f.rst

    .. sip:signal:: PyQt6.QtStateMachine.QStateMachine.runningChanged
        :args:
            bool
        :description: QtStateMachine/QStateMachine-runningChanged-s.rst

    .. sip:signal:: PyQt6.QtStateMachine.QStateMachine.started
        :description: QtStateMachine/QStateMachine-started-s.rst

    .. sip:signal:: PyQt6.QtStateMachine.QStateMachine.stopped
        :description: QtStateMachine/QStateMachine-stopped-s.rst
