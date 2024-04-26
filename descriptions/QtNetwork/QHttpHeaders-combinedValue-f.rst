.. sip:method-description::
    :status: todo
    :pysig: 731d872c21d87206e749c588dc101bf1
    :realsig: (QAnyStringView) const
    :digest: fc8e86a891e8844df765477b9df0ffdc

Returns the values of header *name* in a comma-combined string. Returns a ``null`` :sip:ref:`~PyQt6.QtCore.QByteArray` if the header with *name* doesn't exist.

**Note:** Accessing the value(s) of 'Set-Cookie' header this way may not work as intended. It is a notable exception in the `HTTP RFC <https://datatracker.ietf.org/doc/html/rfc9110#name-field-order>`_ in that its values cannot be combined this way. Prefer :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders.values` instead.

.. seealso:: values(QAnyStringView).
