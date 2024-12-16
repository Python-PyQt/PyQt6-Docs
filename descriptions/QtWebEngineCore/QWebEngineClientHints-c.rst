.. sip:class-description::
    :status: todo
    :brief: Object to customize User-Agent Client Hints used by a profile
    :digest: 5e2b1c17c1a220cd8f7a5601af6a9524

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineClientHints` class provides an object to customize User-Agent Client Hints used by a profile.

:sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineClientHints` allows configuration of exposing browser and platform information via User-Agent response and request headers, and a JavaScript API.

The information accessed via this API is split into two groups: low entropy and high entropy hints. Low entropy hints (\ :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineClientHints.platform` and mobile) are those that do not give away much information; the API makes these accessible with every request and they can not be disabled by :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineClientHints.setAllClientHintsEnabled`.

All the others are high entropy hints; they have the potential to give away more information, therefore they can be disabled by :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineClientHints.setAllClientHintsEnabled`.

Each profile object has its own :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineClientHints` object, which configures the Client Hint settings for that browsing context. If a Client Hint is not configured for a web engine profile, its default value is deduced from the system.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.clientHints`, :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.clientHints`.
