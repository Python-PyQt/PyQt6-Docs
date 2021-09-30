:orphan:

.. sip:class:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWebEngineQuick/QQuickWebEngineProfile-c.rst

    .. sip:enum:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.HttpCacheType
        :description: QtWebEngineQuick/QQuickWebEngineProfile-HttpCacheType-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.HttpCacheType.DiskHttpCache
            :description: QtWebEngineQuick/QQuickWebEngineProfile-HttpCacheType-DiskHttpCache-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.HttpCacheType.MemoryHttpCache
            :description: QtWebEngineQuick/QQuickWebEngineProfile-HttpCacheType-MemoryHttpCache-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.HttpCacheType.NoCache
            :description: QtWebEngineQuick/QQuickWebEngineProfile-HttpCacheType-NoCache-v.rst

    .. sip:enum:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy
        :description: QtWebEngineQuick/QQuickWebEngineProfile-PersistentCookiesPolicy-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies
            :description: QtWebEngineQuick/QQuickWebEngineProfile-PersistentCookiesPolicy-AllowPersistentCookies-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies
            :description: QtWebEngineQuick/QQuickWebEngineProfile-PersistentCookiesPolicy-ForcePersistentCookies-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy.NoPersistentCookies
            :description: QtWebEngineQuick/QQuickWebEngineProfile-PersistentCookiesPolicy-NoPersistentCookies-v.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWebEngineQuick/QQuickWebEngineProfile-__init__-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.cachePath
        :returns:
            str
        :description: QtWebEngineQuick/QQuickWebEngineProfile-cachePath-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.clearHttpCache
        :description: QtWebEngineQuick/QQuickWebEngineProfile-clearHttpCache-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.clientCertificateStore
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineClientCertificateStore`
        :description: QtWebEngineQuick/QQuickWebEngineProfile-clientCertificateStore-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.cookieStore
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineCookieStore`
        :description: QtWebEngineQuick/QQuickWebEngineProfile-cookieStore-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.defaultProfile
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile`
        :static:
        :description: QtWebEngineQuick/QQuickWebEngineProfile-defaultProfile-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.downloadPath
        :returns:
            str
        :description: QtWebEngineQuick/QQuickWebEngineProfile-downloadPath-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.httpAcceptLanguage
        :returns:
            str
        :description: QtWebEngineQuick/QQuickWebEngineProfile-httpAcceptLanguage-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.httpCacheMaximumSize
        :returns:
            int
        :description: QtWebEngineQuick/QQuickWebEngineProfile-httpCacheMaximumSize-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.httpCacheType
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.HttpCacheType`
        :description: QtWebEngineQuick/QQuickWebEngineProfile-httpCacheType-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.httpUserAgent
        :returns:
            str
        :description: QtWebEngineQuick/QQuickWebEngineProfile-httpUserAgent-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.installUrlSchemeHandler
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler`
        :description: QtWebEngineQuick/QQuickWebEngineProfile-installUrlSchemeHandler-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.isOffTheRecord
        :returns:
            bool
        :description: QtWebEngineQuick/QQuickWebEngineProfile-isOffTheRecord-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.isSpellCheckEnabled
        :returns:
            bool
        :description: QtWebEngineQuick/QQuickWebEngineProfile-isSpellCheckEnabled-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.persistentCookiesPolicy
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy`
        :description: QtWebEngineQuick/QQuickWebEngineProfile-persistentCookiesPolicy-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.persistentStoragePath
        :returns:
            str
        :description: QtWebEngineQuick/QQuickWebEngineProfile-persistentStoragePath-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.removeAllUrlSchemeHandlers
        :description: QtWebEngineQuick/QQuickWebEngineProfile-removeAllUrlSchemeHandlers-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.removeUrlScheme
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtWebEngineQuick/QQuickWebEngineProfile-removeUrlScheme-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.removeUrlSchemeHandler
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler`
        :description: QtWebEngineQuick/QQuickWebEngineProfile-removeUrlSchemeHandler-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.setCachePath
        :args:
            str
        :description: QtWebEngineQuick/QQuickWebEngineProfile-setCachePath-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.setDownloadPath
        :args:
            str
        :description: QtWebEngineQuick/QQuickWebEngineProfile-setDownloadPath-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.setHttpAcceptLanguage
        :args:
            str
        :description: QtWebEngineQuick/QQuickWebEngineProfile-setHttpAcceptLanguage-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.setHttpCacheMaximumSize
        :args:
            int
        :description: QtWebEngineQuick/QQuickWebEngineProfile-setHttpCacheMaximumSize-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.setHttpCacheType
        :args:
            :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.HttpCacheType`
        :description: QtWebEngineQuick/QQuickWebEngineProfile-setHttpCacheType-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.setHttpUserAgent
        :args:
            str
        :description: QtWebEngineQuick/QQuickWebEngineProfile-setHttpUserAgent-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.setOffTheRecord
        :args:
            bool
        :description: QtWebEngineQuick/QQuickWebEngineProfile-setOffTheRecord-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.setPersistentCookiesPolicy
        :args:
            :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy`
        :description: QtWebEngineQuick/QQuickWebEngineProfile-setPersistentCookiesPolicy-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.setPersistentStoragePath
        :args:
            str
        :description: QtWebEngineQuick/QQuickWebEngineProfile-setPersistentStoragePath-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.setSpellCheckEnabled
        :args:
            bool
        :description: QtWebEngineQuick/QQuickWebEngineProfile-setSpellCheckEnabled-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.setSpellCheckLanguages
        :args:
            Iterable[str]
        :description: QtWebEngineQuick/QQuickWebEngineProfile-setSpellCheckLanguages-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.setStorageName
        :args:
            str
        :description: QtWebEngineQuick/QQuickWebEngineProfile-setStorageName-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.setUrlRequestInterceptor
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestInterceptor`
        :description: QtWebEngineQuick/QQuickWebEngineProfile-setUrlRequestInterceptor-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.spellCheckLanguages
        :returns:
            List[str]
        :description: QtWebEngineQuick/QQuickWebEngineProfile-spellCheckLanguages-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.storageName
        :returns:
            str
        :description: QtWebEngineQuick/QQuickWebEngineProfile-storageName-f.rst

    .. sip:method:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.urlSchemeHandler
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler`
        :description: QtWebEngineQuick/QQuickWebEngineProfile-urlSchemeHandler-f.rst

    .. sip:signal:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.cachePathChanged
        :description: QtWebEngineQuick/QQuickWebEngineProfile-cachePathChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.downloadPathChanged
        :description: QtWebEngineQuick/QQuickWebEngineProfile-downloadPathChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.httpAcceptLanguageChanged
        :description: QtWebEngineQuick/QQuickWebEngineProfile-httpAcceptLanguageChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.httpCacheMaximumSizeChanged
        :description: QtWebEngineQuick/QQuickWebEngineProfile-httpCacheMaximumSizeChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.httpCacheTypeChanged
        :description: QtWebEngineQuick/QQuickWebEngineProfile-httpCacheTypeChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.httpUserAgentChanged
        :description: QtWebEngineQuick/QQuickWebEngineProfile-httpUserAgentChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.offTheRecordChanged
        :description: QtWebEngineQuick/QQuickWebEngineProfile-offTheRecordChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.persistentCookiesPolicyChanged
        :description: QtWebEngineQuick/QQuickWebEngineProfile-persistentCookiesPolicyChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.persistentStoragePathChanged
        :description: QtWebEngineQuick/QQuickWebEngineProfile-persistentStoragePathChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.presentNotification
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineNotification`
        :description: QtWebEngineQuick/QQuickWebEngineProfile-presentNotification-s.rst

    .. sip:signal:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.spellCheckEnabledChanged
        :description: QtWebEngineQuick/QQuickWebEngineProfile-spellCheckEnabledChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.spellCheckLanguagesChanged
        :description: QtWebEngineQuick/QQuickWebEngineProfile-spellCheckLanguagesChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.storageNameChanged
        :description: QtWebEngineQuick/QQuickWebEngineProfile-storageNameChanged-s.rst
