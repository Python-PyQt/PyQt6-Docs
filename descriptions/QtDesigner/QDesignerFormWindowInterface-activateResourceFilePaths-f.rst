.. sip:method-description::
    :status: todo
    :pysig: e96ed18e57c3212e2beb25f2c5b13027
    :realsig: (const QStringList&,int*,QString*)
    :digest: ff0b1aad9aec3b0285c046726053d21c

Activates the resource (.qrc) file paths *paths*, returning the count of errors in *errorCount* and error message in *errorMessages*. *Qt Designer* loads the resources using the :sip:ref:`~PyQt6.QtCore.QResource` class, making them available for form editing.

In IDE integrations, a list of the project's resource (.qrc) file can be activated, making them available to *Qt Designer*.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.activeResourceFilePaths`, :sip:ref:`~PyQt6.QtCore.QResource`.
