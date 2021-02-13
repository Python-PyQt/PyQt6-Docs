.. sip:class-description::
    :status: todo
    :brief: Encapsulates a QML component definition
    :digest: 47a7acd7472172f14aa41d028c0e04a7

The :sip:ref:`~PyQt6.QtQml.QQmlComponent` class encapsulates a QML component definition.

Components are reusable, encapsulated QML types with well-defined interfaces.

A :sip:ref:`~PyQt6.QtQml.QQmlComponent` instance can be created from a QML file. For example, if there is a ``main.qml`` file like this:

The following code loads this QML file as a component, creates an instance of this component using :sip:ref:`~PyQt6.QtQml.QQmlComponent.create`, and then queries the `Item <https://doc.qt.io/qt-6/qml-qtquick-item.html>`_'s `width <https://doc.qt.io/qt-6/qml-qtquick-item.html#width-prop>`_ value:

::

    QQmlEngine *engine = new QQmlEngine;
    QQmlComponent component(engine, QUrl::fromLocalFile("main.qml"));

    QObject *myObject = component.create();
    QQuickItem *item = qobject_cast<QQuickItem*>(myObject);
    int width = item->width();  // width = 200

To create instances of a component in code where a :sip:ref:`~PyQt6.QtQml.QQmlEngine` instance is not available, you can use :sip:ref:`~PyQt6.QtQml.qmlContext` or :sip:ref:`~PyQt6.QtQml.qmlEngine`. For example, in the scenario below, child items are being created within a :sip:ref:`~PyQt6.QtQuick.QQuickItem` subclass:

::

    void MyCppItem::init()
    {
        QQmlEngine *engine = qmlEngine(this);
        // Or:
        // QQmlEngine *engine = qmlContext(this)->engine();
        QQmlComponent component(engine, QUrl::fromLocalFile("MyItem.qml"));
        QQuickItem *childItem = qobject_cast<QQuickItem*>(component.create());
        childItem->setParentItem(this);
    }

Note that these functions will return ``null`` when called inside the constructor of a :sip:ref:`~PyQt6.QtCore.QObject` subclass, as the instance will not yet have a context nor engine.

.. _qqmlcomponent-network-components:

Network Components
..................

If the URL passed to :sip:ref:`~PyQt6.QtQml.QQmlComponent` is a network resource, or if the QML document references a network resource, the :sip:ref:`~PyQt6.QtQml.QQmlComponent` has to fetch the network data before it is able to create objects. In this case, the :sip:ref:`~PyQt6.QtQml.QQmlComponent` will have a :sip:ref:`~PyQt6.QtQml.QQmlComponent.Status.Loading` :sip:ref:`~PyQt6.QtQml.QQmlComponent.status`. An application will have to wait until the component is :sip:ref:`~PyQt6.QtQml.QQmlComponent.Status.Ready` before calling :sip:ref:`~PyQt6.QtQml.QQmlComponent.create`.

The following example shows how to load a QML file from a network resource. After creating the :sip:ref:`~PyQt6.QtQml.QQmlComponent`, it tests whether the component is loading. If it is, it connects to the :sip:ref:`~PyQt6.QtQml.QQmlComponent.statusChanged` signal and otherwise calls the ``continueLoading()`` method directly. Note that :sip:ref:`~PyQt6.QtQml.QQmlComponent.isLoading` may be false for a network component if the component has been cached and is ready immediately.

::

    MyApplication::MyApplication()
    {
        // ...
        component = new QQmlComponent(engine, QUrl("http://www.example.com/main.qml"));
        if (component->isLoading())
            QObject::connect(component, SIGNAL(statusChanged(QQmlComponent::Status)),
                             this, SLOT(continueLoading()));
        else
            continueLoading();
    }

    void MyApplication::continueLoading()
    {
        if (component->isError()) {
            qWarning() << component->errors();
        } else {
            QObject *myObject = component->create();
        }
    }
