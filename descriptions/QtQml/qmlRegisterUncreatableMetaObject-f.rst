.. sip:method-description::
    :status: todo
    :pysig: 18f8857ba1fc5cd935788582a9501adf
    :realsig: (const QMetaObject&,const char*,int,int,const char*,const QString&)
    :digest: 4270f8dff9b324bb7c28c703d40241d2

This function registers the *staticMetaObject* and its extension in the QML system with the name *qmlName* in the library imported from *uri* having version number composed from *versionMajor* and *versionMinor*.

An instance of the meta object cannot be created. An error message with the given *reason* is printed if the user attempts to create it.

This function is useful for registering Q_NAMESPACE namespaces.

Returns the QML type id.

For example:

::

    namespace MyNamespace {
      Q_NAMESPACE
      enum MyEnum {
          Key1,
          Key2,
      };
      Q_ENUMS(MyEnum)
    }

    //...
    qmlRegisterUncreatableMetaObject(MyNamespace::staticMetaObject, "io.qt", 1, 0, "MyNamespace", "Access to enums & flags only");

On the QML side, you can now use the registered enums:

::

    Component.onCompleted: console.log(MyNamespace.Key2)

.. seealso:: QML_ELEMENT, QML_NAMED_ELEMENT(), QML_UNCREATABLE().
