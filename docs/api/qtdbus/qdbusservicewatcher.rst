:orphan:

.. sip:class:: PyQt6.QtDBus.QDBusServiceWatcher
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtDBus/QDBusServiceWatcher-c.rst

    .. sip:enum:: PyQt6.QtDBus.QDBusServiceWatcher.WatchModeFlag
        :description: QtDBus/QDBusServiceWatcher-WatchModeFlag-e.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusServiceWatcher.WatchModeFlag.WatchForOwnerChange
            :description: QtDBus/QDBusServiceWatcher-WatchModeFlag-WatchForOwnerChange-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusServiceWatcher.WatchModeFlag.WatchForRegistration
            :description: QtDBus/QDBusServiceWatcher-WatchModeFlag-WatchForRegistration-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusServiceWatcher.WatchModeFlag.WatchForUnregistration
            :description: QtDBus/QDBusServiceWatcher-WatchModeFlag-WatchForUnregistration-v.rst

    .. sip:method:: PyQt6.QtDBus.QDBusServiceWatcher.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtDBus/QDBusServiceWatcher-__init__-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusServiceWatcher.__init__
        :args:
            str
            :sip:ref:`~PyQt6.QtDBus.QDBusConnection`
            watchMode: :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.WatchModeFlag` = :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.WatchModeFlag.WatchForOwnerChange`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtDBus/QDBusServiceWatcher-__init__-f-2.rst

    .. sip:method:: PyQt6.QtDBus.QDBusServiceWatcher.addWatchedService
        :args:
            str
        :description: QtDBus/QDBusServiceWatcher-addWatchedService-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusServiceWatcher.connection
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusConnection`
        :description: QtDBus/QDBusServiceWatcher-connection-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusServiceWatcher.removeWatchedService
        :args:
            str
        :returns:
            bool
        :description: QtDBus/QDBusServiceWatcher-removeWatchedService-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusServiceWatcher.setConnection
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusConnection`
        :description: QtDBus/QDBusServiceWatcher-setConnection-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusServiceWatcher.setWatchedServices
        :args:
            Iterable[str]
        :description: QtDBus/QDBusServiceWatcher-setWatchedServices-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusServiceWatcher.setWatchMode
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.WatchModeFlag`
        :description: QtDBus/QDBusServiceWatcher-setWatchMode-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusServiceWatcher.watchedServices
        :returns:
            List[str]
        :description: QtDBus/QDBusServiceWatcher-watchedServices-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusServiceWatcher.watchMode
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.WatchModeFlag`
        :description: QtDBus/QDBusServiceWatcher-watchMode-f-1.rst

    .. sip:signal:: PyQt6.QtDBus.QDBusServiceWatcher.serviceOwnerChanged
        :args:
            str
            str
            str
        :description: QtDBus/QDBusServiceWatcher-serviceOwnerChanged-s.rst

    .. sip:signal:: PyQt6.QtDBus.QDBusServiceWatcher.serviceRegistered
        :args:
            str
        :description: QtDBus/QDBusServiceWatcher-serviceRegistered-s.rst

    .. sip:signal:: PyQt6.QtDBus.QDBusServiceWatcher.serviceUnregistered
        :args:
            str
        :description: QtDBus/QDBusServiceWatcher-serviceUnregistered-s.rst
