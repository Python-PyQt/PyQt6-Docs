.. sip:class-description::
    :status: todo
    :brief: Allows you to set key-value pairs that can be used in QML bindings
    :digest: 930e1f5c5d1128febc49a760e1b911d6

The :sip:ref:`~PyQt6.QtQml.QQmlPropertyMap` class allows you to set key-value pairs that can be used in QML bindings.

:sip:ref:`~PyQt6.QtQml.QQmlPropertyMap` provides a convenient way to expose domain data to the UI layer. The following example shows how you might declare data in C++ and then access it in QML.

In the C++ file:

::

    // create our data
    QQmlPropertyMap ownerData;
    ownerData.insert("name", QVariant(QString("John Smith")));
    ownerData.insert("phone", QVariant(QString("555-5555")));

    // expose it to the UI layer
    QQuickView view;
    QQmlContext *ctxt = view.rootContext();
    ctxt->setContextProperty("owner", &ownerData);

    view.setSource(QUrl::fromLocalFile("main.qml"));
    view.show();

Then, in ``main.qml``:

::

    Text { text: owner.name + " " + owner.phone }

The binding is dynamic - whenever a key's value is updated, anything bound to that key will be updated as well.

To detect value changes made in the UI layer you can connect to the :sip:ref:`~PyQt6.QtQml.QQmlPropertyMap.valueChanged` signal. However, note that :sip:ref:`~PyQt6.QtQml.QQmlPropertyMap.valueChanged` is **NOT** emitted when changes are made by calling :sip:ref:`~PyQt6.QtQml.QQmlPropertyMap.insert` or :sip:ref:`~PyQt6.QtQml.QQmlPropertyMap.clear` - it is only emitted when a value is updated from QML.

**Note:** It is not possible to remove keys from the map; once a key has been added, you can only modify or clear its associated value.

**Note:** When deriving a class from :sip:ref:`~PyQt6.QtQml.QQmlPropertyMap`, use the protected two-argument constructor which ensures that the class is correctly registered with the Qt `Meta-Object System <https://doc.qt.io/qt-6/metaobjects.html>`_.

**Note:** The :sip:ref:`~PyQt6.QtCore.QMetaObject` of a :sip:ref:`~PyQt6.QtQml.QQmlPropertyMap` is dynamically generated and modified. Operations on that meta object are not thread safe, so applications need to take care to explicitly synchronize access to the meta object.
