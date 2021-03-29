.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 99f5ffa73810b93e962d2ced01b19164

Returns the timeout used for transfers, in milliseconds.

This timeout is zero if :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setTransferTimeout` hasn't been called, which means that the timeout is not used.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setTransferTimeout`.
