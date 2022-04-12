:orphan:

.. sip:class:: PyQt6.QtCore.QThreadPool
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCore/QThreadPool-c.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QThreadPool-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.activeThreadCount
        :returns:
            int
        :description: QtCore/QThreadPool-activeThreadCount-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.clear
        :description: QtCore/QThreadPool-clear-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.contains
        :args:
            :sip:ref:`~PyQt6.QtCore.QThread`
        :returns:
            bool
        :description: QtCore/QThreadPool-contains-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.expiryTimeout
        :returns:
            int
        :description: QtCore/QThreadPool-expiryTimeout-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.globalInstance
        :returns:
            :sip:ref:`~PyQt6.QtCore.QThreadPool`
        :static:
        :description: QtCore/QThreadPool-globalInstance-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.maxThreadCount
        :returns:
            int
        :description: QtCore/QThreadPool-maxThreadCount-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.releaseThread
        :description: QtCore/QThreadPool-releaseThread-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.reserveThread
        :description: QtCore/QThreadPool-reserveThread-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.setExpiryTimeout
        :args:
            int
        :description: QtCore/QThreadPool-setExpiryTimeout-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.setMaxThreadCount
        :args:
            int
        :description: QtCore/QThreadPool-setMaxThreadCount-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.setStackSize
        :args:
            int
        :description: QtCore/QThreadPool-setStackSize-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.setThreadPriority
        :args:
            :sip:ref:`~PyQt6.QtCore.QThread.Priority`
        :description: QtCore/QThreadPool-setThreadPriority-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.stackSize
        :returns:
            int
        :description: QtCore/QThreadPool-stackSize-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.start
        :args:
            :sip:ref:`~PyQt6.QtCore.QRunnable`
            priority: int = 0
        :description: QtCore/QThreadPool-start-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.start
        :args:
            Callable[[], None]
            priority: int = 0
        :description: QtCore/QThreadPool-start-f-1.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.startOnReservedThread
        :args:
            :sip:ref:`~PyQt6.QtCore.QRunnable`
        :description: QtCore/QThreadPool-startOnReservedThread-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.startOnReservedThread
        :args:
            Callable[[], None]
        :description: QtCore/QThreadPool-startOnReservedThread-f-1.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.threadPriority
        :returns:
            :sip:ref:`~PyQt6.QtCore.QThread.Priority`
        :description: QtCore/QThreadPool-threadPriority-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.tryStart
        :args:
            :sip:ref:`~PyQt6.QtCore.QRunnable`
        :returns:
            bool
        :description: QtCore/QThreadPool-tryStart-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.tryStart
        :args:
            Callable[[], None]
        :returns:
            bool
        :description: QtCore/QThreadPool-tryStart-f-1.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.tryTake
        :args:
            :sip:ref:`~PyQt6.QtCore.QRunnable`
        :returns:
            bool
        :description: QtCore/QThreadPool-tryTake-f.rst

    .. sip:method:: PyQt6.QtCore.QThreadPool.waitForDone
        :args:
            msecs: int = -1
        :returns:
            bool
        :description: QtCore/QThreadPool-waitForDone-f.rst
