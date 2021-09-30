.. sip:class-description::
    :status: todo
    :brief: Web engine profile shared by multiple pages
    :digest: e8250eeaa919fad2a9f1c77b21ac44f0

The :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile` class provides a web engine profile shared by multiple pages.

A web engine profile contains settings, scripts, persistent cookie policy, and the list of visited links shared by all web engine pages that belong to the profile.

Information about visited links is stored together with persistent cookies and other persistent data in a storage determined by the :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.storageName` property. Persistent data is stored in a subdirectory determined by the :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.persistentStoragePath` property and the cache in a subdirectory determined by the :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.cachePath` property. The :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.httpCacheType` property describes the type of the cache: *in-memory* or *on-disk*. If only the :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.storageName` property is set, the other values are generated automatically based on it. If you specify any of the values manually, you should do it before creating any pages that belong to the profile.

Profiles can be used to isolate pages from each other. A typical use case is a dedicated *off-the-record profile* for a *private browsing* mode. An off-the-record profile forces cookies, the HTTP cache, and other normally persistent data to be stored only in memory. The offTheRecord property holds whether a profile is off-the-record.

The default profile can be accessed by :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.defaultProfile`. It is a built-in profile that all web pages not specifically created with another profile belong to.

A `WebEngineProfile <https://doc.qt.io/qt-6/qml-qtwebengine-webengineprofile.html>`_ instance can be created and accessed from C++ through the :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile` class, which exposes further functionality in C++. This allows Qt Quick applications to intercept URL requests (QQuickWebEngineProfile::setRequestInterceptor), or register custom URL schemes (\ :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.installUrlSchemeHandler`).

Spellchecking HTML form fields can be enabled per profile by setting the spellCheckEnabled property and the current languages used for spellchecking can be set by using the :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.spellCheckLanguages` property.
