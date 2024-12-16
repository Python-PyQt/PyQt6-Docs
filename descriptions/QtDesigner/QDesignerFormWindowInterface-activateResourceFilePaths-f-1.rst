.. sip:method-description::
    :status: todo
    :pysig: 851943427b720b0c1eec8e5150f4b4a4
    :realsig: (const QStringList&, int*, QString*)
    :digest: 298668286d24c244568d25b223d108b0

Activates the resource (.qrc) file paths *paths*, returning the count of errors in *errorCount* and error message in *errorMessages*. Qt Widgets Designer loads the resources using the :sip:ref:`~PyQt6.QtCore.QResource` class, making them available for form editing.

In IDE integrations, a list of the project's resource (.qrc) file can be activated, making them available to Qt Widgets Designer.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.activeResourceFilePaths`, :sip:ref:`~PyQt6.QtCore.QResource`.
