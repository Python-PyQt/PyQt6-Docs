.. sip:class-description::
    :status: todo
    :brief: Quick-access button to commands or options, usually used inside a QToolBar
    :digest: 5d1935460fc4275c9d288d9f6b4ce1a3

The :sip:ref:`~PyQt6.QtWidgets.QToolButton` class provides a quick-access button to commands or options, usually used inside a :sip:ref:`~PyQt6.QtWidgets.QToolBar`.

A tool button is a special button that provides quick-access to specific commands or options. As opposed to a normal command button, a tool button usually doesn't show a text label, but shows an icon instead.

Tool buttons are normally created when new :sip:ref:`~PyQt6.QtGui.QAction` instances are created with :sip:ref:`~PyQt6.QtWidgets.QToolBar.addAction` or existing actions are added to a toolbar with :sip:ref:`~PyQt6.QtWidgets.QToolBar.addAction`. It is also possible to construct tool buttons in the same way as any other widget, and arrange them alongside other widgets in layouts.

One classic use of a tool button is to select tools; for example, the "pen" tool in a drawing program. This would be implemented by using a :sip:ref:`~PyQt6.QtWidgets.QToolButton` as a toggle button (see setCheckable()).

:sip:ref:`~PyQt6.QtWidgets.QToolButton` supports auto-raising. In auto-raise mode, the button draws a 3D frame only when the mouse points at it. The feature is automatically turned on when a button is used inside a :sip:ref:`~PyQt6.QtWidgets.QToolBar`. Change it with :sip:ref:`~PyQt6.QtWidgets.QToolButton.setAutoRaise`.

A tool button's icon is set as :sip:ref:`~PyQt6.QtGui.QIcon`. This makes it possible to specify different pixmaps for the disabled and active state. The disabled pixmap is used when the button's functionality is not available. The active pixmap is displayed when the button is auto-raised because the mouse pointer is hovering over it.

The button's look and dimension is adjustable with :sip:ref:`~PyQt6.QtWidgets.QToolButton.setToolButtonStyle` and setIconSize(). When used inside a :sip:ref:`~PyQt6.QtWidgets.QToolBar` in a :sip:ref:`~PyQt6.QtWidgets.QMainWindow`, the button automatically adjusts to :sip:ref:`~PyQt6.QtWidgets.QMainWindow`'s settings (see :sip:ref:`~PyQt6.QtWidgets.QMainWindow.setToolButtonStyle` and :sip:ref:`~PyQt6.QtWidgets.QMainWindow.setIconSize`). Instead of an icon, a tool button can also display an arrow symbol, specified with :sip:ref:`~PyQt6.QtWidgets.QToolButton.arrowType`.

A tool button can offer additional choices in a popup menu. The popup menu can be set using :sip:ref:`~PyQt6.QtWidgets.QToolButton.setMenu`. Use :sip:ref:`~PyQt6.QtWidgets.QToolButton.setPopupMode` to configure the different modes available for tool buttons with a menu set. The default mode is DelayedPopupMode which is sometimes used with the "Back" button in a web browser. After pressing and holding the button down for a while, a menu pops up showing a list of possible pages to jump to. The timeout is style dependent, see :sip:ref:`~PyQt6.QtWidgets.QStyle.StyleHint.SH_ToolButton_PopupDelay`.

+-----------------------------------------------------------------------------------------------------------------------+
| |image-assistant-toolbar-png|                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------+
| Qt Assistant's toolbar contains tool buttons that are associated with actions used in other parts of the main window. |
+-----------------------------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QPushButton`, :sip:ref:`~PyQt6.QtWidgets.QToolBar`, :sip:ref:`~PyQt6.QtWidgets.QMainWindow`, :sip:ref:`~PyQt6.QtGui.QAction`, `GUI Design Handbook: Push Button <https://doc.qt.io/qt-6/guibooks.html#fowler>`_.

.. |image-assistant-toolbar-png| image:: ../../../images/assistant-toolbar.png
