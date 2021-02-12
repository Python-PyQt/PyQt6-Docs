.. sip:method-description::
    :status: todo
    :pysig: a4410654dfc0edb07ecfc603ca354378
    :realsig: (QObject*,int)
    :digest: db16f368fa4f14733e6a50f88a0c09d7

Immediately dispatches all events which have been previously queued with :sip:ref:`~PyQt6.QtCore.QCoreApplication.postEvent` and which are for the object *receiver* and have the event type *event_type*.

Events from the window system are *not* dispatched by this function, but by :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents`.

If *receiver* is ``nullptr``, the events of *event_type* are sent for all objects. If *event_type* is 0, all the events are sent for *receiver*.

**Note:** This method must be called from the thread in which its :sip:ref:`~PyQt6.QtCore.QObject` parameter, *receiver*, lives.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.postEvent`.
