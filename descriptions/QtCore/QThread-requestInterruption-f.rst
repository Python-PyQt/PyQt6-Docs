.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 27af261cc75370623e0fbe778aee3184

Request the interruption of the thread. That request is advisory and it is up to code running on the thread to decide if and how it should act upon such request. This function does not stop any event loop running on the thread and does not terminate it in any way.

This function has no effect on the main thread, and does nothing if the thread is not currently running.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.isInterruptionRequested`.
