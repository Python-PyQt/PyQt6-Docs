.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ed5ba767f9ed49a451ab331ecd11c855

Returns ``true`` if the pending call has finished processing and the reply has been received.

Note that this function only changes state if you call :sip:ref:`~PyQt6.QtDBus.QDBusPendingCallWatcher.waitForFinished` or if an external D-Bus event happens, which in general only happens if you return to the event loop execution.

.. seealso:: QDBusPendingReply::isFinished().
