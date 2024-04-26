.. sip:method-description::
    :status: todo
    :pysig: d16f54dd241f1011d61fddb403fcd41f
    :realsig: (QEventLoop::ProcessEventsFlags,int)
    :digest: f206c99837f4c18632e6137dee4c51ac

This is an overloaded function.

Processes pending events for the calling thread for *ms* milliseconds or until there are no more events to process, whichever is shorter.

This is equivalent to calling:

::

    QCoreApplication::processEvents(flags, QDeadlineTimer(ms));
