.. sip:method-description::
    :status: todo
    :pysig: c073142cd33c010a88c50b6aee90a2a7
    :realsig: (QWidget*,const QString&,const QUrl&,QFileDialog::Options,const QStringList&)
    :digest: 5a90eb7cd98ba030a528f94c99510eb0

This is a convenience static function that returns an existing directory selected by the user. If the user presses Cancel, it returns an empty url.

The function is used similarly to :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getExistingDirectory`. In particular *parent*, *caption*, *dir* and *options* are used in exactly the same way.

The main difference with :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getExistingDirectory` comes from the ability offered to the user to select a remote directory. That's why the return type and the type of *dir* is :sip:ref:`~PyQt6.QtCore.QUrl`.

The *supportedSchemes* argument allows to restrict the type of URLs the user is able to select. It is a way for the application to declare the protocols it supports to fetch the file content. An empty list means that no restriction is applied (the default). Support for local files ("file" scheme) is implicit and always enabled; it is not necessary to include it in the restriction.

When possible, this static function uses the native file dialog and not a :sip:ref:`~PyQt6.QtWidgets.QFileDialog`. On platforms that don't support selecting remote files, Qt allows to select only local files.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getExistingDirectory`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getOpenFileUrl`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getOpenFileUrls`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getSaveFileUrl`.
