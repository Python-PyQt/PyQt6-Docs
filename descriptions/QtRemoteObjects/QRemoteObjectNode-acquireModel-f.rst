.. sip:method-description::
    :status: todo
    :pysig: ad56d92d22342c4bdcaddf8207cf990d
    :realsig: (const QString&,QtRemoteObjects::InitialAction,const QList<int>&)
    :digest: 3c979a30fa4eee377a9387f45379fb1b

Returns a pointer to a `Replica <https://doc.qt.io/qt-6/qtremoteobjects-replica.html#replica>`_ which is specifically derived from :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`. The *name* provided must match the name used with the matching :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHostBase.enableRemoting` that put the `Model <https://doc.qt.io/qt-6/qtremoteobjects-repc.html#model>`_ on the network. *action* specifies whether the model should fetch data before the :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectReplica.initialized` signal is emitted. If it's set to :sip:ref:`~PyQt6.QtRemoteObjects.QtRemoteObjects.InitialAction.PrefetchData`, then the data for roles in the *rolesHint* will be prefetched. If *rolesHint* is empty, then the data for all the roles exposed by `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_ will be prefetched.

The returned model will be empty until it is initialized with the `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_.
