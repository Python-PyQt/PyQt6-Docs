.. sip:class-description::
    :status: todo
    :brief: Environment for instantiating QML components
    :digest: 638149a818465faed56b6f1ac640ffa7

The :sip:ref:`~PyQt6.QtQml.QQmlEngine` class provides an environment for instantiating QML components.

A :sip:ref:`~PyQt6.QtQml.QQmlEngine` is used to manage :sip:ref:`~PyQt6.QtQml.QQmlComponent` and objects created from them and execute their bindings and functions. :sip:ref:`~PyQt6.QtQml.QQmlEngine` also inherits from :sip:ref:`~PyQt6.QtQml.QJSEngine` which allows seamless integration between your QML components and JavaScript code.

Each QML component is instantiated in a :sip:ref:`~PyQt6.QtQml.QQmlContext`. In QML, contexts are arranged hierarchically and this hierarchy is managed by the :sip:ref:`~PyQt6.QtQml.QQmlEngine`. By default, components are instantiated in the :sip:ref:`~PyQt6.QtQml.QQmlEngine.rootContext`.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent`, :sip:ref:`~PyQt6.QtQml.QQmlContext`, `QML Global Object <https://doc.qt.io/qt-6/qtqml-javascript-qmlglobalobject.html>`_, :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine`.
