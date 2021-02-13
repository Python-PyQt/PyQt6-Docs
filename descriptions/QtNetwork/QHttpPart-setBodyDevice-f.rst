.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: (QIODevice*)
    :digest: 496b330df6cab2f2de0be1d5ffb3db02

Sets the device to read the content from to *device*. For large amounts of data this method should be preferred over :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setBody`, because the content is not copied when using this method, but read directly from the device. *device* must be open and readable. :sip:ref:`~PyQt6.QtNetwork.QHttpPart` does not take ownership of *device*, i.e. the device must be closed and destroyed if necessary. if *device* is sequential (e.g. sockets, but not files), :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post` should be called after *device* has emitted finished(). For unsetting the device and using data set via :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setBody`, use "(0)".

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setBody`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post`.
