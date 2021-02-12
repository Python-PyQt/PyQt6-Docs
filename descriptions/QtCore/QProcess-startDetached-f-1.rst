.. sip:method-description::
    :status: todo
    :pysig: f7153d33eecb245f005d4fbac38861ad
    :realsig: (const QString&,const QStringList&,const QString&,qint64*)
    :digest: a06f1da41f31ea6c0cdc08bad12dfe52

This function overloads :sip:ref:`~PyQt6.QtCore.QProcess.startDetached`.

Starts the program *program* with the arguments *arguments* in a new process, and detaches from it. Returns ``true`` on success; otherwise returns ``false``. If the calling process exits, the detached process will continue to run unaffected.

Argument handling is identical to the respective :sip:ref:`~PyQt6.QtCore.QProcess.start` overload.

The process will be started in the directory *workingDirectory*. If *workingDirectory* is empty, the working directory is inherited from the calling process.

If the function is successful then \*\ *pid* is set to the process identifier of the started process.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.start`.
