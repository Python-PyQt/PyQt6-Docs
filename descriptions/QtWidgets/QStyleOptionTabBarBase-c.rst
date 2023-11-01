.. sip:class-description::
    :status: todo
    :brief: Used to describe the base of a tab bar, i.e. the part that the tab bar usually overlaps with
    :digest: 0de54000bf72db11ae2d48d76bc77a68

The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionTabBarBase` class is used to describe the base of a tab bar, i.e. the part that the tab bar usually overlaps with.

:sip:ref:`~PyQt6.QtWidgets.QStyleOptionTabBarBase` contains all the information that :sip:ref:`~PyQt6.QtWidgets.QStyle` functions need to draw the tab bar base. Note that this is only drawn for a standalone :sip:ref:`~PyQt6.QtWidgets.QTabBar` (one that isn't part of a :sip:ref:`~PyQt6.QtWidgets.QTabWidget`).

For performance reasons, there are few member functions and the access to the member variables is direct (i.e., using the ``.`` or ``->`` operator). This makes the structures straightforward to use and emphasizes that these are simply parameters used by the style functions.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption`, :sip:ref:`~PyQt6.QtWidgets.QTabBar.drawBase`.
