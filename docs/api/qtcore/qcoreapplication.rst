:orphan:

.. sip:class:: PyQt6.QtCore.QCoreApplication
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCore/QCoreApplication-c.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.__init__
        :args:
            list[str]
        :description: QtCore/QCoreApplication-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.addLibraryPath
        :args:
            Optional[str]
        :static:
        :description: QtCore/QCoreApplication-addLibraryPath-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.applicationDirPath
        :returns:
            str
        :static:
        :description: QtCore/QCoreApplication-applicationDirPath-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.applicationFilePath
        :returns:
            str
        :static:
        :description: QtCore/QCoreApplication-applicationFilePath-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.applicationName
        :returns:
            str
        :static:
        :description: QtCore/QCoreApplication-applicationName-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.applicationPid
        :returns:
            int
        :static:
        :description: QtCore/QCoreApplication-applicationPid-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.applicationVersion
        :returns:
            str
        :static:
        :description: QtCore/QCoreApplication-applicationVersion-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.arguments
        :returns:
            list[str]
        :static:
        :description: QtCore/QCoreApplication-arguments-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.checkPermission
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QBluetoothPermission`, :sip:ref:`~PyQt6.QtCore.QCalendarPermission`, :sip:ref:`~PyQt6.QtCore.QCameraPermission`, :sip:ref:`~PyQt6.QtCore.QContactsPermission`, :sip:ref:`~PyQt6.QtCore.QLocationPermission`, :sip:ref:`~PyQt6.QtCore.QMicrophonePermission`]
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.PermissionStatus`
        :description: QtCore/QCoreApplication-checkPermission-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.closingDown
        :returns:
            bool
        :static:
        :description: QtCore/QCoreApplication-closingDown-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.__enter__
        :returns:
            Any
        :description: QtCore/QCoreApplication-__enter__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtCore/QCoreApplication-event-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.eventDispatcher
        :returns:
            :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher`
        :static:
        :description: QtCore/QCoreApplication-eventDispatcher-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.exec
        :returns:
            int
        :static:
        :description: QtCore/QCoreApplication-exec-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.__exit__
        :args:
            Any
            Any
            Any
        :description: QtCore/QCoreApplication-__exit__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.exit
        :args:
            returnCode: int = 0
        :static:
        :description: QtCore/QCoreApplication-exit-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.installNativeEventFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractNativeEventFilter`
        :description: QtCore/QCoreApplication-installNativeEventFilter-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.installTranslator
        :args:
            :sip:ref:`~PyQt6.QtCore.QTranslator`
        :returns:
            bool
        :static:
        :description: QtCore/QCoreApplication-installTranslator-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.instance
        :returns:
            :sip:ref:`~PyQt6.QtCore.QCoreApplication`
        :static:
        :description: QtCore/QCoreApplication-instance-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.isQuitLockEnabled
        :returns:
            bool
        :static:
        :description: QtCore/QCoreApplication-isQuitLockEnabled-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.isSetuidAllowed
        :returns:
            bool
        :static:
        :description: QtCore/QCoreApplication-isSetuidAllowed-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.libraryPaths
        :returns:
            list[str]
        :static:
        :description: QtCore/QCoreApplication-libraryPaths-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.notify
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtCore/QCoreApplication-notify-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.organizationDomain
        :returns:
            str
        :static:
        :description: QtCore/QCoreApplication-organizationDomain-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.organizationName
        :returns:
            str
        :static:
        :description: QtCore/QCoreApplication-organizationName-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.postEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
            priority: int = :sip:ref:`~PyQt6.QtCore.Qt.EventPriority.NormalEventPriority`
        :static:
        :description: QtCore/QCoreApplication-postEvent-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.processEvents
        :args:
            flags: :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventsFlag` = :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventsFlag.AllEvents`
        :static:
        :description: QtCore/QCoreApplication-processEvents-f-2.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.processEvents
        :args:
            :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventsFlag`
            int
        :static:
        :description: QtCore/QCoreApplication-processEvents-f-3.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.processEvents
        :args:
            :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventsFlag`
            :sip:ref:`~PyQt6.QtCore.QDeadlineTimer`
        :static:
        :description: QtCore/QCoreApplication-processEvents-f-4.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.quit
        :static:
        :description: QtCore/QCoreApplication-quit-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.removeLibraryPath
        :args:
            Optional[str]
        :static:
        :description: QtCore/QCoreApplication-removeLibraryPath-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.removeNativeEventFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractNativeEventFilter`
        :description: QtCore/QCoreApplication-removeNativeEventFilter-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.removePostedEvents
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            eventType: int = 0
        :static:
        :description: QtCore/QCoreApplication-removePostedEvents-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.removeTranslator
        :args:
            :sip:ref:`~PyQt6.QtCore.QTranslator`
        :returns:
            bool
        :static:
        :description: QtCore/QCoreApplication-removeTranslator-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.requestPermission
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QBluetoothPermission`, :sip:ref:`~PyQt6.QtCore.QCalendarPermission`, :sip:ref:`~PyQt6.QtCore.QCameraPermission`, :sip:ref:`~PyQt6.QtCore.QContactsPermission`, :sip:ref:`~PyQt6.QtCore.QLocationPermission`, :sip:ref:`~PyQt6.QtCore.QMicrophonePermission`]
            Callable[[Union[:sip:ref:`~PyQt6.QtCore.QBluetoothPermission`, :sip:ref:`~PyQt6.QtCore.QCalendarPermission`, :sip:ref:`~PyQt6.QtCore.QCameraPermission`, :sip:ref:`~PyQt6.QtCore.QContactsPermission`, :sip:ref:`~PyQt6.QtCore.QLocationPermission`, :sip:ref:`~PyQt6.QtCore.QMicrophonePermission`]], None]
        :description: QtCore/QCoreApplication-requestPermission-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.sendEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :static:
        :description: QtCore/QCoreApplication-sendEvent-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.sendPostedEvents
        :args:
            receiver: :sip:ref:`~PyQt6.QtCore.QObject` = None
            eventType: int = 0
        :static:
        :description: QtCore/QCoreApplication-sendPostedEvents-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.setApplicationName
        :args:
            Optional[str]
        :static:
        :description: QtCore/QCoreApplication-setApplicationName-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.setApplicationVersion
        :args:
            Optional[str]
        :static:
        :description: QtCore/QCoreApplication-setApplicationVersion-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.setAttribute
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute`
            on: bool = True
        :static:
        :description: QtCore/QCoreApplication-setAttribute-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.setEventDispatcher
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher`
        :static:
        :description: QtCore/QCoreApplication-setEventDispatcher-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.setLibraryPaths
        :args:
            Iterable[Optional[str]]
        :static:
        :description: QtCore/QCoreApplication-setLibraryPaths-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.setOrganizationDomain
        :args:
            Optional[str]
        :static:
        :description: QtCore/QCoreApplication-setOrganizationDomain-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.setOrganizationName
        :args:
            Optional[str]
        :static:
        :description: QtCore/QCoreApplication-setOrganizationName-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.setQuitLockEnabled
        :args:
            bool
        :static:
        :description: QtCore/QCoreApplication-setQuitLockEnabled-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.setSetuidAllowed
        :args:
            bool
        :static:
        :description: QtCore/QCoreApplication-setSetuidAllowed-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.startingUp
        :returns:
            bool
        :static:
        :description: QtCore/QCoreApplication-startingUp-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.testAttribute
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute`
        :returns:
            bool
        :static:
        :description: QtCore/QCoreApplication-testAttribute-f.rst

    .. sip:method:: PyQt6.QtCore.QCoreApplication.translate
        :args:
            str
            str
            disambiguation: str = None
            n: int = -1
        :returns:
            str
        :static:
        :description: QtCore/QCoreApplication-translate-f.rst

    .. sip:signal:: PyQt6.QtCore.QCoreApplication.aboutToQuit
        :description: QtCore/QCoreApplication-aboutToQuit-s.rst
