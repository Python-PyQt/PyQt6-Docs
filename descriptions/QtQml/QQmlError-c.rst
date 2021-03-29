.. sip:class-description::
    :status: todo
    :brief: Encapsulates a QML error
    :digest: 94512efc2f60aa81d56b4c0281081584

The :sip:ref:`~PyQt6.QtQml.QQmlError` class encapsulates a QML error.

:sip:ref:`~PyQt6.QtQml.QQmlError` includes a textual description of the error, as well as location information (the file, line, and column). The :sip:ref:`~PyQt6.QtQml.QQmlError.toString` method creates a single-line, human-readable string containing all of this information, for example:

::

    file:///home/user/test.qml:7:8: Invalid property assignment: double expected

You can use :sip:ref:`~PyQt6.QtCore.qDebug`, :sip:ref:`~PyQt6.QtCore.qInfo`, or :sip:ref:`~PyQt6.QtCore.qWarning` to output errors to the console. This method will attempt to open the file indicated by the error and include additional contextual information.

::

    file:///home/user/test.qml:7:8: Invalid property assignment: double expected
            y: "hello"
               ^

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickView.errors`, :sip:ref:`~PyQt6.QtQml.QQmlComponent.errors`.
