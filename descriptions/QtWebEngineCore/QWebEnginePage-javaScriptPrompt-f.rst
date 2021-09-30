.. sip:method-description::
    :status: todo
    :pysig: 2f4b53c1c70fe379b64b83147938386b
    :realsig: (const QUrl&,const QString&,const QString&,QString*)
    :digest: 5ec387bca436e851526c9f60c54a1ec1

This function is called whenever a JavaScript program running in a frame affiliated with *securityOrigin* tries to prompt the user for input. The program may provide an optional message, *msg*, as well as a default value for the input in *defaultValue*.

If the prompt was cancelled by the user, the implementation should return ``false``; otherwise the result should be written to *result* and ``true`` should be returned. If the prompt was not cancelled by the user, the implementation should return ``true`` and the result string must not be null.

The default implementation uses :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getText`.
