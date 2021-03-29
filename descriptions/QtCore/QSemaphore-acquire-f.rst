.. sip:method-description::
    :status: todo
    :pysig: cd756c5b6e9231f18958d85978fd7238
    :realsig: (int)
    :digest: 41e38b16a90fd8f44fb7015c6d407ead

Tries to acquire ``n`` resources guarded by the semaphore. If *n* > :sip:ref:`~PyQt6.QtCore.QSemaphore.available`, this call will block until enough resources are available.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSemaphore.release`, :sip:ref:`~PyQt6.QtCore.QSemaphore.available`, :sip:ref:`~PyQt6.QtCore.QSemaphore.tryAcquire`.
