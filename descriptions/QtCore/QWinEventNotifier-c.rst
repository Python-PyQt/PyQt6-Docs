.. sip:class-description::
    :status: todo
    :brief: Support for the Windows Wait functions
    :digest: f0ffbe35e6f27981cdff38871405d719

The :sip:ref:`~PyQt6.QtCore.QWinEventNotifier` class provides support for the Windows Wait functions.

The :sip:ref:`~PyQt6.QtCore.QWinEventNotifier` class makes it possible to use the wait functions on windows in a asynchronous manner. With this class, you can register a HANDLE to an event and get notification when that event becomes signalled. The state of the event is not modified in the process so if it is a manual reset event you will need to reset it after the notification.

Once you have created a event object using Windows API such as CreateEvent() or OpenEvent(), you can create an event notifier to monitor the event handle. If the event notifier is enabled, it will emit the :sip:ref:`~PyQt6.QtCore.QWinEventNotifier.activated` signal whenever the corresponding event object is signalled.

The :sip:ref:`~PyQt6.QtCore.QWinEventNotifier.setEnabled` function allows you to disable as well as enable the event notifier. It is generally advisable to explicitly enable or disable the event notifier. A disabled notifier does nothing when the event object is signalled (the same effect as not creating the event notifier). Use the :sip:ref:`~PyQt6.QtCore.QWinEventNotifier.isEnabled` function to determine the notifier's current status.

Finally, you can use the :sip:ref:`~PyQt6.QtCore.QWinEventNotifier.setHandle` function to register a new event object, and the :sip:ref:`~PyQt6.QtCore.QWinEventNotifier.handle` function to retrieve the event handle.

**Further information:** Although the class is called :sip:ref:`~PyQt6.QtCore.QWinEventNotifier`, it can be used for certain other objects which are so-called synchronization objects, such as Processes, Threads, Waitable timers.

**Warning:** This class is only available on Windows.
