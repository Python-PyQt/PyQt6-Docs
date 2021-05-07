.. sip:method-description::
    :status: todo
    :pysig: af55b61bcb6b72b7c4013fab425e1775
    :realsig: (const QString&,const QDBusConnection&,QDBusServiceWatcher::WatchMode,QObject*)
    :digest: 81719c2e8e073147779a0099fc58fbe1

Creates a :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher` object and attaches it to the *connection* connection. Also, this function immediately starts watching for *watchMode* changes to service *service*.

The *parent* parameter is passed to :sip:ref:`~PyQt6.QtCore.QObject` to set the parent of this object.
