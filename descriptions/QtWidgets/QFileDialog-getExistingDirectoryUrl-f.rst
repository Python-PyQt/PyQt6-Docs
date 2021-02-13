.. sip:method-description::
    :status: todo
    :pysig: ce48770beffb62b8ea9663f12809b9f0
    :realsig: (QWidget*,const QString&,const QUrl&,QFileDialog::Options,const QStringList&)
    :digest: 3c79eec61d1ac16de6afe1807f0757d3

This is a convenience static function that will return an existing directory selected by the user. If the user presses Cancel, it returns an empty url.

The function is used similarly to :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getExistingDirectory`. In particular *parent*, *caption*, *dir* and *options* are used in the exact same way.

The main difference with :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getExistingDirectory` comes from the ability offered to the user to select a remote directory. That's why the return type and the type of *dir* is :sip:ref:`~PyQt6.QtCore.QUrl`.

The *supportedSchemes* argument allows to restrict the type of URLs the user will be able to select. It is a way for the application to declare the protocols it will support to fetch the file content. An empty list means that no restriction is applied (the default). Supported for local files ("file" scheme) is implicit and always enabled; it is not necessary to include it in the restriction.

When possible, this static function will use the native file dialog and not a :sip:ref:`~PyQt6.QtWidgets.QFileDialog`. On platforms which don't support selecting remote files, Qt will allow to select only local files.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getExistingDirectory`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getOpenFileUrl`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getOpenFileUrls`, :sip:ref:`~PyQt6.QtWidgets.QFileDialog.getSaveFileUrl`.
