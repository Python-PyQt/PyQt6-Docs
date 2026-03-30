.. sip:method-description::
    :status: todo
    :pysig: 252f2463b17d7b65060495677c920d4c
    :realsig: (const QStringList&)
    :digest: ca3ac863d4133493832da31ff191f4f1

Sets the list of D-Bus services being watched to be *services*.

Note that setting the entire list means removing all previous rules for watching services and adding new ones. This is an expensive operation and should be avoided, if possible. Instead, use :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.addWatchedService` and :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.removeWatchedService` if you can to manipulate entries in the list.

Removes any existing binding of :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.watchedServices`.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.watchedServices`.
