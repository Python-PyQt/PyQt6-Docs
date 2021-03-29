.. sip:method-description::
    :status: todo
    :pysig: f6a258d8f3ee5206d682d799316314b1
    :realsig: (bool)
    :digest: bd2a9be851271345b0ddee12715c72f4

If *block* is true, signals emitted by this object are blocked (i.e., emitting a signal will not invoke anything connected to it). If *block* is false, no such blocking will occur.

The return value is the previous value of :sip:ref:`~PyQt6.QtCore.QObject.signalsBlocked`.

Note that the :sip:ref:`~PyQt6.QtCore.QObject.destroyed` signal will be emitted even if the signals for this object have been blocked.

Signals emitted while being blocked are not buffered.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.signalsBlocked`, :sip:ref:`~PyQt6.QtCore.QSignalBlocker`.
