.. sip:class-description::
    :status: todo
    :brief: Evaluates JavaScript in a QML context
    :digest: 90b2b6125f29a6db3b0895c573ef6d1c

The :sip:ref:`~PyQt6.QtQml.QQmlExpression` class evaluates JavaScript in a QML context.

For example, given a file ``main.qml`` like this:

The following code evaluates a JavaScript expression in the context of the above QML:

::

    QQmlEngine *engine = new QQmlEngine;
    QQmlComponent component(engine, QUrl::fromLocalFile("main.qml"));

    QObject *myObject = component.create();
    QQmlExpression *expr = new QQmlExpression(engine->rootContext(), myObject, "width * 2");
    int result = expr->evaluate().toInt();  // result = 400
