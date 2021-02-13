.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: f8c1105d1f2d865ad806a929d1d2293d

Returns the timeout used for transfers, in milliseconds.

This timeout is zero if :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.setTransferTimeout` hasn't been called, which means that the timeout is not used.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.setTransferTimeout`.
