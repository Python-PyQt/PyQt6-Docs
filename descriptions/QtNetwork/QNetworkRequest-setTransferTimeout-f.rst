.. sip:method-description::
    :status: todo
    :pysig: e25cdc302512fdfafa8fa76909001fbe
    :realsig: (int)
    :digest: a360cd7f4a5ee16278c9bb2af02fbb02

Sets *timeout* as the transfer timeout in milliseconds.

Transfers are aborted if no bytes are transferred before the timeout expires. Zero means no timer is set. If no argument is provided, the timeout is :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.TransferTimeoutConstant.DefaultTransferTimeoutConstant`. If this function is not called, the timeout is disabled and has the value zero.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.transferTimeout`.
