:orphan:

.. sip:class:: PyQt6.QtWebEngineCore.QWebEnginePermission
    :description: QtWebEngineCore/QWebEnginePermission-c.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType
        :description: QtWebEngineCore/QWebEnginePermission-PermissionType-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType.ClipboardReadWrite
            :description: QtWebEngineCore/QWebEnginePermission-PermissionType-ClipboardReadWrite-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType.DesktopAudioVideoCapture
            :description: QtWebEngineCore/QWebEnginePermission-PermissionType-DesktopAudioVideoCapture-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType.DesktopVideoCapture
            :description: QtWebEngineCore/QWebEnginePermission-PermissionType-DesktopVideoCapture-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType.Geolocation
            :description: QtWebEngineCore/QWebEnginePermission-PermissionType-Geolocation-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType.LocalFontsAccess
            :description: QtWebEngineCore/QWebEnginePermission-PermissionType-LocalFontsAccess-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType.MediaAudioCapture
            :description: QtWebEngineCore/QWebEnginePermission-PermissionType-MediaAudioCapture-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType.MediaAudioVideoCapture
            :description: QtWebEngineCore/QWebEnginePermission-PermissionType-MediaAudioVideoCapture-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType.MediaVideoCapture
            :description: QtWebEngineCore/QWebEnginePermission-PermissionType-MediaVideoCapture-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType.MouseLock
            :description: QtWebEngineCore/QWebEnginePermission-PermissionType-MouseLock-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType.Notifications
            :description: QtWebEngineCore/QWebEnginePermission-PermissionType-Notifications-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType.Unsupported
            :description: QtWebEngineCore/QWebEnginePermission-PermissionType-Unsupported-v.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEnginePermission.State
        :description: QtWebEngineCore/QWebEnginePermission-State-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.State.Ask
            :description: QtWebEngineCore/QWebEnginePermission-State-Ask-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.State.Denied
            :description: QtWebEngineCore/QWebEnginePermission-State-Denied-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.State.Granted
            :description: QtWebEngineCore/QWebEnginePermission-State-Granted-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEnginePermission.State.Invalid
            :description: QtWebEngineCore/QWebEnginePermission-State-Invalid-v.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEnginePermission.__init__
        :description: QtWebEngineCore/QWebEnginePermission-__init__-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEnginePermission.__init__
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission`
        :description: QtWebEngineCore/QWebEnginePermission-__init__-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEnginePermission.deny
        :description: QtWebEngineCore/QWebEnginePermission-deny-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEnginePermission.__eq__
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission`
        :returns:
            bool
        :description: QtWebEngineCore/QWebEnginePermission-__eq__-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEnginePermission.grant
        :description: QtWebEngineCore/QWebEnginePermission-grant-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEnginePermission.isPersistent
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType`
        :returns:
            bool
        :static:
        :description: QtWebEngineCore/QWebEnginePermission-isPersistent-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEnginePermission.isValid
        :returns:
            bool
        :description: QtWebEngineCore/QWebEnginePermission-isValid-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEnginePermission.__ne__
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission`
        :returns:
            bool
        :description: QtWebEngineCore/QWebEnginePermission-__ne__-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEnginePermission.origin
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWebEngineCore/QWebEnginePermission-origin-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEnginePermission.permissionType
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType`
        :description: QtWebEngineCore/QWebEnginePermission-permissionType-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEnginePermission.reset
        :description: QtWebEngineCore/QWebEnginePermission-reset-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEnginePermission.state
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.State`
        :description: QtWebEngineCore/QWebEnginePermission-state-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEnginePermission.swap
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission`
        :description: QtWebEngineCore/QWebEnginePermission-swap-f.rst
