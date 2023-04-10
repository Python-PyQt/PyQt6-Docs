.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: 9583462d395132e715b8268d48c4757d

Returns the list of directories where the engine searches for installed modules in a URL-based directory structure.

For example, if ``/opt/MyApp/lib/imports`` is in the path, then QML that imports ``com.mycompany.Feature`` will cause the :sip:ref:`~PyQt6.QtQml.QQmlEngine` to look in ``/opt/MyApp/lib/imports/com/mycompany/Feature/`` for the components provided by that module. A ``qmldir`` file is required for defining the type version mapping and possibly QML extensions plugins.

By default, this list contains the paths mentioned in `QML Import Path <https://doc.qt.io/qt-6/qtqml-syntax-imports.html#qml-import-path>`_.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.addImportPath`, :sip:ref:`~PyQt6.QtQml.QQmlEngine.setImportPathList`.
