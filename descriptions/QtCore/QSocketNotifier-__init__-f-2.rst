.. sip:method-description::
    :status: todo
    :pysig: 3d90f42c8ebcbc381d1a9103d26cfba7
    :realsig: (qintptr,QSocketNotifier::Type,QObject*)
    :digest: 6ae0ff52ba431da1dc83cfb7f534a4ff

Constructs a socket notifier with the given *parent*. It enables the *socket*, and watches for events of the given *type*.

It is generally advisable to explicitly enable or disable the socket notifier, especially for write notifiers.

**Note for Windows users:** The socket passed to :sip:ref:`~PyQt6.QtCore.QSocketNotifier` will become non-blocking, even if it was created as a blocking socket.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSocketNotifier.setEnabled`, :sip:ref:`~PyQt6.QtCore.QSocketNotifier.isEnabled`.
