.. sip:method-description::
    :status: todo
    :pysig: 00d9eeda9449078d8c3c4fec71a5610c
    :realsig: (const QUrl&, const QString&)
    :digest: 0950ba5e7bb56521b7d91e52d882ddae

This function is called whenever a JavaScript program running in a frame affiliated with *securityOrigin* calls the ``alert()`` function with the message *msg*.

The default implementation shows the message, *msg*, with :sip:ref:`~PyQt6.QtWidgets.QMessageBox.information`.
