:orphan:

.. sip:class:: PyQt6.QtStateMachine.QHistoryState
    :inherits: :sip:ref:`~PyQt6.QtStateMachine.QAbstractState`
    :description: QtStateMachine/QHistoryState-c.rst

    .. sip:enum:: PyQt6.QtStateMachine.QHistoryState.HistoryType
        :description: QtStateMachine/QHistoryState-HistoryType-e.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QHistoryState.HistoryType.DeepHistory
            :description: QtStateMachine/QHistoryState-HistoryType-DeepHistory-v.rst

        .. sip:enum-member:: PyQt6.QtStateMachine.QHistoryState.HistoryType.ShallowHistory
            :description: QtStateMachine/QHistoryState-HistoryType-ShallowHistory-v.rst

    .. sip:method:: PyQt6.QtStateMachine.QHistoryState.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtStateMachine.QState` = None
        :description: QtStateMachine/QHistoryState-__init__-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QHistoryState.__init__
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QHistoryState.HistoryType`
            parent: :sip:ref:`~PyQt6.QtStateMachine.QState` = None
        :description: QtStateMachine/QHistoryState-__init__-f-1.rst

    .. sip:method:: PyQt6.QtStateMachine.QHistoryState.defaultState
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractState`
        :description: QtStateMachine/QHistoryState-defaultState-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QHistoryState.defaultTransition
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractTransition`
        :description: QtStateMachine/QHistoryState-defaultTransition-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QHistoryState.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtStateMachine/QHistoryState-event-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QHistoryState.historyType
        :returns:
            :sip:ref:`~PyQt6.QtStateMachine.QHistoryState.HistoryType`
        :description: QtStateMachine/QHistoryState-historyType-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QHistoryState.onEntry
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtStateMachine/QHistoryState-onEntry-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QHistoryState.onExit
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtStateMachine/QHistoryState-onExit-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QHistoryState.setDefaultState
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractState`
        :description: QtStateMachine/QHistoryState-setDefaultState-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QHistoryState.setDefaultTransition
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QAbstractTransition`
        :description: QtStateMachine/QHistoryState-setDefaultTransition-f.rst

    .. sip:method:: PyQt6.QtStateMachine.QHistoryState.setHistoryType
        :args:
            :sip:ref:`~PyQt6.QtStateMachine.QHistoryState.HistoryType`
        :description: QtStateMachine/QHistoryState-setHistoryType-f.rst

    .. sip:signal:: PyQt6.QtStateMachine.QHistoryState.defaultStateChanged
        :description: QtStateMachine/QHistoryState-defaultStateChanged-s.rst

    .. sip:signal:: PyQt6.QtStateMachine.QHistoryState.defaultTransitionChanged
        :description: QtStateMachine/QHistoryState-defaultTransitionChanged-s.rst

    .. sip:signal:: PyQt6.QtStateMachine.QHistoryState.historyTypeChanged
        :description: QtStateMachine/QHistoryState-historyTypeChanged-s.rst
