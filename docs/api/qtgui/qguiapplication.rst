:orphan:

.. sip:class:: PyQt6.QtGui.QGuiApplication
    :inherits: :sip:ref:`~PyQt6.QtCore.QCoreApplication`
    :description: QtGui/QGuiApplication-c.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.__init__
        :args:
            list[str]
        :description: QtGui/QGuiApplication-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.allWindows
        :returns:
            list[:sip:ref:`~PyQt6.QtGui.QWindow`]
        :static:
        :description: QtGui/QGuiApplication-allWindows-f-1.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.applicationDisplayName
        :returns:
            str
        :static:
        :description: QtGui/QGuiApplication-applicationDisplayName-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.applicationState
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ApplicationState`
        :static:
        :description: QtGui/QGuiApplication-applicationState-f-1.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.changeOverrideCursor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QCursor`, :sip:ref:`~PyQt6.QtCore.Qt.CursorShape`]
        :static:
        :description: QtGui/QGuiApplication-changeOverrideCursor-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.clipboard
        :returns:
            :sip:ref:`~PyQt6.QtGui.QClipboard`
        :static:
        :description: QtGui/QGuiApplication-clipboard-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.desktopFileName
        :returns:
            str
        :static:
        :description: QtGui/QGuiApplication-desktopFileName-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.desktopSettingsAware
        :returns:
            bool
        :static:
        :description: QtGui/QGuiApplication-desktopSettingsAware-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.devicePixelRatio
        :returns:
            float
        :description: QtGui/QGuiApplication-devicePixelRatio-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtGui/QGuiApplication-event-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.exec
        :returns:
            int
        :static:
        :description: QtGui/QGuiApplication-exec-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.focusObject
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :static:
        :description: QtGui/QGuiApplication-focusObject-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.focusWindow
        :returns:
            :sip:ref:`~PyQt6.QtGui.QWindow`
        :static:
        :description: QtGui/QGuiApplication-focusWindow-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.font
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :static:
        :description: QtGui/QGuiApplication-font-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.highDpiScaleFactorRoundingPolicy
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.HighDpiScaleFactorRoundingPolicy`
        :static:
        :description: QtGui/QGuiApplication-highDpiScaleFactorRoundingPolicy-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.inputMethod
        :returns:
            :sip:ref:`~PyQt6.QtGui.QInputMethod`
        :static:
        :description: QtGui/QGuiApplication-inputMethod-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.isLeftToRight
        :returns:
            bool
        :static:
        :description: QtGui/QGuiApplication-isLeftToRight-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.isRightToLeft
        :returns:
            bool
        :static:
        :description: QtGui/QGuiApplication-isRightToLeft-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.isSavingSession
        :returns:
            bool
        :description: QtGui/QGuiApplication-isSavingSession-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.isSessionRestored
        :returns:
            bool
        :description: QtGui/QGuiApplication-isSessionRestored-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.keyboardModifiers
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier`
        :static:
        :description: QtGui/QGuiApplication-keyboardModifiers-f-1.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.layoutDirection
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.LayoutDirection`
        :static:
        :description: QtGui/QGuiApplication-layoutDirection-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.modalWindow
        :returns:
            :sip:ref:`~PyQt6.QtGui.QWindow`
        :static:
        :description: QtGui/QGuiApplication-modalWindow-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.mouseButtons
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.MouseButton`
        :static:
        :description: QtGui/QGuiApplication-mouseButtons-f-1.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.notify
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtGui/QGuiApplication-notify-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.overrideCursor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QCursor`
        :static:
        :description: QtGui/QGuiApplication-overrideCursor-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.palette
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPalette`
        :static:
        :description: QtGui/QGuiApplication-palette-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.platformName
        :returns:
            str
        :static:
        :description: QtGui/QGuiApplication-platformName-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.primaryScreen
        :returns:
            :sip:ref:`~PyQt6.QtGui.QScreen`
        :static:
        :description: QtGui/QGuiApplication-primaryScreen-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.queryKeyboardModifiers
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier`
        :static:
        :description: QtGui/QGuiApplication-queryKeyboardModifiers-f-1.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.quitOnLastWindowClosed
        :returns:
            bool
        :static:
        :description: QtGui/QGuiApplication-quitOnLastWindowClosed-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.restoreOverrideCursor
        :static:
        :description: QtGui/QGuiApplication-restoreOverrideCursor-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.screenAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QScreen`
        :static:
        :description: QtGui/QGuiApplication-screenAt-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.screens
        :returns:
            list[:sip:ref:`~PyQt6.QtGui.QScreen`]
        :static:
        :description: QtGui/QGuiApplication-screens-f-1.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.sessionId
        :returns:
            str
        :description: QtGui/QGuiApplication-sessionId-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.sessionKey
        :returns:
            str
        :description: QtGui/QGuiApplication-sessionKey-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.setApplicationDisplayName
        :args:
            Optional[str]
        :static:
        :description: QtGui/QGuiApplication-setApplicationDisplayName-f-1.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.setBadgeNumber
        :args:
            int
        :description: QtGui/QGuiApplication-setBadgeNumber-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.setDesktopFileName
        :args:
            Optional[str]
        :static:
        :description: QtGui/QGuiApplication-setDesktopFileName-f-1.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.setDesktopSettingsAware
        :args:
            bool
        :static:
        :description: QtGui/QGuiApplication-setDesktopSettingsAware-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.setFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :static:
        :description: QtGui/QGuiApplication-setFont-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.HighDpiScaleFactorRoundingPolicy`
        :static:
        :description: QtGui/QGuiApplication-setHighDpiScaleFactorRoundingPolicy-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.setLayoutDirection
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.LayoutDirection`
        :static:
        :description: QtGui/QGuiApplication-setLayoutDirection-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.setOverrideCursor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QCursor`, :sip:ref:`~PyQt6.QtCore.Qt.CursorShape`]
        :static:
        :description: QtGui/QGuiApplication-setOverrideCursor-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.setPalette
        :args:
            :sip:ref:`~PyQt6.QtGui.QPalette`
        :static:
        :description: QtGui/QGuiApplication-setPalette-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.setQuitOnLastWindowClosed
        :args:
            bool
        :static:
        :description: QtGui/QGuiApplication-setQuitOnLastWindowClosed-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.setWindowIcon
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :static:
        :description: QtGui/QGuiApplication-setWindowIcon-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.styleHints
        :returns:
            :sip:ref:`~PyQt6.QtGui.QStyleHints`
        :static:
        :description: QtGui/QGuiApplication-styleHints-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.sync
        :static:
        :description: QtGui/QGuiApplication-sync-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.topLevelAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QWindow`
        :static:
        :description: QtGui/QGuiApplication-topLevelAt-f.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.topLevelWindows
        :returns:
            list[:sip:ref:`~PyQt6.QtGui.QWindow`]
        :static:
        :description: QtGui/QGuiApplication-topLevelWindows-f-1.rst

    .. sip:method:: PyQt6.QtGui.QGuiApplication.windowIcon
        :returns:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :static:
        :description: QtGui/QGuiApplication-windowIcon-f.rst

    .. sip:signal:: PyQt6.QtGui.QGuiApplication.applicationDisplayNameChanged
        :description: QtGui/QGuiApplication-applicationDisplayNameChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QGuiApplication.applicationStateChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.ApplicationState`
        :description: QtGui/QGuiApplication-applicationStateChanged-s-1.rst

    .. sip:signal:: PyQt6.QtGui.QGuiApplication.commitDataRequest
        :args:
            :sip:ref:`~PyQt6.QtGui.QSessionManager`
        :description: QtGui/QGuiApplication-commitDataRequest-s.rst

    .. sip:signal:: PyQt6.QtGui.QGuiApplication.focusObjectChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtGui/QGuiApplication-focusObjectChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QGuiApplication.focusWindowChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QWindow`
        :description: QtGui/QGuiApplication-focusWindowChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QGuiApplication.fontDatabaseChanged
        :description: QtGui/QGuiApplication-fontDatabaseChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QGuiApplication.lastWindowClosed
        :description: QtGui/QGuiApplication-lastWindowClosed-s.rst

    .. sip:signal:: PyQt6.QtGui.QGuiApplication.layoutDirectionChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.LayoutDirection`
        :description: QtGui/QGuiApplication-layoutDirectionChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QGuiApplication.primaryScreenChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QScreen`
        :description: QtGui/QGuiApplication-primaryScreenChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QGuiApplication.saveStateRequest
        :args:
            :sip:ref:`~PyQt6.QtGui.QSessionManager`
        :description: QtGui/QGuiApplication-saveStateRequest-s.rst

    .. sip:signal:: PyQt6.QtGui.QGuiApplication.screenAdded
        :args:
            :sip:ref:`~PyQt6.QtGui.QScreen`
        :description: QtGui/QGuiApplication-screenAdded-s.rst

    .. sip:signal:: PyQt6.QtGui.QGuiApplication.screenRemoved
        :args:
            :sip:ref:`~PyQt6.QtGui.QScreen`
        :description: QtGui/QGuiApplication-screenRemoved-s.rst
