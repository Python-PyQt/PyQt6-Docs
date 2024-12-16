.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: efceb7cabc64ada3f634ae52ad707dc3

Returns the timeout used for transfers, in milliseconds.

If transferTimeoutAsDuration().count() cannot be represented in ``int``, this function returns ``INT_MAX``/``INT_MIN`` instead.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setTransferTimeout`, transferTimeoutAsDuration().
