.. sip:method-description::
    :status: todo
    :pysig: 8aa4db8179170d37e11ad02ad96f4d34
    :realsig: (const QStringList&)
    :digest: b623777d7c3061b464ad0d3beadee18b

Sets *paths* as the list of directories where the engine searches for installed modules in a URL-based directory structure.

By default, the list contains the directory of the application executable, paths specified in the ``QML_IMPORT_PATH`` environment variable, and the builtin ``QmlImportsPath`` from :sip:ref:`~PyQt6.QtCore.QLibraryInfo`.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.importPathList`, :sip:ref:`~PyQt6.QtQml.QQmlEngine.addImportPath`.
