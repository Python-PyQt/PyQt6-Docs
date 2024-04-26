.. sip:method-description::
    :status: todo
    :pysig: c6348efafc76172751eb50bb18df284b
    :realsig: (QEventLoop::ProcessEventsFlags,int)
    :digest: a1c0228c1e212bea15906f30990fd886

This is an overloaded function.

Process pending events that match *flags* for a maximum of *maxTime* milliseconds, or until there are no more events to process, whichever is shorter.

Equivalent to calling:

::

    processEvents(flags, QDeadlineTimer(maxTime));
