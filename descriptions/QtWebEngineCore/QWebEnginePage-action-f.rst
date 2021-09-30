.. sip:method-description::
    :status: todo
    :pysig: 2a0f438f9edc267e4c569af826a80f64
    :realsig: (QWebEnginePage::WebAction) const
    :digest: de62f39c280c5ec1b34a073677ae884d

Returns a :sip:ref:`~PyQt6.QtGui.QAction` for the specified :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.WebAction.WebAction` *action*.

The action is owned by the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage` but you can customize the look by changing its properties.

:sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage` also takes care of implementing the action, so that upon triggering the corresponding action is performed on the page.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.triggerAction`.
