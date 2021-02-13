.. sip:class-description::
    :status: todo
    :brief: Defines a context within a QML engine
    :digest: ad83d85c8d0d5dcaaf886c2a516eb18f

The :sip:ref:`~PyQt6.QtQml.QQmlContext` class defines a context within a QML engine.

Contexts allow data to be exposed to the QML components instantiated by the QML engine.

Each :sip:ref:`~PyQt6.QtQml.QQmlContext` contains a set of properties, distinct from its :sip:ref:`~PyQt6.QtCore.QObject` properties, that allow data to be explicitly bound to a context by name. The context properties are defined and updated by calling :sip:ref:`~PyQt6.QtQml.QQmlContext.setContextProperty`. The following example shows a Qt model being bound to a context and then accessed from a QML file.

::

    QQmlEngine engine;
    QStringListModel modelData;
    QQmlContext *context = new QQmlContext(engine.rootContext());
    context->setContextProperty("myModel", &modelData);

    QQmlComponent component(&engine);
    component.setData("import QtQuick 2.0\nListView { model: myModel }", QUrl());
    QObject *window = component.create(context);

Note it is the responsibility of the creator to delete any :sip:ref:`~PyQt6.QtQml.QQmlContext` it constructs. If the ``context`` object in the example is no longer needed when the ``window`` component instance is destroyed, the ``context`` must be destroyed explicitly. The simplest way to ensure this is to set ``window`` as the parent of ``context``.

To simplify binding and maintaining larger data sets, a context object can be set on a :sip:ref:`~PyQt6.QtQml.QQmlContext`. All the properties of the context object are available by name in the context, as though they were all individually added through calls to :sip:ref:`~PyQt6.QtQml.QQmlContext.setContextProperty`. Changes to the property's values are detected through the property's notify signal. Setting a context object is both faster and easier than manually adding and maintaining context property values.

The following example has the same effect as the previous one, but it uses a context object.

::

    class MyDataSet : ... {
        ...
        Q_PROPERTY(QAbstractItemModel *myModel READ model NOTIFY modelChanged)
        ...
    };

    MyDataSet myDataSet;
    QQmlEngine engine;
    QQmlContext *context = new QQmlContext(engine.rootContext());
    context->setContextObject(&myDataSet);

    QQmlComponent component(&engine);
    component.setData("import QtQuick 2.0\nListView { model: myModel }", QUrl());
    component.create(context);

All properties added explicitly by :sip:ref:`~PyQt6.QtQml.QQmlContext.setContextProperty` take precedence over the context object's properties.

.. _qqmlcontext-the-context-hierarchy:

The Context Hierarchy
.....................

Contexts form a hierarchy. The root of this hierarchy is the QML engine's :sip:ref:`~PyQt6.QtQml.QQmlEngine.rootContext`. Child contexts inherit the context properties of their parents; if a child context sets a context property that already exists in its parent, the new context property overrides that of the parent.

The following example defines two contexts - ``context1`` and ``context2``. The second context overrides the "b" context property inherited from the first with a new value.

::

    QQmlEngine engine;
    QQmlContext *context1 = new QQmlContext(engine.rootContext());
    QQmlContext *context2 = new QQmlContext(context1);

    context1->setContextProperty("a", 12);
    context1->setContextProperty("b", 12);

    context2->setContextProperty("b", 15);

While QML objects instantiated in a context are not strictly owned by that context, their bindings are. If a context is destroyed, the property bindings of outstanding QML objects will stop evaluating.

**Warning:** Setting the context object or adding new context properties after an object has been created in that context is an expensive operation (essentially forcing all bindings to reevaluate). Thus whenever possible you should complete "setup" of the context before using it to create any objects.

.. seealso:: `Exposing Attributes of C++ Types to QML <https://doc.qt.io/qt-6/qtqml-cppintegration-exposecppattributes.html>`_.
