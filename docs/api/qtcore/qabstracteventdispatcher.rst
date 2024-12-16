:orphan:

.. sip:class:: PyQt6.QtCore.QAbstractEventDispatcher
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCore/QAbstractEventDispatcher-c.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QAbstractEventDispatcher-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.closingDown
        :description: QtCore/QAbstractEventDispatcher-closingDown-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.filterNativeEvent
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            :py:class:`~PyQt6.sip.voidptr`
        :returns:
            bool
            :py:class:`~PyQt6.sip.voidptr`
        :description: QtCore/QAbstractEventDispatcher-filterNativeEvent-f-2.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.installNativeEventFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractNativeEventFilter`
        :description: QtCore/QAbstractEventDispatcher-installNativeEventFilter-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.instance
        :args:
            thread: :sip:ref:`~PyQt6.QtCore.QThread` = None
        :returns:
            :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher`
        :static:
        :description: QtCore/QAbstractEventDispatcher-instance-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.interrupt
        :description: QtCore/QAbstractEventDispatcher-interrupt-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.processEvents
        :args:
            :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventsFlag`
        :returns:
            bool
        :description: QtCore/QAbstractEventDispatcher-processEvents-f-1.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.registeredTimers
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher.TimerInfo`]
        :description: QtCore/QAbstractEventDispatcher-registeredTimers-f-1.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.registerTimer
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.TimerType`
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            int
        :description: QtCore/QAbstractEventDispatcher-registerTimer-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.registerTimer
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtCore.Qt.TimerType`
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtCore/QAbstractEventDispatcher-registerTimer-f-1.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.remainingTime
        :args:
            int
        :returns:
            int
        :description: QtCore/QAbstractEventDispatcher-remainingTime-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.removeNativeEventFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractNativeEventFilter`
        :description: QtCore/QAbstractEventDispatcher-removeNativeEventFilter-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.startingUp
        :description: QtCore/QAbstractEventDispatcher-startingUp-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.unregisterTimer
        :args:
            int
        :returns:
            bool
        :description: QtCore/QAbstractEventDispatcher-unregisterTimer-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.unregisterTimers
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            bool
        :description: QtCore/QAbstractEventDispatcher-unregisterTimers-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractEventDispatcher.wakeUp
        :description: QtCore/QAbstractEventDispatcher-wakeUp-f.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractEventDispatcher.aboutToBlock
        :description: QtCore/QAbstractEventDispatcher-aboutToBlock-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractEventDispatcher.awake
        :description: QtCore/QAbstractEventDispatcher-awake-s.rst
