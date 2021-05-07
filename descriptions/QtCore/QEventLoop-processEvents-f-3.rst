.. sip:method-description::
    :status: todo
    :pysig: d466f51a668524e02b230ae13166aabe
    :realsig: (QEventLoop::ProcessEventsFlags,int)
    :digest: 9db4c94524fef74b482a15f07756e64a

Process pending events that match *flags* for a maximum of *maxTime* milliseconds, or until there are no more events to process, whichever is shorter. This function is especially useful if you have a long running operation and want to show its progress without allowing user input, i.e. by using the :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventFlags.ExcludeUserInputEvents` flag.

**Notes:**

* This function does not process events continuously; it returns after all available events are processed.

* Specifying the :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventFlags.WaitForMoreEvents` flag makes no sense and will be ignored.
