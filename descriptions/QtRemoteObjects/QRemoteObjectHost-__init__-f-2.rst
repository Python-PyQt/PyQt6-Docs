.. sip:method-description::
    :status: todo
    :pysig: 82620dc11d2cca994cf6e12cc4c7c35a
    :realsig: (const QUrl&,const QUrl&,QRemoteObjectHostBase::AllowedSchemas,QObject*)
    :digest: e76a6ae8923352e2a3243ffe8aebf290

Constructs a new :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost` Node (i.e., a Node that supports exposing `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_ objects on the QtRO network) with address *address*. If set, *registryAddress* will be used to connect to the :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistry` at the provided address. The *allowedSchemas* parameter is only needed (and should be set to :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas.AllowExternalRegistration`) if the schema of the url should be used as an `External Schema <https://doc.qt.io/qt-6/qtremoteobjects-external-schemas.html#external-schemas>`_ by the registry.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost.setHostUrl`, setRegistryUrl().
