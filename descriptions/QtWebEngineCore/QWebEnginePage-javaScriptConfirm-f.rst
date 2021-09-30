.. sip:method-description::
    :status: todo
    :pysig: 96369ac9329bf8353c2b54cb2525f81e
    :realsig: (const QUrl&,const QString&)
    :digest: f10476556273a83929153413b9472a8a

This function is called whenever a JavaScript program running in a frame affiliated with *securityOrigin* calls the ``confirm()`` function with the message *msg*. Returns ``true`` if the user confirms the message; otherwise returns ``false``.

It is also called when the ``onbeforeunload`` handler is requesting a confirmation before leaving a page.

The default implementation executes the query using :sip:ref:`~PyQt6.QtWidgets.QMessageBox.information` with :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton.Ok` and :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton.Cancel` buttons.
