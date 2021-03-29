.. sip:method-description::
    :status: todo
    :pysig: 023b630f6b768a3a3d5e9555b21b1001
    :realsig: (const char*,int,int,const char*)
    :digest: b0fbef52b04decfb8a489038cd8da5ff

Returns the QML type id of a type that was registered with the name *qmlName* in a particular *uri* and a version specified in *versionMajor* and *versionMinor*.

This function returns the same value as the QML type registration functions such as :sip:ref:`~PyQt6.QtQml.qmlRegisterType` and :sip:ref:`~PyQt6.QtQml.qmlRegisterSingletonType`.

If *qmlName*, *uri* and *versionMajor* match a registered type, but the specified minor version in *versionMinor* is higher, then the id of the type with the closest minor version is returned.

Returns -1 if no matching type was found or one of the given parameters was invalid.

.. seealso:: QML_ELEMENT, QML_NAMED_ELEMENT, QML_SINGLETON, :sip:ref:`~PyQt6.QtQml.qmlRegisterType`, :sip:ref:`~PyQt6.QtQml.qmlRegisterSingletonType`.
