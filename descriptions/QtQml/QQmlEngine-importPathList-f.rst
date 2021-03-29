.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: 947bd5bf0282e67d991d62b729372a54

Returns the list of directories where the engine searches for installed modules in a URL-based directory structure.

For example, if ``/opt/MyApp/lib/imports`` is in the path, then QML that imports ``com.mycompany.Feature`` will cause the :sip:ref:`~PyQt6.QtQml.QQmlEngine` to look in ``/opt/MyApp/lib/imports/com/mycompany/Feature/`` for the components provided by that module. A ``qmldir`` file is required for defining the type version mapping and possibly QML extensions plugins.

By default, the list contains the directory of the application executable, paths specified in the ``QML2_IMPORT_PATH`` environment variable, and the builtin ``Qml2ImportsPath`` from :sip:ref:`~PyQt6.QtCore.QLibraryInfo`.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.addImportPath`, :sip:ref:`~PyQt6.QtQml.QQmlEngine.setImportPathList`.
