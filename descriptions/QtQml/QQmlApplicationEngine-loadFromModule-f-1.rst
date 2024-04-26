.. sip:method-description::
    :status: todo
    :pysig: 4548a82a424de40b70622a91da08ea88
    :realsig: (QAnyStringView, QAnyStringView)
    :digest: a5f6585241e22b2773cb5d8c58107702

Loads the QML type *typeName* from the module specified by *uri*. If the type originates from a QML file located at a remote url, the type will be loaded asynchronously. Listen to the :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine.objectCreated` signal to determine when the object tree is ready.

If an error occurs, the :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine.objectCreated` signal is emitted with a null pointer as parameter and error messages are printed with :sip:ref:`~PyQt6.QtCore.qWarning`.

::

    QQmlApplicationEngine engine;
    engine.loadFromModule("QtQuick", "Rectangle");

**Note:** The module identified by *uri* is searched in the `import path <https://doc.qt.io/qt-6/qtqml-syntax-imports.html#qml-import-path>`_, in the same way as if you were doing ``import uri`` inside a QML file. If the module cannot be located there, this function will fail.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.loadFromModule`.
