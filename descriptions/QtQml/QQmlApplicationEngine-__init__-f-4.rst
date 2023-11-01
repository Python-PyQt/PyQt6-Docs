.. sip:method-description::
    :status: todo
    :pysig: 7d74642492c1254c6ab51fbfe503f7bc
    :realsig: (const QString&, QObject*)
    :digest: 29730108f110fcb79346e858e6b71dce

Create a new :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine` and loads the QML file at the given *filePath*, which must be a local file path. If a relative path is given then it will be interpreted as relative to the working directory of the application.

This is provided as a convenience, and is the same as using the empty constructor and calling load afterwards.
