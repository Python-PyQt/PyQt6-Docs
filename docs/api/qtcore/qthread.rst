:orphan:

.. sip:class:: PyQt6.QtCore.QThread
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCore/QThread-c.rst

    .. sip:enum:: PyQt6.QtCore.QThread.Priority
        :description: QtCore/QThread-Priority-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QThread.Priority.HighestPriority
            :description: QtCore/QThread-Priority-HighestPriority-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QThread.Priority.HighPriority
            :description: QtCore/QThread-Priority-HighPriority-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QThread.Priority.IdlePriority
            :description: QtCore/QThread-Priority-IdlePriority-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QThread.Priority.InheritPriority
            :description: QtCore/QThread-Priority-InheritPriority-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QThread.Priority.LowestPriority
            :description: QtCore/QThread-Priority-LowestPriority-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QThread.Priority.LowPriority
            :description: QtCore/QThread-Priority-LowPriority-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QThread.Priority.NormalPriority
            :description: QtCore/QThread-Priority-NormalPriority-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QThread.Priority.TimeCriticalPriority
            :description: QtCore/QThread-Priority-TimeCriticalPriority-v.rst

    .. sip:method:: PyQt6.QtCore.QThread.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QThread-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.currentThread
        :returns:
            :sip:ref:`~PyQt6.QtCore.QThread`
        :static:
        :description: QtCore/QThread-currentThread-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.currentThreadId
        :returns:
            :py:class:`~PyQt6.sip.voidptr`
        :static:
        :description: QtCore/QThread-currentThreadId-f-1.rst

    .. sip:method:: PyQt6.QtCore.QThread.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtCore/QThread-event-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.eventDispatcher
        :returns:
            :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher`
        :description: QtCore/QThread-eventDispatcher-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.exec
        :returns:
            int
        :description: QtCore/QThread-exec-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.exit
        :args:
            returnCode: int = 0
        :description: QtCore/QThread-exit-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.idealThreadCount
        :returns:
            int
        :static:
        :description: QtCore/QThread-idealThreadCount-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.isCurrentThread
        :returns:
            bool
        :description: QtCore/QThread-isCurrentThread-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.isFinished
        :returns:
            bool
        :description: QtCore/QThread-isFinished-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.isInterruptionRequested
        :returns:
            bool
        :description: QtCore/QThread-isInterruptionRequested-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.isMainThread
        :returns:
            bool
        :static:
        :description: QtCore/QThread-isMainThread-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.isRunning
        :returns:
            bool
        :description: QtCore/QThread-isRunning-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.loopLevel
        :returns:
            int
        :description: QtCore/QThread-loopLevel-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.msleep
        :args:
            int
        :static:
        :description: QtCore/QThread-msleep-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.priority
        :returns:
            :sip:ref:`~PyQt6.QtCore.QThread.Priority`
        :description: QtCore/QThread-priority-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.quit
        :description: QtCore/QThread-quit-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.requestInterruption
        :description: QtCore/QThread-requestInterruption-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.run
        :description: QtCore/QThread-run-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.setEventDispatcher
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher`
        :description: QtCore/QThread-setEventDispatcher-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.setPriority
        :args:
            :sip:ref:`~PyQt6.QtCore.QThread.Priority`
        :description: QtCore/QThread-setPriority-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.setStackSize
        :args:
            int
        :description: QtCore/QThread-setStackSize-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.setTerminationEnabled
        :args:
            enabled: bool = True
        :static:
        :description: QtCore/QThread-setTerminationEnabled-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.sleep
        :args:
            int
        :static:
        :description: QtCore/QThread-sleep-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.stackSize
        :returns:
            int
        :description: QtCore/QThread-stackSize-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.start
        :args:
            priority: :sip:ref:`~PyQt6.QtCore.QThread.Priority` = :sip:ref:`~PyQt6.QtCore.QThread.Priority.InheritPriority`
        :description: QtCore/QThread-start-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.terminate
        :description: QtCore/QThread-terminate-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.usleep
        :args:
            int
        :static:
        :description: QtCore/QThread-usleep-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.wait
        :args:
            deadline: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` = QDeadlineTimer(QDeadlineTimer.Forever)
        :returns:
            bool
        :description: QtCore/QThread-wait-f.rst

    .. sip:method:: PyQt6.QtCore.QThread.wait
        :args:
            int
        :returns:
            bool
        :description: QtCore/QThread-wait-f-1.rst

    .. sip:method:: PyQt6.QtCore.QThread.yieldCurrentThread
        :static:
        :description: QtCore/QThread-yieldCurrentThread-f.rst

    .. sip:signal:: PyQt6.QtCore.QThread.finished
        :description: QtCore/QThread-finished-s.rst

    .. sip:signal:: PyQt6.QtCore.QThread.started
        :description: QtCore/QThread-started-s.rst
