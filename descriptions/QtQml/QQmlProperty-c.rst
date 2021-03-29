.. sip:class-description::
    :status: todo
    :brief: Abstracts accessing properties on objects created from QML
    :digest: 9412a33531137fb8a01b143815255999

The :sip:ref:`~PyQt6.QtQml.QQmlProperty` class abstracts accessing properties on objects created from QML.

As QML uses Qt's meta-type system all of the existing :sip:ref:`~PyQt6.QtCore.QMetaObject` classes can be used to introspect and interact with objects created by QML. However, some of the new features provided by QML - such as type safety and attached properties - are most easily used through the :sip:ref:`~PyQt6.QtQml.QQmlProperty` class that simplifies some of their natural complexity.

Unlike :sip:ref:`~PyQt6.QtCore.QMetaProperty` which represents a property on a class type, :sip:ref:`~PyQt6.QtQml.QQmlProperty` encapsulates a property on a specific object instance. To read a property's value, programmers create a :sip:ref:`~PyQt6.QtQml.QQmlProperty` instance and call the :sip:ref:`~PyQt6.QtQml.QQmlProperty.read` method. Likewise to write a property value the :sip:ref:`~PyQt6.QtQml.QQmlProperty.write` method is used.

For example, for the following QML code:

The `Text <https://doc.qt.io/qt-6/qml-qtquick-text.html>`_ object's properties could be accessed using :sip:ref:`~PyQt6.QtQml.QQmlProperty`, like this:

::

    #include <QQmlProperty>
    #include <QGraphicsObject>

    ...

    QQuickView view(QUrl::fromLocalFile("MyItem.qml"));
    QQmlProperty property(view.rootObject(), "font.pixelSize");
    qWarning() << "Current pixel size:" << property.read().toInt();
    property.write(24);
    qWarning() << "Pixel size should now be 24:" << property.read().toInt();
