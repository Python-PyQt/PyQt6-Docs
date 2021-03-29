.. sip:class-description::
    :status: todo
    :brief: Environment for instantiating QML components
    :digest: 32446103b664bf235b30297296f10e6a

The :sip:ref:`~PyQt6.QtQml.QQmlEngine` class provides an environment for instantiating QML components.

Each QML component is instantiated in a :sip:ref:`~PyQt6.QtQml.QQmlContext`. :sip:ref:`~PyQt6.QtQml.QQmlContext`'s are essential for passing data to QML components. In QML, contexts are arranged hierarchically and this hierarchy is managed by the :sip:ref:`~PyQt6.QtQml.QQmlEngine`.

Prior to creating any QML components, an application must have created a :sip:ref:`~PyQt6.QtQml.QQmlEngine` to gain access to a QML context. The following example shows how to create a simple Text item.

::

    QQmlEngine engine;
    QQmlComponent component(&engine);
    component.setData("import QtQuick 2.0\nText { text: \"Hello world!\" }", QUrl());
    QQuickItem *item = qobject_cast<QQuickItem *>(component.create());

    //add item to view, etc
    ...

In this case, the Text item will be created in the engine's :sip:ref:`~PyQt6.QtQml.QQmlEngine.rootContext`.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent`, :sip:ref:`~PyQt6.QtQml.QQmlContext`, `QML Global Object <https://doc.qt.io/qt-6/qtqml-javascript-qmlglobalobject.html>`_.
