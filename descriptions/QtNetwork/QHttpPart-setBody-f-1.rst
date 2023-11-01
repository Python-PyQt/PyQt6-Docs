.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (const QByteArray&)
    :digest: 69d7b6e225a9f6a15e2d6b37754b8d85

Sets the body of this MIME part to *body*. The body set with this method will be used unless the device is set via :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setBodyDevice`. For a large amount of data (e.g. an image), use :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setBodyDevice`, which will not copy the data internally.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setBodyDevice`.
