.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 38dd0bc36a536068544602e99bf13100

If *enable* is true, the notifier is enabled; otherwise the notifier is disabled.

When the notifier is enabled, it emits the :sip:ref:`~PyQt6.QtCore.QSocketNotifier.activated` signal whenever a socket event corresponding to its :sip:ref:`~PyQt6.QtCore.QSocketNotifier.type` occurs. When it is disabled, it ignores socket events (the same effect as not creating the socket notifier).

Write notifiers should normally be disabled immediately after the :sip:ref:`~PyQt6.QtCore.QSocketNotifier.activated` signal has been emitted

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSocketNotifier.isEnabled`, :sip:ref:`~PyQt6.QtCore.QSocketNotifier.activated`.
