.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 682cc82ca4e6f06173e8af1f2436bfd5

Temporarily restores the :sip:ref:`~PyQt6.QtCore.QObject.signalsBlocked` state to what it was before this :sip:ref:`~PyQt6.QtCore.QSignalBlocker`'s constructor ran. To undo, use :sip:ref:`~PyQt6.QtCore.QSignalBlocker.reblock`.

The numbers of :sip:ref:`~PyQt6.QtCore.QSignalBlocker.reblock` and  calls are not counted, so every  undoes any number of :sip:ref:`~PyQt6.QtCore.QSignalBlocker.reblock` calls.
