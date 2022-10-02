.. sip:method-description::
    :status: todo
    :pysig: 0bee5ee99a425921db962be70be70688
    :realsig: ()
    :digest: 4a3acd3d9601fa30d03173a1d87b92e6

This function creates the standard context menu which is shown when the user clicks on the text edit with the right mouse button. It is called from the default :sip:ref:`~PyQt6.QtWidgets.QTextEdit.contextMenuEvent` handler. The popup menu's ownership is transferred to the caller.

We recommend that you use the createStandardContextMenu(\ :sip:ref:`~PyQt6.QtCore.QPoint`) version instead which will enable the actions that are sensitive to where the user clicked.
