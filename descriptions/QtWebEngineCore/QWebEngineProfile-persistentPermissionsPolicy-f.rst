.. sip:method-description::
    :status: todo
    :pysig: ce1654c31c96e5120888d7c5336bd2cd
    :realsig: () const
    :digest: c6a266190a45a89986c03045d2545e27

Returns the current policy for persistent permissions.

Off-the-record profiles are not allowed to save data to the disk, so they can only return ``StoreInMemory`` or ``AskEveryTime``.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.PersistentPermissionsPolicy`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setPersistentPermissionsPolicy`.
