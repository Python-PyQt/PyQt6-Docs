.. sip:method-description::
    :status: todo
    :pysig: 8d249b8e39866890cc8fe2c54281b385
    :realsig: (const QPoint&)
    :digest: 98672ed9a76179bb0121e07aae1f0817

This function creates the standard context menu which is shown when the user clicks on the text edit with the right mouse button. It is called from the default :sip:ref:`~PyQt6.QtWidgets.QTextEdit.contextMenuEvent` handler and it takes the *position* in document coordinates where the mouse click was. This can enable actions that are sensitive to the position where the user clicked. The popup menu's ownership is transferred to the caller.
