.. sip:method-description::
    :status: todo
    :pysig: 97848922537a54cee114e3d2ed9a4aee
    :realsig: (QJsonParseError*)
    :digest: cd21d777c9d28e7f2ba5c8315ecccc10

Returns the received data as a :sip:ref:`~PyQt6.QtCore.QJsonDocument`.

The returned value is wrapped in ``std::optional``. If the conversion from the received data fails (empty data or JSON parsing error), ``std::nullopt`` is returned, and *error* is filled with details.

Calling this function consumes the received data, and any further calls to get response data will return empty.

This function returns ``std::nullopt`` and will not consume any data if the reply is not finished. If *error* is passed, it will be set to :sip:ref:`~PyQt6.QtCore.QJsonParseError.ParseError.NoError` to distinguish this case from an actual error.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QRestReply.readBody`, :sip:ref:`~PyQt6.QtNetwork.QRestReply.readText`.
