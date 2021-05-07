.. sip:method-description::
    :status: todo
    :pysig: 4f836b25f24af9a183a3f4127fcd4041
    :realsig: (QEventLoop::ProcessEventsFlags)
    :digest: c0252999ba3317e3e71b635319881208

Processes some pending events that match *flags*. Returns ``true`` if pending events were handled; otherwise returns ``false``.

This function is especially useful if you have a long running operation and want to show its progress without allowing user input; i.e. by using the :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventFlags.ExcludeUserInputEvents` flag.

This function is simply a wrapper for :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher.processEvents`. See the documentation for that function for details.
