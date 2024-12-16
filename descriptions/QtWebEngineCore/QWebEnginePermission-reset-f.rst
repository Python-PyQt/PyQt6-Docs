.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: () const
    :digest: eaf97bd9501a496104c759091dbd6927

Removes the permission from the profile's underlying storage. By default, permissions are stored on disk (except for off-the-record profiles, where permissions are stored in memory and are destroyed with the profile). This means that an already granted/denied permission will not be requested twice, but will get automatically granted/denied every subsequent time a website requests it. Calling reset() allows the query to be displayed again the next time the website requests it.

Does nothing when :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.isValid` evaluates to false.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.grant`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.deny`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePermission.isValid`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.persistentPermissionsPolicy`.
