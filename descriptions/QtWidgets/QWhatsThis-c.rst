.. sip:class-description::
    :status: todo
    :brief: Simple description of any widget, i.e. answering the question "What's This?"
    :digest: 1e4fd18f2b91066e5677151d496a561d

The :sip:ref:`~PyQt6.QtWidgets.QWhatsThis` class provides a simple description of any widget, i.e. answering the question "What's This?".

"What's This?" help is part of an application's online help system, and provides users with information about the functionality and usage of a particular widget. "What's This?" help texts are typically longer and more detailed than :sip:ref:`~PyQt6.QtWidgets.QToolTip`, but generally provide less information than that supplied by separate help windows.

:sip:ref:`~PyQt6.QtWidgets.QWhatsThis` provides a single window with an explanatory text that pops up when the user asks "What's This?". The default way for users to ask the question is to move the focus to the relevant widget and press Shift+F1. The help text appears immediately; it goes away as soon as the user does something else. (Note that if there is a shortcut for Shift+F1, this mechanism will not work.) Some dialogs provide a "?" button that users can click to enter "What's This?" mode; they then click the relevant widget to pop up the "What's This?" window. It is also possible to provide a a menu option or toolbar button to switch into "What's This?" mode.

To add "What's This?" text to a widget or an action, you simply call :sip:ref:`~PyQt6.QtWidgets.QWidget.setWhatsThis` or :sip:ref:`~PyQt6.QtGui.QAction.setWhatsThis`.

The text can be either rich text or plain text. If you specify a rich text formatted string, it will be rendered using the default stylesheet, making it possible to embed images in the displayed text. To be as fast as possible, the default stylesheet uses a simple method to determine whether the text can be rendered as plain text. See Qt::mightBeRichText() for details.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-whatsthis-whatsthis.py
    :lines: 66-69

An alternative way to enter "What's This?" mode is to call :sip:ref:`~PyQt6.QtWidgets.QWhatsThis.createAction`, and add the returned :sip:ref:`~PyQt6.QtGui.QAction` to either a menu or a tool bar. By invoking this context help action (in the picture below, the button with the arrow and question mark icon) the user switches into "What's This?" mode. If they now click on a widget the appropriate help text is shown. The mode is left when help is given or when the user presses Esc.

.. image:: ../../../images/whatsthis.png

You can enter "What's This?" mode programmatically with :sip:ref:`~PyQt6.QtWidgets.QWhatsThis.enterWhatsThisMode`, check the mode with :sip:ref:`~PyQt6.QtWidgets.QWhatsThis.inWhatsThisMode`, and return to normal mode with :sip:ref:`~PyQt6.QtWidgets.QWhatsThis.leaveWhatsThisMode`.

If you want to control the "What's This?" behavior of a widget manually see :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_CustomWhatsThis`.

It is also possible to show different help texts for different regions of a widget, by using a :sip:ref:`~PyQt6.QtGui.QHelpEvent` of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.WhatsThis`. Intercept the help event in your widget's :sip:ref:`~PyQt6.QtWidgets.QWidget.event` function and call :sip:ref:`~PyQt6.QtWidgets.QWhatsThis.showText` with the text you want to display for the position specified in :sip:ref:`~PyQt6.QtGui.QHelpEvent.pos`. If the text is rich text and the user clicks on a link, the widget also receives a :sip:ref:`~PyQt6.QtGui.QWhatsThisClickedEvent` with the link's reference as :sip:ref:`~PyQt6.QtGui.QWhatsThisClickedEvent.href`. If a :sip:ref:`~PyQt6.QtGui.QWhatsThisClickedEvent` is handled (i.e. :sip:ref:`~PyQt6.QtWidgets.QWidget.event` returns true), the help window remains visible. Call :sip:ref:`~PyQt6.QtWidgets.QWhatsThis.hideText` to hide it explicitly.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QToolTip`.
