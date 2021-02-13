.. sip:signal-description::
    :status: todo
    :pysig: 1ba8e8c57b34d839dad7e544f389f2bd
    :realsig: (QObject*,const QUrl&)
    :digest: 941a53c7787aea2bdcedf315bb4aed1e

This signal is emitted when an object finishes loading. If loading was successful, *object* contains a pointer to the loaded object, otherwise the pointer is NULL.

The *url* to the component the *object* came from is also provided.

**Note:** If the path to the component was provided as a QString containing a relative path, the *url* will contain a fully resolved path to the file.
