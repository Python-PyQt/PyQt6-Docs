.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: a85b815e120d5f8d30121d3aa7461bcd

Removes the query string pair whose key is equal to *key* from the URL. If there are multiple items with a key equal to *key*, it removes the first item in the order they were present in the query string or added with :sip:ref:`~PyQt6.QtCore.QUrlQuery.addQueryItem`.

**Note:** The key is expected to be in percent-encoded form.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrlQuery.removeAllQueryItems`.
