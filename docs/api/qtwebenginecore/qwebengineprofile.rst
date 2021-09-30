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

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWebEngineCore/QWebEngineProfile-__init__-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.__init__
        :args:
            str
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWebEngineCore/QWebEngineProfile-__init__-f-1.rst

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
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler`
        :description: QtWebEngineCore/QWebEngineProfile-installUrlSchemeHandler-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.isOffTheRecord
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineProfile-isOffTheRecord-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.isSpellCheckEnabled
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineProfile-isSpellCheckEnabled-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.persistentCookiesPolicy
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentCookiesPolicy`
        :description: QtWebEngineCore/QWebEngineProfile-persistentCookiesPolicy-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.persistentStoragePath
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineProfile-persistentStoragePath-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.removeAllUrlSchemeHandlers
        :description: QtWebEngineCore/QWebEngineProfile-removeAllUrlSchemeHandlers-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.removeUrlScheme
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtWebEngineCore/QWebEngineProfile-removeUrlScheme-f.rst

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
            str
        :description: QtWebEngineCore/QWebEngineProfile-setCachePath-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setDownloadPath
        :args:
            str
        :description: QtWebEngineCore/QWebEngineProfile-setDownloadPath-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setHttpAcceptLanguage
        :args:
            str
        :description: QtWebEngineCore/QWebEngineProfile-setHttpAcceptLanguage-f.rst

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
            str
        :description: QtWebEngineCore/QWebEngineProfile-setHttpUserAgent-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setNotificationPresenter
        :args:
            Callable[[:sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineNotification`], None]
        :description: QtWebEngineCore/QWebEngineProfile-setNotificationPresenter-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setPersistentCookiesPolicy
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentCookiesPolicy`
        :description: QtWebEngineCore/QWebEngineProfile-setPersistentCookiesPolicy-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setPersistentStoragePath
        :args:
            str
        :description: QtWebEngineCore/QWebEngineProfile-setPersistentStoragePath-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setSpellCheckEnabled
        :args:
            bool
        :description: QtWebEngineCore/QWebEngineProfile-setSpellCheckEnabled-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.setSpellCheckLanguages
        :args:
            Iterable[str]
        :description: QtWebEngineCore/QWebEngineProfile-setSpellCheckLanguages-f.rst

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
            List[str]
        :description: QtWebEngineCore/QWebEngineProfile-spellCheckLanguages-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.storageName
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineProfile-storageName-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.urlSchemeHandler
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler`
        :description: QtWebEngineCore/QWebEngineProfile-urlSchemeHandler-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineProfile.visitedLinksContainsUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineProfile-visitedLinksContainsUrl-f.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineProfile.downloadRequested
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest`
        :description: QtWebEngineCore/QWebEngineProfile-downloadRequested-s.rst
