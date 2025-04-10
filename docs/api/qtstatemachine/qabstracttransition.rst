:orphan:

.. sip:class:: PyQt6.QtStateMachine.QAbstractTransition
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtStateMachine/QAbstractTransition-c.rst

    .. sip:enum:: PyQt6.QtStateMachine.QAbstractTransition.TransitionType
        :description: QtStateMachine/QAbstractTransition-TransitionType-e.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QAbstractTransition.TransitionType.ExternalTransition
            :description: QtStateMachine/QAbstractTransition-TransitionType-ExternalTransition-v.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QAbstractTransition.TransitionType.InternalTransition
            :description: QtStateMachine/QAbstractTransition-TransitionType-InternalTransition-v.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.__init__
        :args:
            sourceState: :sip:ref:`~PyQt6.QtStateMachine.QState` = None
        :description: QtStateMachine/QAbstractTransition-__init__-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.addAnimation
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation`
        :description: QtStateMachine/QAbstractTransition-addAnimation-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.animations
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QAbstractAnimation`]
        :description: QtStateMachine/QAbstractTransition-animations-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtStateMachine/QAbstractTransition-event-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.eventTest
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtStateMachine/QAbstractTransition-eventTest-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.machine
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QStateMachine`
        :description: QtStateMachine/QAbstractTransition-machine-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.onTransition
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtStateMachine/QAbstractTransition-onTransition-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.removeAnimation
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation`
        :description: QtStateMachine/QAbstractTransition-removeAnimation-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.setTargetState
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractState`
        :description: QtStateMachine/QAbstractTransition-setTargetState-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.setTargetStates
        :args:
            Iterable[:sip:ref:`~PyQt6.QtStateMachine.QAbstractState`]
        :description: QtStateMachine/QAbstractTransition-setTargetStates-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.setTransitionType
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractTransition.TransitionType`
        :description: QtStateMachine/QAbstractTransition-setTransitionType-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.sourceState
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QState`
        :description: QtStateMachine/QAbstractTransition-sourceState-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.targetState
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractState`
        :description: QtStateMachine/QAbstractTransition-targetState-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.targetStates
        :returns:
            list[:sip:ref:`~PyQt6.QtStateMachine.QAbstractState`]
        :description: QtStateMachine/QAbstractTransition-targetStates-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractTransition.transitionType
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractTransition.TransitionType`
        :description: QtStateMachine/QAbstractTransition-transitionType-f.rst

    .. sip:signal:: PyQt6.QtStateMachine.QAbstractTransition.targetStateChanged
        :description: QtStateMachine/QAbstractTransition-targetStateChanged-s.rst

    .. sip:signal:: PyQt6.QtStateMachine.QAbstractTransition.targetStatesChanged
        :description: QtStateMachine/QAbstractTransition-targetStatesChanged-s.rst

    .. sip:signal:: PyQt6.QtStateMachine.QAbstractTransition.triggered
        :description: QtStateMachine/QAbstractTransition-triggered-s.rst
