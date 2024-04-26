.. sip:method-description::
    :status: todo
    :pysig: 2a0f438f9edc267e4c569af826a80f64
    :realsig: (QWebEnginePage::WebAction) const
    :digest: bcf52a35b64495aaba0ca56a722a1740

Returns a :sip:ref:`~PyQt6.QtGui.QAction` for the specified :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.WebAction.WebAction` *action*.

The action is owned by the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage` but you can customize the look by changing its properties.

QWebEnginePage::action(WebAction action) does not have a default styled icon. Use :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.pageAction` to have an action with a default styled icon.

:sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage` also takes care of implementing the action, so that upon triggering the corresponding action is performed on the page.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.triggerAction`.
