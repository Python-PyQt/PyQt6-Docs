.. sip:class-description::
    :status: todo
    :brief: Layout item that represents a widget
    :digest: a05cd54c068b17972a991c8dc0ae4385

The :sip:ref:`~PyQt6.QtWidgets.QWidgetItem` class is a layout item that represents a widget.

Normally, you don't need to use this class directly. Qt's built-in layout managers provide the following functions for manipulating widgets in layouts:

+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Class                                      | Functions                                                                                                                                                                                                                                                                               |
+============================================+=========================================================================================================================================================================================================================================================================================+
| :sip:ref:`~PyQt6.QtWidgets.QBoxLayout`     | :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addWidget`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertWidget`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.setStretchFactor`                                                                                                                          |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QGridLayout`    | :sip:ref:`~PyQt6.QtWidgets.QGridLayout.addWidget`                                                                                                                                                                                                                                       |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QStackedLayout` | :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.addWidget`, :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.insertWidget`, :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.currentWidget`, :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.setCurrentWidget`, :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.widget` |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLayout`, :sip:ref:`~PyQt6.QtWidgets.QSpacerItem`, :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.widget`.
