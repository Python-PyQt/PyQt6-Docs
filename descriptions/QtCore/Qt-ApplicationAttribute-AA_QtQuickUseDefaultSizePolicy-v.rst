.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 6da03e16a491074b22a100c5fa5bdd2b

Qt Quick Layouts use the built-in size policy of `Item <https://doc.qt.io/qt-6/qml-qtquick-item.html>`_. For example, when this is set, Button fills the available width, but has a fixed height. When this is not set, it will use the default sizing behavior of the layout it's in, which is to use its implicit size as the preferred size. This is explained in detail in `Specifying preferred size <https://doc.qt.io/qt-6/qtquicklayouts-overview.html#specifying-preferred-size>`_ and `Size constraints <https://doc.qt.io/qt-6/qtquicklayouts-overview.html#size-constraints>`_. When this is set, the default size policy of the item with the layout can be overridden by explicitly setting `Layout.fillWidth <https://doc.qt.io/qt-6/qml-qtquick-layouts-layout.html#fillWidth-attached-prop>`_ or `Layout.fillHeight <https://doc.qt.io/qt-6/qml-qtquick-layouts-layout.html#fillHeight-attached-prop>`_.
