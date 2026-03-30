.. sip:method-description::
    :status: todo
    :pysig: d3f5a2fa44905d475192899f44d42328
    :realsig: (const QString&, QObject*)
    :digest: 29730108f110fcb79346e858e6b71dce

Create a new :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine` and loads the QML file at the given *filePath*, which must be a local file or qrc path. If a relative path is given then it will be interpreted as relative to the working directory of the application.

This is provided as a convenience, and is the same as using the empty constructor and calling load afterwards.
