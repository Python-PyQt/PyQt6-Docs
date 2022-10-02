.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: c3507abfe4d767dceb271be720432bfa

Re-blocks signals after a previous :sip:ref:`~PyQt6.QtCore.QSignalBlocker.unblock`.

The numbers of reblock() and :sip:ref:`~PyQt6.QtCore.QSignalBlocker.unblock` calls are not counted, so every reblock() undoes any number of :sip:ref:`~PyQt6.QtCore.QSignalBlocker.unblock` calls.
