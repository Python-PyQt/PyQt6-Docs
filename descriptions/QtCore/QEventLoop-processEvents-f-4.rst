.. sip:method-description::
    :status: todo
    :pysig: f4226c2335d5dd6c62dcc81e0301854a
    :realsig: (QEventLoop::ProcessEventsFlags, QDeadlineTimer)
    :digest: 9e20e1ea0bb905ebfc93be938332f184

Process pending events that match *flags* until *deadline* has expired, or until there are no more events to process, whichever happens first. This function is especially useful if you have a long running operation and want to show its progress without allowing user input, i.e. by using the :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventFlags.ExcludeUserInputEvents` flag.

**Notes:**

* This function does not process events continuously; it returns after all available events are processed.

* Specifying the :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventFlags.WaitForMoreEvents` flag makes no sense and will be ignored.
