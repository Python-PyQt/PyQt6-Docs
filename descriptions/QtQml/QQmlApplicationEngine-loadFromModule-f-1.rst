.. sip:method-description::
    :status: todo
    :pysig: 4548a82a424de40b70622a91da08ea88
    :realsig: (QAnyStringView, QAnyStringView)
    :digest: 713a812c8452c8ac37096037610c9ce9

Loads the QML type *typeName* from the module specified by *uri*. If the type originates from a QML file located at a remote url, the type will be loaded asynchronously. Listen to the :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine.objectCreated` signal to determine when the object tree is ready.

If an error occurs, the :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine.objectCreated` signal is emitted with a null pointer as parameter and error messages are printed with :sip:ref:`~PyQt6.QtCore.qWarning`.

::

    QQmlApplicationEngine engine;
    engine.loadFromModule("QtQuick", "Rectangle");

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.loadFromModule`.
