.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 14ca7b93eb3aeb31fb67705d2a11931f

Removes the query string pair whose key is equal to *key* from the URL. If there are multiple items with a key equal to *key*, it removes the first item in the order they were present in the query string or added with :sip:ref:`~PyQt6.QtCore.QUrlQuery.addQueryItem`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrlQuery.removeAllQueryItems`.
