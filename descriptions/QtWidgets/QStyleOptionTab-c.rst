.. sip:class-description::
    :status: todo
    :brief: Used to describe the parameters for drawing a tab bar
    :digest: b0a6b99a2c386c422493b3d0b20391d3

The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionTab` class is used to describe the parameters for drawing a tab bar.

The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionTab` class is used for drawing several built-in Qt widgets including :sip:ref:`~PyQt6.QtWidgets.QTabBar` and the panel for :sip:ref:`~PyQt6.QtWidgets.QTabWidget`.

An instance of the :sip:ref:`~PyQt6.QtWidgets.QStyleOptionTab` class has type :sip:ref:`~PyQt6.QtWidgets.QStyleOption.OptionType.SO_Tab` and version 3. The type is used internally by :sip:ref:`~PyQt6.QtWidgets.QStyleOption`, its subclasses, and qstyleoption_cast() to determine the type of style option. In general you do not need to worry about this unless you want to create your own :sip:ref:`~PyQt6.QtWidgets.QStyleOption` subclass and your own styles. The version is used by :sip:ref:`~PyQt6.QtWidgets.QStyleOption` subclasses to implement extensions without breaking compatibility. If you use qstyleoption_cast(), you normally do not need to check it.

For performance reasons, there are few member functions and the access to the member variables is direct (i.e., using the ``.`` or ``->`` operator). This makes the structures straightforward to use and emphasizes that these are simply parameters used by the style functions.

For an example demonstrating how style options can be used, see the `Styles <https://doc.qt.io/qt-6/qtwidgets-widgets-styles-example.html>`_ example.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption`.
