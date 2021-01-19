:orphan:

.. sip:class:: PyQt6.QtCore.QSettings
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCore/QSettings-c.rst

    .. sip:enum:: PyQt6.QtCore.QSettings.Format
        :description: QtCore/QSettings-Format-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QSettings.Format.IniFormat
            :description: QtCore/QSettings-Format-IniFormat-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSettings.Format.InvalidFormat
            :description: QtCore/QSettings-Format-InvalidFormat-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSettings.Format.NativeFormat
            :description: QtCore/QSettings-Format-NativeFormat-v.rst

    .. sip:enum:: PyQt6.QtCore.QSettings.Scope
        :description: QtCore/QSettings-Scope-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QSettings.Scope.SystemScope
            :description: QtCore/QSettings-Scope-SystemScope-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSettings.Scope.UserScope
            :description: QtCore/QSettings-Scope-UserScope-v.rst

    .. sip:enum:: PyQt6.QtCore.QSettings.Status
        :description: QtCore/QSettings-Status-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QSettings.Status.AccessError
            :description: QtCore/QSettings-Status-AccessError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSettings.Status.FormatError
            :description: QtCore/QSettings-Status-FormatError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QSettings.Status.NoError
            :description: QtCore/QSettings-Status-NoError-v.rst

    .. sip:method:: PyQt6.QtCore.QSettings.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QSettings-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QSettings.Scope`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QSettings-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSettings.__init__
        :args:
            str
            application: str = ''
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QSettings-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QSettings.__init__
        :args:
            str
            :sip:ref:`~PyQt6.QtCore.QSettings.Format`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QSettings-__init__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QSettings.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QSettings.Scope`
            str
            application: str = ''
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QSettings-__init__-f-4.rst

    .. sip:method:: PyQt6.QtCore.QSettings.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QSettings.Format`
            :sip:ref:`~PyQt6.QtCore.QSettings.Scope`
            str
            application: str = ''
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QSettings-__init__-f-5.rst

    .. sip:method:: PyQt6.QtCore.QSettings.allKeys
        :returns:
            List[str]
        :description: QtCore/QSettings-allKeys-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.applicationName
        :returns:
            str
        :description: QtCore/QSettings-applicationName-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.beginGroup
        :args:
            str
        :description: QtCore/QSettings-beginGroup-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.beginReadArray
        :args:
            str
        :returns:
            int
        :description: QtCore/QSettings-beginReadArray-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.beginWriteArray
        :args:
            str
            size: int = -1
        :description: QtCore/QSettings-beginWriteArray-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.childGroups
        :returns:
            List[str]
        :description: QtCore/QSettings-childGroups-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.childKeys
        :returns:
            List[str]
        :description: QtCore/QSettings-childKeys-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.clear
        :description: QtCore/QSettings-clear-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.contains
        :args:
            str
        :returns:
            bool
        :description: QtCore/QSettings-contains-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.defaultFormat
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSettings.Format`
        :static:
        :description: QtCore/QSettings-defaultFormat-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.endArray
        :description: QtCore/QSettings-endArray-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.endGroup
        :description: QtCore/QSettings-endGroup-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtCore/QSettings-event-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.fallbacksEnabled
        :returns:
            bool
        :description: QtCore/QSettings-fallbacksEnabled-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.fileName
        :returns:
            str
        :description: QtCore/QSettings-fileName-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.format
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSettings.Format`
        :description: QtCore/QSettings-format-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.group
        :returns:
            str
        :description: QtCore/QSettings-group-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.isAtomicSyncRequired
        :returns:
            bool
        :description: QtCore/QSettings-isAtomicSyncRequired-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.isWritable
        :returns:
            bool
        :description: QtCore/QSettings-isWritable-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.organizationName
        :returns:
            str
        :description: QtCore/QSettings-organizationName-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.remove
        :args:
            str
        :description: QtCore/QSettings-remove-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.scope
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSettings.Scope`
        :description: QtCore/QSettings-scope-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.setArrayIndex
        :args:
            int
        :description: QtCore/QSettings-setArrayIndex-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.setAtomicSyncRequired
        :args:
            bool
        :description: QtCore/QSettings-setAtomicSyncRequired-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.setDefaultFormat
        :args:
            :sip:ref:`~PyQt6.QtCore.QSettings.Format`
        :static:
        :description: QtCore/QSettings-setDefaultFormat-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.setFallbacksEnabled
        :args:
            bool
        :description: QtCore/QSettings-setFallbacksEnabled-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.setPath
        :args:
            :sip:ref:`~PyQt6.QtCore.QSettings.Format`
            :sip:ref:`~PyQt6.QtCore.QSettings.Scope`
            str
        :static:
        :description: QtCore/QSettings-setPath-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.setValue
        :args:
            str
            Any
        :description: QtCore/QSettings-setValue-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.status
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSettings.Status`
        :description: QtCore/QSettings-status-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.sync
        :description: QtCore/QSettings-sync-f.rst

    .. sip:method:: PyQt6.QtCore.QSettings.value
        :args:
            str
            defaultValue: Any = None
            type: type = None
        :returns:
            object
        :description: QtCore/QSettings-value-f.rst
