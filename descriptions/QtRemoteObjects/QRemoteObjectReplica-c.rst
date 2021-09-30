.. sip:class-description::
    :status: todo
    :brief: A class interacting with (but not implementing) a Qt API on the Remote Object network
    :digest: c59292db480d3dc7ce7bc63f134ab781

A class interacting with (but not implementing) a Qt API on the Remote Object network.

A Remote Object Replica is a :sip:ref:`~PyQt6.QtCore.QObject` proxy for another :sip:ref:`~PyQt6.QtCore.QObject` (called the `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_ object). Once initialized, a replica can be considered a "latent copy" of the `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_ object. That is, every change to a Q_PROPERTY on the `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_, or signal emitted by the `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_ will be updated/emitted by all `Replica <https://doc.qt.io/qt-6/qtremoteobjects-replica.html#replica>`_ objects. Latency is introduced by process scheduling by any OSes involved and network communication latency. As long as the replica has been initialized and the communication is not disrupted, receipt and order of changes is guaranteed.

The :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectReplica.isInitialized` and :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectReplica.state` properties (and corresponding :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectReplica.initialized`/\ :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectReplica.stateChanged` signals) allow the state of a `Replica <https://doc.qt.io/qt-6/qtremoteobjects-replica.html#replica>`_ to be determined.

While Qt Remote Objects (QtRO) handles the initialization and synchronization of `Replica <https://doc.qt.io/qt-6/qtremoteobjects-replica.html#replica>`_ objects, there are numerous steps happening behind the scenes which can fail and that aren't encountered in single process Qt applications. See `Troubleshooting <https://doc.qt.io/qt-6/qtremoteobjects-troubleshooting.html#troubleshooting>`_ for advice on how to handle such issues when using a remote objects network.
