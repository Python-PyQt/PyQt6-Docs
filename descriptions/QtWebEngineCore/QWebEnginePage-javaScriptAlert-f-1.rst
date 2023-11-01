.. sip:method-description::
    :status: todo
    :pysig: 351fc569fc3d0a3596b6f00cca9976e5
    :realsig: (const QUrl&, const QString&)
    :digest: 0950ba5e7bb56521b7d91e52d882ddae

This function is called whenever a JavaScript program running in a frame affiliated with *securityOrigin* calls the ``alert()`` function with the message *msg*.

The default implementation shows the message, *msg*, with :sip:ref:`~PyQt6.QtWidgets.QMessageBox.information`.
