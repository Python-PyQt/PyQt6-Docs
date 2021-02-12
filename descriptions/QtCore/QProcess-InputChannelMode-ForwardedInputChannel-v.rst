.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 9ddbfd965b0a26be093eb019c51693b2

`QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ forwards the input of the main process onto the running process. The child process reads its standard input from the same source as the main process. Note that the main process must not try to read its standard input while the child process is running.
