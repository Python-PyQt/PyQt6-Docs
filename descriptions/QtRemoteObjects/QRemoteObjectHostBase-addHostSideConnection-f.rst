.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: (QIODevice*)
    :digest: 92003175113b4707d43d24d212e1a06d

In order to QRemoteObjectHost::enableRemoting() `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_ objects over `External QIODevices <https://doc.qt.io/qt-6/qtremoteobjects-external-schemas.html#external-qiodevices>`_, Qt Remote Objects needs access to the communications channel (a :sip:ref:`~PyQt6.QtCore.QIODevice`) between the respective nodes. It is the  call that enables this on the `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_ side, taking the *ioDevice* as input. Any :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHostBase.enableRemoting` call will still work without calling , but the Node will not be able to share the `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_ objects without being provided the connection to the Replica node. Before calling this function you must call :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost.setHostUrl`\ () with a unique URL and :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas.AllowExternalRegistration`.

.. seealso:: addClientSideConnection.
