.. sip:method-description::
    :status: todo
    :pysig: 510cf367f4d3c66c653e9cb48eb8aeb3
    :realsig: (qsizetype, QAnyStringView, QAnyStringView)
    :digest: 8e7f379b854d1a9a5007d134ac603e5b

Inserts a header entry at index *i*, with *name* and *value*. The index must be valid (see :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders.size`). Returns whether the insert succeeded.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders.append`, insert(qsizetype, QHttpHeaders::WellKnownHeader, QAnyStringView), :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders.size`, :ref:`qhttpheaders-allowed-field-name-and-value-characters`.
