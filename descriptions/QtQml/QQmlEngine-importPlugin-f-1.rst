.. sip:method-description::
    :status: todo
    :pysig: c4bb615629abc55efde4fb0c5f394936
    :realsig: (const QString&, const QString&, QList<QQmlError>*)
    :digest: 0c8635e0de31f62be6dc7e9573cf5e08

Import the module from QML with an "import" statement instead.

Imports the plugin named *filePath* with the *uri* provided. Returns true if the plugin was successfully imported; otherwise returns false.

On failure and if non-null, the *errors* list will have any errors which occurred prepended to it.

The plugin has to be a Qt plugin which implements the :sip:ref:`~PyQt6.QtQml.QQmlEngineExtensionPlugin` interface.

**Note:** Directly loading plugins like this can confuse the module import logic. In order to make the import logic load plugins from a specific place, you can use :sip:ref:`~PyQt6.QtQml.QQmlEngine.addPluginPath`. Each plugin should be part of a QML module that you can import using the "import" statement.
