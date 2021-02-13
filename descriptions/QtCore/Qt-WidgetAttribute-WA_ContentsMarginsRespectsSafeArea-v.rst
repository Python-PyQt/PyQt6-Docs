.. sip:enum-member-description::
    :status: todo
    :value: 130
    :digest: a9c61cc3f8bf9c92ab75aeefe2cb5bfa

A `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ respects the safe area margins of a window by incorporating the margins into its contents' margins by default. This means, that a :sip:ref:`~PyQt6.QtWidgets.QLayout` will use the content area of a widget for its layout, unless the  attribute is set. This along with a contents margin of 0 can be used on the actual layout, to allow for example a background image to underlay the status bar and other system areas on an iOS device, while still allowing child widgets of that background to be inset based on the safe area.
