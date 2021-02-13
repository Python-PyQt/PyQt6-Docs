.. sip:class-description::
    :status: todo
    :brief: Used to describe the base of a tab bar, i.e. the part that the tab bar usually overlaps with
    :digest: ca85d2e56a5031445bdd0d59492e0994

The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionTabBarBase` class is used to describe the base of a tab bar, i.e. the part that the tab bar usually overlaps with.

:sip:ref:`~PyQt6.QtWidgets.QStyleOptionTabBarBase` contains all the information that :sip:ref:`~PyQt6.QtWidgets.QStyle` functions need to draw the tab bar base. Note that this is only drawn for a standalone :sip:ref:`~PyQt6.QtWidgets.QTabBar` (one that isn't part of a :sip:ref:`~PyQt6.QtWidgets.QTabWidget`).

For performance reasons, there are few member functions and the access to the member variables is direct (i.e., using the ``.`` or ``->`` operator). This makes the structures straightforward to use and emphasizes that these are simply parameters used by the style functions.

For an example demonstrating how style options can be used, see the `Styles <https://doc.qt.io/qt-6/qtwidgets-widgets-styles-example.html>`_ example.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption`, :sip:ref:`~PyQt6.QtWidgets.QTabBar.drawBase`.
