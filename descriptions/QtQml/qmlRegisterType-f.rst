.. sip:method-description::
    :status: todo
    :pysig: 4a3930cd5a8b5ed17374fbe1e4f549aa
    :realsig: (const QUrl&,const char*,int,int,const char*)
    :digest: 1171f2b18b40e3a963739ffb06932436

This function registers a type in the QML system with the name *qmlName*, in the library imported from *uri* having the version number composed from *versionMajor* and *versionMinor*. The type is defined by the QML file located at *url*. The url must be an absolute URL, i.e. url.isRelative() == false.

Normally QML files can be loaded as types directly from other QML files, or using a qmldir file. This function allows registration of files to types from C++ code, such as when the type mapping needs to be procedurally determined at startup.

Returns -1 if the registration was not successful.
