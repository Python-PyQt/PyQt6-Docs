.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 175bd16bee6a7a376d64ba0bd5a272a9

Schedules this object for deletion.

The object will be deleted when control returns to the event loop. If the event loop is not running when this function is called (e.g.  is called on an object before :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`), the object will be deleted once the event loop is started. If  is called after the main event loop has stopped, the object will not be deleted. Since Qt 4.8, if  is called on an object that lives in a thread with no running event loop, the object will be destroyed when the thread finishes.

Note that entering and leaving a new event loop (e.g., by opening a modal dialog) will *not* perform the deferred deletion; for the object to be deleted, the control must return to the event loop from which  was called. This does not apply to objects deleted while a previous, nested event loop was still running: the Qt event loop will delete those objects as soon as the new nested event loop starts.

**Note:** It is safe to call this function more than once; when the first deferred deletion event is delivered, any pending events for the object are removed from the event queue.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.destroyed`, QPointer.
