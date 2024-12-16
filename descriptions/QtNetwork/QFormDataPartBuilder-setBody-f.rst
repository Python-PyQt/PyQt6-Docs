.. sip:method-description::
    :status: todo
    :pysig: 9d96cc370951dd82c66fcbe6ef1527ad
    :realsig: (QByteArrayView, QAnyStringView, QAnyStringView)
    :digest: 46478113033f7a26645ccf314631d0a9

Sets *data* as the body of this MIME part and, if given, *fileName* as the file name parameter in the content disposition header.

If *mimeType* is not given (is empty), then :sip:ref:`~PyQt6.QtNetwork.QFormDataPartBuilder` tries to auto-detect the mime-type of *data* using :sip:ref:`~PyQt6.QtCore.QMimeDatabase`.

A subsequent call to :sip:ref:`~PyQt6.QtNetwork.QFormDataPartBuilder.setBodyDevice` discards the body and the device will be used instead.

For a large amount of data (e.g. an image), :sip:ref:`~PyQt6.QtNetwork.QFormDataPartBuilder.setBodyDevice` is preferred, which will not copy the data internally.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QFormDataPartBuilder.setBodyDevice`.
