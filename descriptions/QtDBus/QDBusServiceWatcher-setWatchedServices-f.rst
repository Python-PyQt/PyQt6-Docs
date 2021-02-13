.. sip:method-description::
    :status: todo
    :pysig: 8aa4db8179170d37e11ad02ad96f4d34
    :realsig: (const QStringList&)
    :digest: 15aa847472d416b1518be1f5b75dda75

Sets the list of D-Bus services being watched to be *services*.

Note that setting the entire list means removing all previous rules for watching services and adding new ones. This is an expensive operation and should be avoided, if possible. Instead, use :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.addWatchedService` and :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.removeWatchedService` if you can to manipulate entries in the list.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.watchedServices`.
