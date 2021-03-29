.. sip:method-description::
    :status: todo
    :pysig: 694b7ed9d307ae950646aeb5da98e571
    :realsig: (const QString&,const QString&)
    :digest: 98c8222b1960d235d36e9a2f3397c3f8

Returns the meta data for the Qt compressed help file *documentationFileName*. If there is no data available for *name*, an invalid `QVariant() <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ is returned. The meta data is defined when creating the Qt compressed help file and cannot be modified later. Common meta data includes e.g. the author of the documentation.
