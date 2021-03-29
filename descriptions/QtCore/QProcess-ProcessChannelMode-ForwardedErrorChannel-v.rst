.. sip:enum-member-description::
    :status: todo
    :value: 4
    :digest: 9ddbfd965b0a26be093eb019c51693b2

`QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ manages the standard output of the running process, but forwards its standard error onto the main process. This reflects the typical use of command line tools as filters, where the standard output is redirected to another process or a file, while standard error is printed to the console for diagnostic purposes. (This value was introduced in Qt 5.2.)
