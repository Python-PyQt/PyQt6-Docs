.. sip:method-description::
    :status: todo
    :pysig: 8575cd542b930d3f2086c7593d54cd6a
    :realsig: (QEventLoop::ProcessEventsFlags,int)
    :digest: f206c99837f4c18632e6137dee4c51ac

This is an overloaded function.

Processes pending events for the calling thread for *ms* milliseconds or until there are no more events to process, whichever is shorter.

This is equivalent to calling:

::

    QCoreApplication::processEvents(flags, QDeadlineTimer(ms));
