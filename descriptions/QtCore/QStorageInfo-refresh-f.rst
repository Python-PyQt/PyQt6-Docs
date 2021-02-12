.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 81be58b52b47bff6fa46b4ea1e49a299

Resets :sip:ref:`~PyQt6.QtCore.QStorageInfo`'s internal cache.

:sip:ref:`~PyQt6.QtCore.QStorageInfo` caches information about storage to speed up performance. :sip:ref:`~PyQt6.QtCore.QStorageInfo` retrieves information during object construction and/or when calling the :sip:ref:`~PyQt6.QtCore.QStorageInfo.setPath` method. You have to manually reset the cache by calling this function to update storage information.
