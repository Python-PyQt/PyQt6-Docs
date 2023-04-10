.. sip:class-description::
    :status: todo
    :brief: Defines a context within a QML engine
    :digest: 27ddbef4fa1012b6671a21b3274a3e15

The :sip:ref:`~PyQt6.QtQml.QQmlContext` class defines a context within a QML engine.

Contexts hold the objects identified by *id* in a QML document. You can use {\ :sip:ref:`~PyQt6.QtQml.QQmlContext.nameForObject`} and :sip:ref:`~PyQt6.QtQml.QQmlContext.objectForName` to retrieve them.

**Note:** It is the responsibility of the creator to delete any :sip:ref:`~PyQt6.QtQml.QQmlContext` it constructs. If a :sip:ref:`~PyQt6.QtQml.QQmlContext` is no longer needed, it must be destroyed explicitly. The simplest way to ensure this is to give the :sip:ref:`~PyQt6.QtQml.QQmlContext` a :sip:ref:`~PyQt6.QtCore.QObject.setParent`.

.. _qqmlcontext-the-context-hierarchy:

The Context Hierarchy
.....................

Contexts form a hierarchy. The root of this hierarchy is the QML engine's :sip:ref:`~PyQt6.QtQml.QQmlEngine.rootContext`. Each QML component creates its own context when instantiated and some QML elements create extra contexts for themselves.

While QML objects instantiated in a context are not strictly owned by that context, their bindings are. If a context is destroyed, the property bindings of outstanding QML objects will stop evaluating.

.. _qqmlcontext-context-properties:

Context Properties
..................

Contexts also allow data to be exposed to the QML components instantiated by the QML engine. Such data is invisible to any tooling, including the `Qt Quick Compiler <https://doc.qt.io/qt-6/qtqml-qtquick-compiler-tech.html>`_ and to future readers of the QML documents in question. It will only be exposed if the QML component is instantiated in the specific C++ context you are envisioning. In other places, different context data may be exposed instead.

Instead of using the QML context to expose data to your QML components, you should either create additional object properties to hold the data or use singletons. See `Exposing C++ State to QML <https://doc.qt.io/qt-6/qtqml-cppintegration-exposecppstate.html>`_ for a detailed explanation.

Each :sip:ref:`~PyQt6.QtQml.QQmlContext` contains a set of properties, distinct from its :sip:ref:`~PyQt6.QtCore.QObject` properties, that allow data to be explicitly bound to a context by name. The context properties can be defined and updated by calling :sip:ref:`~PyQt6.QtQml.QQmlContext.setContextProperty`.

To simplify binding and maintaining larger data sets, a context object can be set on a :sip:ref:`~PyQt6.QtQml.QQmlContext`. All the properties of the context object are available by name in the context, as though they were all individually added through calls to :sip:ref:`~PyQt6.QtQml.QQmlContext.setContextProperty`. Changes to the property's values are detected through the property's notify signal. Setting a context object is both faster and easier than manually adding and maintaining context property values.

All properties added explicitly by :sip:ref:`~PyQt6.QtQml.QQmlContext.setContextProperty` take precedence over the context object's properties.

Child contexts inherit the context properties of their parents; if a child context sets a context property that already exists in its parent, the new context property overrides that of the parent.

**Warning:** Setting the context object or adding new context properties after an object has been created in that context is an expensive operation (essentially forcing all bindings to re-evaluate). Thus, if you need to use context properties, you should at least complete the "setup" of the context before using it to create any objects.

.. seealso:: `Exposing Attributes of C++ Types to QML <https://doc.qt.io/qt-6/qtqml-cppintegration-exposecppattributes.html>`_.
