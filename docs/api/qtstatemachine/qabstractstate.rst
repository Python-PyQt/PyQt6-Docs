:orphan:

.. sip:class:: PyQt6.QtStateMachine.QAbstractState
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtStateMachine/QAbstractState-c.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractState.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtStateMachine.QState` = None
        :description: QtStateMachine/QAbstractState-__init__-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractState.active
        :returns:
            bool
        :description: QtStateMachine/QAbstractState-active-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractState.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtStateMachine/QAbstractState-event-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractState.machine
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QStateMachine`
        :description: QtStateMachine/QAbstractState-machine-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractState.onEntry
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtStateMachine/QAbstractState-onEntry-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractState.onExit
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtStateMachine/QAbstractState-onExit-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QAbstractState.parentState
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QState`
        :description: QtStateMachine/QAbstractState-parentState-f.rst

    .. sip:signal:: PyQt6.QtStateMachine.QAbstractState.activeChanged
        :args:
            bool
        :description: QtStateMachine/QAbstractState-activeChanged-s.rst

    .. sip:signal:: PyQt6.QtStateMachine.QAbstractState.entered
        :description: QtStateMachine/QAbstractState-entered-s.rst

    .. sip:signal:: PyQt6.QtStateMachine.QAbstractState.exited
        :description: QtStateMachine/QAbstractState-exited-s.rst
