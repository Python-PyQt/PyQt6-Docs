.. sip:method-description::
    :status: todo
    :pysig: 4a3930cd5a8b5ed17374fbe1e4f549aa
    :realsig: (const QUrl&,const char*,int,int,const char*)
    :digest: 58004975233342810694747d83505d40

This function may be used to register a singleton type with the name *qmlName*, in the library imported from *uri* having the version number composed from *versionMajor* and *versionMinor*. The type is defined by the QML file located at *url*. The url must be an absolute URL, i.e. url.isRelative() == false.

In addition the type's QML file must have pragma Singleton statement among its import statements.

A singleton type may be referenced via the type name with which it was registered, and this typename may be used as the target in a `Connections <https://doc.qt.io/qt-6/qml-qtqml-connections.html>`_ type or otherwise used as any other type id would. One exception to this is that a singleton type property may not be aliased (because the singleton type name does not identify an object within the same component as any other item).

Usage:

::

    // Second, register the QML singleton type by calling this function in an initialization function.
    qmlRegisterSingletonType(QUrl("file:///absolute/path/SingletonType.qml"), "Qt.example.qobjectSingleton", 1, 0, "RegisteredSingleton");

In order to use the registered singleton type in QML, you must import the singleton type.

It is also possible to have QML singleton types registered without using the :sip:ref:`~PyQt6.QtQml.qmlRegisterSingletonType` function. That can be done by adding a pragma Singleton statement among the imports of the type's QML file. In addition the type must be defined in a qmldir file with a singleton keyword and the qmldir must be imported by the QML files using the singleton.

.. seealso:: QML_SINGLETON.
