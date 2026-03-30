.. sip:method-description::
    :status: todo
    :pysig: 252f2463b17d7b65060495677c920d4c
    :realsig: (const QStringList&)
    :digest: 2e9dcab6a43d899815afebd1d931b3d2

Sets *paths* as the list of directories where the engine searches for installed modules in a URL-based directory structure.

By default, this list contains the paths mentioned in `QML Import Path <https://doc.qt.io/qt-6/qtqml-syntax-imports.html#qml-import-path>`_.

**Warning:** Calling setImportPathList does not preserve the default import paths.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.importPathList`, :sip:ref:`~PyQt6.QtQml.QQmlEngine.addImportPath`.
