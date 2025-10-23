.. sip:method-description::
    :status: todo
    :pysig: 19cbc2f41cb574f33750d71cdb5c9930
    :realsig: (QObject*,QEvent*,int)
    :digest: 15dcbb76e0f3aac7d6d5ffa032709d2a

Adds the event *event*, with the object *receiver* as the receiver of the event, to an event queue and returns immediately.

The event must be allocated on the heap since the post event queue will take ownership of the event and delete it once it has been posted. It is *not safe* to access the event after it has been posted.

When control returns to the main event loop, all events that are stored in the queue will be sent using the :sip:ref:`~PyQt6.QtCore.QCoreApplication.notify` function.

Events are sorted in descending *priority* order, i.e. events with a high *priority* are queued before events with a lower *priority*. The *priority* can be any integer value, i.e. between INT_MAX and INT_MIN, inclusive; see :sip:ref:`~PyQt6.QtCore.Qt.EventPriority` for more details. Events with equal *priority* will be processed in the order posted.

**Note:** :sip:ref:`~PyQt6.QtCore.QObject.deleteLater` schedules the object for deferred deletion, which is typically handled by the receiver's event loop. If no event loop is running in the thread, the deletion will be performed when the thread finishes. A common and safe pattern is to connect the thread's finished() signal to the object's deleteLater() slot:

::

    QObject::connect(thread, &QThread::finished, worker, &QObject::deleteLater);

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.sendEvent`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.notify`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.sendPostedEvents`, :sip:ref:`~PyQt6.QtCore.Qt.EventPriority`.
