.. sip:method-description::
    :status: todo
    :pysig: d466f51a668524e02b230ae13166aabe
    :realsig: (QEventLoop::ProcessEventsFlags,int)
    :digest: 08b6b347dda152fe7826e2586c233f99

Process pending events that match *flags* for a maximum of *maxTime* milliseconds, or until there are no more events to process, whichever is shorter.

Equivalent to calling:

::

    processEvents(flags, QDeadlineTimer(maxTime));
