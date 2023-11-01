.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: b298194b6547e325337c26e42c77daca

Adds *path* as a directory where the engine searches for installed modules in a URL-based directory structure.

The *path* may be a local filesystem directory, a `Qt Resource <https://doc.qt.io/qt-6/resources.html>`_ path (``:/imports``), a `Qt Resource <https://doc.qt.io/qt-6/resources.html>`_ url (``qrc:/imports``) or a URL.

The *path* will be converted into canonical form before it is added to the import path list.

The newly added *path* will be first in the :sip:ref:`~PyQt6.QtQml.QQmlEngine.importPathList`.

**See also** :sip:ref:`~PyQt6.QtQml.QQmlEngine.setImportPathList`, `QML Modules <https://doc.qt.io/qt-6/qtqml-modules-topic.html>`_, and `QML Import Path <https://doc.qt.io/qt-6/qtqml-syntax-imports.html#qml-import-path>`_
