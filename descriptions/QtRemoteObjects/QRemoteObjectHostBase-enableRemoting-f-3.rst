.. sip:method-description::
    :status: todo
    :pysig: 563517837fb263445e8fcb88939af548
    :realsig: (QAbstractItemModel*, const QString&, const QList<int>, QItemSelectionModel*)
    :digest: a960ae1a650ec790f571de3b5a8689a1

This overload of :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHostBase.enableRemoting` is specific to :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` types (or any type derived from :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`). This is useful if you want to have a model and the HMI for the model in different processes.

The three required parameters are the *model* itself, the *name* by which to lookup the model, and the *roles* that should be exposed on the Replica side. If you want to synchronize selection between `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_ and `Replica <https://doc.qt.io/qt-6/qtremoteobjects-replica.html#replica>`_, the optional *selectionModel* parameter can be used. This is only recommended when using a single Replica.

Behind the scenes, Qt Remote Objects batches data() lookups and prefetches data when possible to make the model interaction as responsive as possible.

Returns ``false`` if the current node is a client node, or if the :sip:ref:`~PyQt6.QtCore.QObject` is already registered to be remoted, and ``true`` if remoting is successfully enabled for the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHostBase.disableRemoting`.
