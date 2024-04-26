.. sip:method-description::
    :status: todo
    :pysig: 409d34ebd31ca65e87a8400a0828c66d
    :realsig: (QWebEngineProfile::HttpCacheType)
    :digest: 3f460c2262a64ccc561db35fa7dc7b9c

Sets the HTTP cache type to *httpCacheType*.

**Note:** Setting the *httpCacheType* to :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.HttpCacheType.NoCache` on the profile, which has already some cache entries does not trigger the removal of those entries.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.httpCacheType`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setCachePath`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.clearHttpCache`.
