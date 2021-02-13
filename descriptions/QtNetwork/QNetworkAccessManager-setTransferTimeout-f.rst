.. sip:method-description::
    :status: todo
    :pysig: e25cdc302512fdfafa8fa76909001fbe
    :realsig: (int)
    :digest: c1ef93c86296adc30b252912dd186541

Sets *timeout* as the transfer timeout in milliseconds.

Transfers are aborted if no bytes are transferred before the timeout expires. Zero means no timer is set. If no argument is provided, the timeout is :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.TransferTimeoutConstant.DefaultTransferTimeoutConstant`. If this function is not called, the timeout is disabled and has the value zero. The request-specific non-zero timeouts set for the requests that are executed override this value. This means that if :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` has an enabled timeout, it needs to be disabled to execute a request without a timeout.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.transferTimeout`.
