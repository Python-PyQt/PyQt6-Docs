.. sip:method-description::
    :status: todo
    :pysig: ad86875787d0b01fe455ac340209c013
    :realsig: (QThread::QualityOfService)
    :digest: 7416aff5f892a1871484b9e27e745707

Set the Quality of Service level of the thread object to *serviceLevel*. This can only be called from the thread itself or before the thread is started!

This is currently only implemented on Apple platforms, and Windows. The function call will complete successfully on other platforms but will not currently have any effect.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.serviceLevel`, :sip:ref:`~PyQt6.QtCore.QThreadPool.setServiceLevel`.
