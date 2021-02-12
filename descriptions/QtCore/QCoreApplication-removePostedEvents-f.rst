.. sip:method-description::
    :status: todo
    :pysig: 2b1fdb440ecd0b11815e3e37426a9560
    :realsig: (QObject*,int)
    :digest: 8529ce71a3f55a64f5b0700e30ea601b

Removes all events of the given *eventType* that were posted using :sip:ref:`~PyQt6.QtCore.QCoreApplication.postEvent` for *receiver*.

The events are *not* dispatched, instead they are removed from the queue. You should never need to call this function. If you do call it, be aware that killing events may cause *receiver* to break one or more invariants.

If *receiver* is ``nullptr``, the events of *eventType* are removed for all objects. If *eventType* is 0, all the events are removed for *receiver*. You should never call this function with *eventType* of 0.
