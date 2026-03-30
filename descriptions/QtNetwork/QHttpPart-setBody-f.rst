.. sip:method-description::
    :status: todo
    :pysig: c70916e782d9742b90f37ccdedc4f900
    :realsig: (const QByteArray&)
    :digest: 69d7b6e225a9f6a15e2d6b37754b8d85

Sets the body of this MIME part to *body*. The body set with this method will be used unless the device is set via :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setBodyDevice`. For a large amount of data (e.g. an image), use :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setBodyDevice`, which will not copy the data internally.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setBodyDevice`.
