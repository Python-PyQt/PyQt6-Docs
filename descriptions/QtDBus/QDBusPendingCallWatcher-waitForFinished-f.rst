.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: fcb7e6d96c1350fe4c425cfd5fb57905

Suspends the execution of the calling thread until the reply is received and processed. After this function returns, :sip:ref:`~PyQt6.QtDBus.QDBusPendingCallWatcher.isFinished` should return true, indicating the reply's contents are ready to be processed.

.. seealso:: QDBusPendingReply::waitForFinished().
