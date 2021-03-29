.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: c679a39f2220c75fcde3eab14e9fef3c

This signal is emitted from the associated thread right before it finishes executing.

When this signal is emitted, the event loop has already stopped running. No more events will be processed in the thread, except for deferred deletion events. This signal can be connected to :sip:ref:`~PyQt6.QtCore.QObject.deleteLater`, to free objects in that thread.

**Note:** If the associated thread was terminated using :sip:ref:`~PyQt6.QtCore.QThread.terminate`, it is undefined from which thread this signal is emitted.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.started`.
