.. sip:class-description::
    :status: todo
    :brief: Web engine profile shared by multiple pages
    :digest: 918c16f44876ec57aa1c955f4a5f414c

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile` class provides a web engine profile shared by multiple pages.

A web engine profile contains settings, scripts, persistent cookie policy, and the list of visited links shared by all web engine pages that belong to the profile.

All pages that belong to the profile share a common :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineSettings` instance, which can be accessed with the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.settings` method. Likewise, the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.scripts` method provides access to a common :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineScriptCollection` instance.

Information about visited links is stored together with persistent cookies and other persistent data in a storage returned by :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.storageName`. Persistent data is stored in a subdirectory set by calling :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setPersistentStoragePath`, and the cache is located in a subdirectory set by calling :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setCachePath`. The cache type can be set to *in-memory* or *on-disk* by calling :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setHttpCacheType`. If only the storage name is set, the subdirectories are created and named automatically. If you set any of the values manually, you should do it before creating any pages that belong to the profile.

The cache can be cleared of links by calling :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.clearVisitedLinks` or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.clearAllVisitedLinks`. :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentCookiesPolicy.PersistentCookiesPolicy` describes whether session and persistent cookies are saved to and restored from memory or disk.

Profiles can be used to isolate pages from each other. A typical use case is a dedicated *off-the-record profile* for a *private browsing* mode. Using :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile` without defining a storage name constructs a new off-the-record profile that leaves no record on the local machine, and has no persistent data or cache. The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.isOffTheRecord` method can be used to check whether a profile is off-the-record.

The default profile can be accessed by :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.defaultProfile`. It is a built-in profile that all web pages not specifically created with another profile belong to.

Implementing the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestInterceptor` interface and registering the interceptor on a profile by :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setUrlRequestInterceptor` enables intercepting, blocking, and modifying URL requests (\ :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestInfo`) before they reach the networking stack of Chromium.

A :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler` can be registered for a profile by :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.installUrlSchemeHandler` to add support for custom URL schemes. Requests for the scheme are then issued to :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler.requestStarted` as :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob` objects.

Spellchecking HTML form fields can be enabled per profile by using the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setSpellCheckEnabled` method and the current languages used for spellchecking can be set by using the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setSpellCheckLanguages` method.
