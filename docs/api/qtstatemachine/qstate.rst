:orphan:

.. sip:class:: PyQt6.QtStateMachine.QState
    :inherits: :sip:ref:`~PyQt6.QtStateMachine.QAbstractState`
    :description: QtStateMachine/QState-c.rst

    .. sip:enum:: PyQt6.QtStateMachine.QState.ChildMode
        :description: QtStateMachine/QState-ChildMode-e.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QState.ChildMode.ExclusiveStates
            :description: QtStateMachine/QState-ChildMode-ExclusiveStates-v.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QState.ChildMode.ParallelStates
            :description: QtStateMachine/QState-ChildMode-ParallelStates-v.rst

    .. sip:enum:: PyQt6.QtStateMachine.QState.RestorePolicy
        :description: QtStateMachine/QState-RestorePolicy-e.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QState.RestorePolicy.DontRestoreProperties
            :description: QtStateMachine/QState-RestorePolicy-DontRestoreProperties-v.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QState.RestorePolicy.RestoreProperties
            :description: QtStateMachine/QState-RestorePolicy-RestoreProperties-v.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtStateMachine.QState` = None
        :description: QtStateMachine/QState-__init__-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.__init__
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QState.ChildMode`
            parent: :sip:ref:`~PyQt6.QtStateMachine.QState` = None
        :description: QtStateMachine/QState-__init__-f-1.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.addTransition
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractTransition`
        :description: QtStateMachine/QState-addTransition-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.addTransition
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractState`
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractTransition`
        :description: QtStateMachine/QState-addTransition-f-1.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.addTransition
        :args:
            pyqtBoundSignal
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractState`
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QSignalTransition`
        :description: QtStateMachine/QState-addTransition-f-2.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.assignProperty
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            str
            Any
        :description: QtStateMachine/QState-assignProperty-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.childMode
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QState.ChildMode`
        :description: QtStateMachine/QState-childMode-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.errorState
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractState`
        :description: QtStateMachine/QState-errorState-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtStateMachine/QState-event-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.initialState
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractState`
        :description: QtStateMachine/QState-initialState-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.onEntry
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtStateMachine/QState-onEntry-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.onExit
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtStateMachine/QState-onExit-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.removeTransition
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractTransition`
        :description: QtStateMachine/QState-removeTransition-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.setChildMode
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QState.ChildMode`
        :description: QtStateMachine/QState-setChildMode-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.setErrorState
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractState`
        :description: QtStateMachine/QState-setErrorState-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.setInitialState
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractState`
        :description: QtStateMachine/QState-setInitialState-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QState.transitions
        :returns:
            list[:sip:ref:`~PyQt6.QtStateMachine.QAbstractTransition`]
        :description: QtStateMachine/QState-transitions-f.rst

    .. sip:signal:: PyQt6.QtStateMachine.QState.childModeChanged
        :description: QtStateMachine/QState-childModeChanged-s.rst

    .. sip:signal:: PyQt6.QtStateMachine.QState.errorStateChanged
        :description: QtStateMachine/QState-errorStateChanged-s.rst

    .. sip:signal:: PyQt6.QtStateMachine.QState.finished
        :description: QtStateMachine/QState-finished-s.rst

    .. sip:signal:: PyQt6.QtStateMachine.QState.initialStateChanged
        :description: QtStateMachine/QState-initialStateChanged-s.rst

    .. sip:signal:: PyQt6.QtStateMachine.QState.propertiesAssigned
        :description: QtStateMachine/QState-propertiesAssigned-s.rst
