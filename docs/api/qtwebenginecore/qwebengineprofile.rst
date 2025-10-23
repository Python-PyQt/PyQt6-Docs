:orphan:

.. sip:class:: PyQt6.QtWebEngineCore.QWebEngineProfile
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWebEngineCore/QWebEngineProfile-c.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineProfile.HttpCacheType
        :description: QtWebEngineCore/QWebEngineProfile-HttpCacheType-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineProfile.HttpCacheType.DiskHttpCache
            :description: QtWebEngineCore/QWebEngineProfile-HttpCacheType-DiskHttpCache-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineProfile.HttpCacheType.MemoryHttpCache
            :description: QtWebEngineCore/QWebEngineProfile-HttpCacheType-MemoryHttpCache-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineProfile.HttpCacheType.NoCache
            :description: QtWebEngineCore/QWebEngineProfile-HttpCacheType-NoCache-v.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentCookiesPolicy
        :description: QtWebEngineCore/QWebEngineProfile-PersistentCookiesPolicy-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies
            :description: QtWebEngineCore/QWebEngineProfile-PersistentCookiesPolicy-AllowPersistentCookies-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies
            :description: QtWebEngineCore/QWebEngineProfile-PersistentCookiesPolicy-ForcePersistentCookies-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentCookiesPolicy.NoPersistentCookies
            :description: QtWebEngineCore/QWebEngineProfile-PersistentCookiesPolicy-NoPersistentCookies-v.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentPermissionsPolicy
        :description: QtWebEngineCore/QWebEngineProfile-PersistentPermissionsPolicy-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentPermissionsPolicy.AskEveryTime
            :description: QtWebEngineCore/QWebEngineProfile-PersistentPermissionsPolicy-AskEveryTime-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentPermissionsPolicy.StoreInMemory
            :description: QtWebEngineCore/QWebEngineProfile-PersistentPermissionsPolicy-StoreInMemory-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentPermissionsPolicy.StoreOnDisk
            :description: QtWebEngineCore/QWebEngineProfile-PersistentPermissionsPolicy-StoreOnDisk-v.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWebEngineCore/QWebEngineProfile-__init__-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.__init__
        :args:
            Optional[str]
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWebEngineCore/QWebEngineProfile-__init__-f-2.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.additionalTrustedCertificates
        :returns:
            list[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :description: QtWebEngineCore/QWebEngineProfile-additionalTrustedCertificates-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.cachePath
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineProfile-cachePath-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.clearAllVisitedLinks
        :description: QtWebEngineCore/QWebEngineProfile-clearAllVisitedLinks-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.clearHttpCache
        :description: QtWebEngineCore/QWebEngineProfile-clearHttpCache-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.clearVisitedLinks
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QUrl`]
        :description: QtWebEngineCore/QWebEngineProfile-clearVisitedLinks-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.clientCertificateStore
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineClientCertificateStore`
        :description: QtWebEngineCore/QWebEngineProfile-clientCertificateStore-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.clientHints
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineClientHints`
        :description: QtWebEngineCore/QWebEngineProfile-clientHints-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.cookieStore
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineCookieStore`
        :description: QtWebEngineCore/QWebEngineProfile-cookieStore-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.defaultProfile
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile`
        :static:
        :description: QtWebEngineCore/QWebEngineProfile-defaultProfile-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.downloadPath
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineProfile-downloadPath-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.extensionManager
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager`
        :description: QtWebEngineCore/QWebEngineProfile-extensionManager-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.httpAcceptLanguage
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineProfile-httpAcceptLanguage-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.httpCacheMaximumSize
        :returns:
            int
        :description: QtWebEngineCore/QWebEngineProfile-httpCacheMaximumSize-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.httpCacheType
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.HttpCacheType`
        :description: QtWebEngineCore/QWebEngineProfile-httpCacheType-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.httpUserAgent
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineProfile-httpUserAgent-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.installUrlSchemeHandler
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler`
        :description: QtWebEngineCore/QWebEngineProfile-installUrlSchemeHandler-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.isOffTheRecord
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineProfile-isOffTheRecord-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.isPushServiceEnabled
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineProfile-isPushServiceEnabled-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.isSpellCheckEnabled
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineProfile-isSpellCheckEnabled-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.listAllPermissions
        :returns:
            list[:sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission`]
        :description: QtWebEngineCore/QWebEngineProfile-listAllPermissions-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.listPermissionsForOrigin
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :returns:
            list[:sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission`]
        :description: QtWebEngineCore/QWebEngineProfile-listPermissionsForOrigin-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.listPermissionsForPermissionType
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType`
        :returns:
            list[:sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission`]
        :description: QtWebEngineCore/QWebEngineProfile-listPermissionsForPermissionType-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.persistentCookiesPolicy
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentCookiesPolicy`
        :description: QtWebEngineCore/QWebEngineProfile-persistentCookiesPolicy-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.persistentPermissionsPolicy
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentPermissionsPolicy`
        :description: QtWebEngineCore/QWebEngineProfile-persistentPermissionsPolicy-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.persistentStoragePath
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineProfile-persistentStoragePath-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.queryPermission
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.PermissionType`
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission`
        :description: QtWebEngineCore/QWebEngineProfile-queryPermission-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.removeAllUrlSchemeHandlers
        :description: QtWebEngineCore/QWebEngineProfile-removeAllUrlSchemeHandlers-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.removeUrlScheme
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtWebEngineCore/QWebEngineProfile-removeUrlScheme-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.removeUrlSchemeHandler
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler`
        :description: QtWebEngineCore/QWebEngineProfile-removeUrlSchemeHandler-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.requestIconForIconURL
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            int
            Callable[[:sip:ref:`~PyQt6.QtGui.QIcon`, :sip:ref:`~PyQt6.QtCore.QUrl`], None]
        :description: QtWebEngineCore/QWebEngineProfile-requestIconForIconURL-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.requestIconForPageURL
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            int
            Callable[[:sip:ref:`~PyQt6.QtGui.QIcon`, :sip:ref:`~PyQt6.QtCore.QUrl`, :sip:ref:`~PyQt6.QtCore.QUrl`], None]
        :description: QtWebEngineCore/QWebEngineProfile-requestIconForPageURL-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.scripts
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineScriptCollection`
        :description: QtWebEngineCore/QWebEngineProfile-scripts-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setCachePath
        :args:
            Optional[str]
        :description: QtWebEngineCore/QWebEngineProfile-setCachePath-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setDownloadPath
        :args:
            Optional[str]
        :description: QtWebEngineCore/QWebEngineProfile-setDownloadPath-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setHttpAcceptLanguage
        :args:
            Optional[str]
        :description: QtWebEngineCore/QWebEngineProfile-setHttpAcceptLanguage-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setHttpCacheMaximumSize
        :args:
            int
        :description: QtWebEngineCore/QWebEngineProfile-setHttpCacheMaximumSize-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setHttpCacheType
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.HttpCacheType`
        :description: QtWebEngineCore/QWebEngineProfile-setHttpCacheType-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setHttpUserAgent
        :args:
            Optional[str]
        :description: QtWebEngineCore/QWebEngineProfile-setHttpUserAgent-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setNotificationPresenter
        :args:
            Callable[[:sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineNotification`], None]
        :description: QtWebEngineCore/QWebEngineProfile-setNotificationPresenter-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setPersistentCookiesPolicy
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentCookiesPolicy`
        :description: QtWebEngineCore/QWebEngineProfile-setPersistentCookiesPolicy-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setPersistentPermissionsPolicy
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentPermissionsPolicy`
        :description: QtWebEngineCore/QWebEngineProfile-setPersistentPermissionsPolicy-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setPersistentStoragePath
        :args:
            Optional[str]
        :description: QtWebEngineCore/QWebEngineProfile-setPersistentStoragePath-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setPushServiceEnabled
        :args:
            bool
        :description: QtWebEngineCore/QWebEngineProfile-setPushServiceEnabled-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setSpellCheckEnabled
        :args:
            bool
        :description: QtWebEngineCore/QWebEngineProfile-setSpellCheckEnabled-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setSpellCheckLanguages
        :args:
            Iterable[Optional[str]]
        :description: QtWebEngineCore/QWebEngineProfile-setSpellCheckLanguages-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.settings
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineSettings`
        :description: QtWebEngineCore/QWebEngineProfile-settings-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setUrlRequestInterceptor
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestInterceptor`
        :description: QtWebEngineCore/QWebEngineProfile-setUrlRequestInterceptor-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.spellCheckLanguages
        :returns:
            list[str]
        :description: QtWebEngineCore/QWebEngineProfile-spellCheckLanguages-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.storageName
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineProfile-storageName-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.urlSchemeHandler
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler`
        :description: QtWebEngineCore/QWebEngineProfile-urlSchemeHandler-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.visitedLinksContainsUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineProfile-visitedLinksContainsUrl-f.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineProfile.clearHttpCacheCompleted
        :description: QtWebEngineCore/QWebEngineProfile-clearHttpCacheCompleted-s.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineProfile.downloadRequested
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest`
        :description: QtWebEngineCore/QWebEngineProfile-downloadRequested-s.rst
