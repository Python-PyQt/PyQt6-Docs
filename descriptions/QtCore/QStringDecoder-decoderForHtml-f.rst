.. sip:method-description::
    :status: todo
    :pysig: e9ae30baf9b69b0f67363d96a2224955
    :realsig: (QByteArrayView)
    :digest: b14b2de6a24e61803db67ef9bf40c2e3

Tries to determine the encoding of the HTML in *data* by looking at leading byte order marks or a charset specifier in the HTML meta tag and returns a :sip:ref:`~PyQt6.QtCore.QStringDecoder` matching the encoding. If the returned decoder is not valid, the encoding specified is not supported by :sip:ref:`~PyQt6.QtCore.QStringConverter`. If no encoding is detected, the method returns a decoder for Utf8.

.. seealso:: isValid().
