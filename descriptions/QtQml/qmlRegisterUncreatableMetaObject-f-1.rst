.. sip:method-description::
    :status: todo
    :pysig: 836fd3e43aa19699886a16de48867f27
    :realsig: (const QMetaObject&, const char*, int, int, const char*, const QString&)
    :digest: cfba071e7dc8d3e417caecd6af5fe061

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
      Q_ENUM(MyEnum)
    }

    //...
    qmlRegisterUncreatableMetaObject(MyNamespace::staticMetaObject, "io.qt", 1, 0, "MyNamespace", "Access to enums & flags only");

On the QML side, you can now use the registered enums:

::

    Component.onCompleted: console.log(MyNamespace.Key2)

.. seealso:: QML_ELEMENT, QML_NAMED_ELEMENT(), QML_UNCREATABLE().
