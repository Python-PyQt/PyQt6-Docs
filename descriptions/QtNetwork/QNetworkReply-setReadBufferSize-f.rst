.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qint64)
    :digest: 3deb2de4e4dbc83afe47c43f1b120676

Sets the size of the read buffer to be *size* bytes. The read buffer is the buffer that holds data that is being downloaded off the network, before it is read with :sip:ref:`~PyQt6.QtCore.QIODevice.read`. Setting the buffer size to 0 will make the buffer unlimited in size.

:sip:ref:`~PyQt6.QtNetwork.QNetworkReply` will try to stop reading from the network once this buffer is full (i.e., bytesAvailable() returns *size* or more), thus causing the download to throttle down as well. If the buffer is not limited in size, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` will try to download as fast as possible from the network.

Unlike :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setReadBufferSize`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` cannot guarantee precision in the read buffer size. That is, bytesAvailable() can return more than *size*.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.readBufferSize`.
