.. sip:class-description::
    :status: todo
    :brief: Parameters for input method events
    :digest: 6473d9eb7ae29c5d1e681f550b9fc6a7

The :sip:ref:`~PyQt6.QtGui.QInputMethodEvent` class provides parameters for input method events.

Input method events are sent to widgets when an input method is used to enter text into a widget. Input methods are widely used to enter text for languages with non-Latin alphabets.

Note that when creating custom text editing widgets, the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_InputMethodEnabled` window attribute must be set explicitly (using the :sip:ref:`~PyQt6.QtWidgets.QWidget.setAttribute` function) in order to receive input method events.

The events are of interest to authors of keyboard entry widgets who want to be able to correctly handle languages with complex character input. Text input in such languages is usually a three step process:

#. **Starting to Compose**

   When the user presses the first key on a keyboard, an input context is created. This input context will contain a string of the typed characters.

#. **Composing**

   With every new key pressed, the input method will try to create a matching string for the text typed so far called preedit string. While the input context is active, the user can only move the cursor inside the string belonging to this input context.

#. **Completing**

   At some point, the user will activate a user interface component (perhaps using a particular key) where they can choose from a number of strings matching the text they have typed so far. The user can either confirm their choice cancel the input; in either case the input context will be closed.

:sip:ref:`~PyQt6.QtGui.QInputMethodEvent` models these three stages, and transfers the information needed to correctly render the intermediate result. A :sip:ref:`~PyQt6.QtGui.QInputMethodEvent` has two main parameters: :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.preeditString` and :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.commitString`. The :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.preeditString` parameter gives the currently active preedit string. The :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.commitString` parameter gives a text that should get added to (or replace parts of) the text of the editor widget. It usually is a result of the input operations and has to be inserted to the widgets text directly before the preedit string.

If the :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.commitString` should replace parts of the of the text in the editor, :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.replacementLength` will contain the number of characters to be replaced. :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.replacementStart` contains the position at which characters are to be replaced relative from the start of the preedit string.

A number of attributes control the visual appearance of the preedit string (the visual appearance of text outside the preedit string is controlled by the widget only). The :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.AttributeType.AttributeType` enum describes the different attributes that can be set.

A class implementing :sip:ref:`~PyQt6.QtWidgets.QWidget.inputMethodEvent` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.inputMethodEvent` should at least understand and honor the :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.AttributeType.TextFormat` and :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.AttributeType.Cursor` attributes.

Since input methods need to be able to query certain properties from the widget or graphics item, subclasses must also implement :sip:ref:`~PyQt6.QtWidgets.QWidget.inputMethodQuery` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.inputMethodQuery`, respectively.

When receiving an input method event, the text widget has to performs the following steps:

#. If the widget has selected text, the selected text should get removed.

#. Remove the text starting at :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.replacementStart` with length :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.replacementLength` and replace it by the :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.commitString`. If :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.replacementLength` is 0, :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.replacementStart` gives the insertion position for the :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.commitString`.

   When doing replacement the area of the preedit string is ignored, thus a replacement starting at -1 with a length of 2 will remove the last character before the preedit string and the first character afterwards, and insert the commit string directly before the preedit string.

   If the widget implements undo/redo, this operation gets added to the undo stack.

#. If there is no current preedit string, insert the :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.preeditString` at the current cursor position; otherwise replace the previous :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.preeditString` with the one received from this event.

   If the widget implements undo/redo, the :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.preeditString` should not influence the undo/redo stack in any way.

   The widget should examine the list of attributes to apply to the preedit string. It has to understand at least the :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.AttributeType.TextFormat` and Cursor attributes and render them as specified.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QInputMethod`.
