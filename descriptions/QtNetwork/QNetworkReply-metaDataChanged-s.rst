.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 188c51c30deab16d9e557da01d8be182

This signal is emitted whenever the metadata in this reply changes. metadata is any information that is not the content (data) itself, including the network headers. In the majority of cases, the metadata will be known fully by the time the first byte of data is received. However, it is possible to receive updates of headers or other metadata during the processing of the data.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.header`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.rawHeaderList`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.rawHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.hasRawHeader`.
