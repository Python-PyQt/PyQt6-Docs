.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 69c9f79b2a876b5d4012b432f2d1185a

Schedules this object for deletion.

The object will be deleted when control returns to the event loop. If the event loop is not running when this function is called (e.g. deleteLater() is called on an object before :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`), the object will be deleted once the event loop is started. If deleteLater() is called after the main event loop has stopped, the object will not be deleted. If deleteLater() is called on an object that lives in a thread with no running event loop, the object will be destroyed when the thread finishes.

Note that entering and leaving a new event loop (e.g., by opening a modal dialog) will *not* perform the deferred deletion; for the object to be deleted, the control must return to the event loop from which deleteLater() was called. This does not apply to objects deleted while a previous, nested event loop was still running: the Qt event loop will delete those objects as soon as the new nested event loop starts.

In situations where Qt is not driving the event dispatcher via e.g. :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec` or :sip:ref:`~PyQt6.QtCore.QEventLoop.exec`, deferred deletes will not be processed automatically. To ensure deferred deletion in this scenario, the following workaround can be used:

::

    const auto *eventDispatcher = QThread::currentThread()->eventDispatcher();
    QObject::connect(eventDispatcher, &QAbstractEventDispatcher::aboutToBlock,
        QThread::currentThread(), []{
            if (QThread::currentThread()->loopLevel() == 0)
                QCoreApplication::sendPostedEvents(nullptr, QEvent::DeferredDelete);
        }
    );

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.destroyed`, QPointer.
