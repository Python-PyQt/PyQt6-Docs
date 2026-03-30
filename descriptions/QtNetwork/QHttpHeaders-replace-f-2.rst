.. sip:method-description::
    :status: todo
    :pysig: 510cf367f4d3c66c653e9cb48eb8aeb3
    :realsig: (qsizetype, QAnyStringView, QAnyStringView)
    :digest: 0cbed6fb62eb0ddfc8dbb7bbe30c0e85

Replaces the header entry at index *i*, with *name* and *newValue*. The index must be valid (see :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders.size`). Returns whether the replace succeeded.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders.append`, replace(qsizetype, QHttpHeaders::WellKnownHeader, QAnyStringView), :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders.size`, :ref:`qhttpheaders-allowed-field-name-and-value-characters`.
