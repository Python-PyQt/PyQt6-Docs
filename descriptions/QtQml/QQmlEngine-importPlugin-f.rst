.. sip:method-description::
    :status: todo
    :pysig: 39741433306dcb868b97dd017ad57e3b
    :realsig: (const QString&,const QString&,QList<QQmlError>*)
    :digest: 22d095b8cac6db122d44576940358466

Imports the plugin named *filePath* with the *uri* provided. Returns true if the plugin was successfully imported; otherwise returns false.

On failure and if non-null, the *errors* list will have any errors which occurred prepended to it.

The plugin has to be a Qt plugin which implements the :sip:ref:`~PyQt6.QtQml.QQmlEngineExtensionPlugin` interface.
