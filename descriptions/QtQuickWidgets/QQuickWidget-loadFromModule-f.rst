.. sip:method-description::
    :status: todo
    :pysig: 4548a82a424de40b70622a91da08ea88
    :realsig: (QAnyStringView, QAnyStringView)
    :digest: 2ed60b7fe91be471459378e6376a4287

Loads the QML component identified by *uri* and *typeName*. If the component is backed by a QML file, :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.source` will be set accordingly. For types defined in ``C++``, ``source`` will be empty.

If any :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.source` was set before this method was called, it will be cleared.

Calling this method multiple times with the same *uri* and *typeName* will result in the QML component being reinstantiated.

.. seealso:: :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.setSource`, :sip:ref:`~PyQt6.QtQml.QQmlComponent.loadFromModule`, :sip:ref:`~PyQt6.QtQml.QQmlApplicationEngine.loadFromModule`.
