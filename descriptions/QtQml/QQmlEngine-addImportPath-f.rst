.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 0aae42f9c0e0a853e11bd89d2bb4ef17

Adds *path* as a directory where the engine searches for installed modules in a URL-based directory structure.

The *path* may be a local filesystem directory, a `Qt Resource <https://doc.qt.io/qt-6/resources.html>`_ path (``:/imports``), a `Qt Resource <https://doc.qt.io/qt-6/resources.html>`_ url (``qrc:/imports``) or a URL.

The *path* will be converted into canonical form before it is added to the import path list.

The newly added *path* will be first in the :sip:ref:`~PyQt6.QtQml.QQmlEngine.importPathList`.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.setImportPathList`, `QML Modules <https://doc.qt.io/qt-6/qtqml-modules-topic.html>`_, `QML Import Path <https://doc.qt.io/qt-6/qtqml-syntax-imports.html#qml-import-path>`_.
