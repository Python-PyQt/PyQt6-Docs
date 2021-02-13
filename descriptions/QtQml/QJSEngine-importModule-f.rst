.. sip:method-description::
    :status: todo
    :pysig: ee4163cc141154e5c0774a9f9c667938
    :realsig: (const QString&)
    :digest: dfe6e047f11b308d1073e43f058c5ff7

Imports the module located at *fileName* and returns a module namespace object that contains all exported variables, constants and functions as properties.

If this is the first time the module is imported in the engine, the file is loaded from the specified location in either the local file system or the Qt resource system and evaluated as an ECMAScript module. The file is expected to be encoded in UTF-8 text.

Subsequent imports of the same module will return the previously imported instance. Modules are singletons and remain around until the engine is destroyed.

The specified *fileName* will internally be normalized using :sip:ref:`~PyQt6.QtCore.QFileInfo.canonicalFilePath`. That means that multiple imports of the same file on disk using different relative paths will load the file only once.

**Note:** If an exception is thrown during the loading of the module, the return value will be the exception (typically an ``Error`` object; see :sip:ref:`~PyQt6.QtQml.QJSValue.isError`).
