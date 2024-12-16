.. sip:method-description::
    :status: todo
    :pysig: dde0551ebc46544686c58ec6c6e2df57
    :realsig: (QIODevice*, QAnyStringView, QAnyStringView)
    :digest: 4cc668d5803d80bb4cf35a5ecc6ab4d2

Sets *body* as the body device of this part and *fileName* as the file name parameter in the content disposition header.

If *mimeType* is not given (is empty), then :sip:ref:`~PyQt6.QtNetwork.QFormDataPartBuilder` tries to auto-detect the mime-type of *body* using :sip:ref:`~PyQt6.QtCore.QMimeDatabase`.

A subsequent call to :sip:ref:`~PyQt6.QtNetwork.QFormDataPartBuilder.setBody` discards the body device and the data set by :sip:ref:`~PyQt6.QtNetwork.QFormDataPartBuilder.setBody` will be used instead.

For large amounts of data this method should be preferred over :sip:ref:`~PyQt6.QtNetwork.QFormDataPartBuilder.setBody`, because the content is not copied when using this method, but read directly from the device.

*body* must be open and readable. :sip:ref:`~PyQt6.QtNetwork.QFormDataPartBuilder` does not take ownership of *body*, i.e. the device must be closed and destroyed if necessary.

**Note:** If *body* is sequential (e.g. sockets, but not files), :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post` should be called after *body* has emitted finished().

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QFormDataPartBuilder.setBody`, :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setBodyDevice`.
