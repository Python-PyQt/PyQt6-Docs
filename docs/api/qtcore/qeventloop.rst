:orphan:

.. sip:class:: PyQt6.QtCore.QEventLoop
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCore/QEventLoop-c.rst

    .. sip:enum:: PyQt6.QtCore.QEventLoop.ProcessEventFlags
        :description: QtCore/QEventLoop-ProcessEventFlags-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QEventLoop.ProcessEventFlags.AllEvents
            :description: QtCore/QEventLoop-ProcessEventFlags-AllEvents-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QEventLoop.ProcessEventFlags.ExcludeSocketNotifiers
            :description: QtCore/QEventLoop-ProcessEventFlags-ExcludeSocketNotifiers-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QEventLoop.ProcessEventFlags.ExcludeUserInputEvents
            :description: QtCore/QEventLoop-ProcessEventFlags-ExcludeUserInputEvents-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QEventLoop.ProcessEventFlags.WaitForMoreEvents
            :description: QtCore/QEventLoop-ProcessEventFlags-WaitForMoreEvents-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QEventLoop.ProcessEventFlags.X11ExcludeTimers
            :description: QtCore/QEventLoop-ProcessEventFlags-X11ExcludeTimers-v.rst

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
            flags: :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventFlags` = :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventFlags.AllEvents`
        :returns:
            int
        :description: QtCore/QEventLoop-exec-f.rst

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
            flags: :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventFlags` = :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventFlags.AllEvents`
        :returns:
            bool
        :description: QtCore/QEventLoop-processEvents-f.rst

    .. sip:method:: PyQt6.QtCore.QEventLoop.processEvents
        :args:
            :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventFlags`
            int
        :description: QtCore/QEventLoop-processEvents-f-1.rst

    .. sip:method:: PyQt6.QtCore.QEventLoop.quit
        :description: QtCore/QEventLoop-quit-f.rst

    .. sip:method:: PyQt6.QtCore.QEventLoop.wakeUp
        :description: QtCore/QEventLoop-wakeUp-f.rst
