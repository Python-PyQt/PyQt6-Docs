.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 5e940c4210370d2e3ce301a9f9002196

This signal is emitted whenever the selection changes, either interactively or programmatically. For example, by calling :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.triggerAction` with a selection action.

**Note:** When using the mouse to select text by left-clicking and dragging, the signal will be emitted for each new character selected, and not upon releasing the left mouse button.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.selectedText`.
