.. sip:class-description::
    :status: todo
    :brief: Blank space in a layout
    :digest: bc705968538b2dd801ae5f6ee35396f0

The :sip:ref:`~PyQt6.QtWidgets.QSpacerItem` class provides blank space in a layout.

Normally, you don't need to use this class directly. Qt's built-in layout managers provide the following functions for manipulating empty space in layouts:

+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Class                                   | Functions                                                                                                                                                                                                                                   |
+=========================================+=============================================================================================================================================================================================================================================+
| :sip:ref:`~PyQt6.QtWidgets.QHBoxLayout` | :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addSpacing`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addStretch`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertSpacing`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertStretch`                            |
+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QGridLayout` | :sip:ref:`~PyQt6.QtWidgets.QGridLayout.setRowMinimumHeight`, :sip:ref:`~PyQt6.QtWidgets.QGridLayout.setRowStretch`, :sip:ref:`~PyQt6.QtWidgets.QGridLayout.setColumnMinimumWidth`, :sip:ref:`~PyQt6.QtWidgets.QGridLayout.setColumnStretch` |
+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLayout`, :sip:ref:`~PyQt6.QtWidgets.QWidgetItem`, :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.spacerItem`.
