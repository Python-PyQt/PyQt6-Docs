.. sip:method-description::
    :status: todo
    :pysig: 6fc6797ffab361c7dfd3fc8df2a4bb8c
    :realsig: (QSocketNotifier::Type,QObject*)
    :digest: c7538dd1096f3401a8129975fbf3b76a

Constructs a socket notifier with the given *type* that has no descriptor assigned. The *parent* argument is passed to :sip:ref:`~PyQt6.QtCore.QObject`'s constructor.

Call the :sip:ref:`~PyQt6.QtCore.QSocketNotifier.setSocket` function to set the descriptor for monitoring.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSocketNotifier.setSocket`, :sip:ref:`~PyQt6.QtCore.QSocketNotifier.isValid`, :sip:ref:`~PyQt6.QtCore.QSocketNotifier.isEnabled`.
