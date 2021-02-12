.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 5aa59713ad647b52c71850bb750e4392

To avoid unintended truncation of the descriptor, use the QSocketDescriptor overload of this function. If you need compatibility with versions older than 5.15 you need to change the slot to accept qintptr if it currently accepts an int, and then connect using Functor-Based Connection.

This signal is emitted whenever the socket notifier is enabled and a socket event corresponding to its :sip:ref:`~PyQt6.QtCore.QSocketNotifier.Type.Type` occurs.

The socket identifier is passed in the *socket* parameter.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSocketNotifier.type`, :sip:ref:`~PyQt6.QtCore.QSocketNotifier.socket`.
