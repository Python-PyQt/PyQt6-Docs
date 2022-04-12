:orphan:

.. sip:class:: PyQt6.QtCore.QEventLoop
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCore/QEventLoop-c.rst

    .. sip:enum:: PyQt6.QtCore.QEventLoop.ProcessEventsFlag
        :description: QtCore/QEventLoop-ProcessEventsFlag-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QEventLoop.ProcessEventsFlag.AllEvents
            :description: QtCore/QEventLoop-ProcessEventsFlag-AllEvents-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QEventLoop.ProcessEventsFlag.ExcludeSocketNotifiers
            :description: QtCore/QEventLoop-ProcessEventsFlag-ExcludeSocketNotifiers-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QEventLoop.ProcessEventsFlag.ExcludeUserInputEvents
            :description: QtCore/QEventLoop-ProcessEventsFlag-ExcludeUserInputEvents-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QEventLoop.ProcessEventsFlag.WaitForMoreEvents
            :description: QtCore/QEventLoop-ProcessEventsFlag-WaitForMoreEvents-v.rst

    .. sip:method:: PyQt6.QtCore.QEventLoop.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QEventLoop-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QEventLoop.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtCore/QEventLoop-event-f.rst

    .. sip:method:: PyQt6.QtCore.QEventLoop.exec
        :args:
            flags: :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventsFlag` = :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventsFlag.AllEvents`
        :returns:
            int
        :description: QtCore/QEventLoop-exec-f-1.rst

    .. sip:method:: PyQt6.QtCore.QEventLoop.exit
        :args:
            returnCode: int = 0
        :description: QtCore/QEventLoop-exit-f.rst

    .. sip:method:: PyQt6.QtCore.QEventLoop.isRunning
        :returns:
            bool
        :description: QtCore/QEventLoop-isRunning-f.rst

    .. sip:method:: PyQt6.QtCore.QEventLoop.processEvents
        :args:
            flags: :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventsFlag` = :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventsFlag.AllEvents`
        :returns:
            bool
        :description: QtCore/QEventLoop-processEvents-f-2.rst

    .. sip:method:: PyQt6.QtCore.QEventLoop.processEvents
        :args:
            :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventsFlag`
            int
        :description: QtCore/QEventLoop-processEvents-f-3.rst

    .. sip:method:: PyQt6.QtCore.QEventLoop.quit
        :description: QtCore/QEventLoop-quit-f.rst

    .. sip:method:: PyQt6.QtCore.QEventLoop.wakeUp
        :description: QtCore/QEventLoop-wakeUp-f.rst
