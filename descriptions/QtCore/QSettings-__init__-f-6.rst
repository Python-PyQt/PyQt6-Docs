.. sip:method-description::
    :status: todo
    :pysig: 61f46cad57ed4820e8a0c785c38ecb19
    :realsig: (const QString&, const QString&, QObject*)
    :digest: e11f667b79a59e7a172f8235b52671a3

Constructs a :sip:ref:`~PyQt6.QtCore.QSettings` object for accessing settings of the application called *application* from the organization called *organization*, and with parent *parent*.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 116-116

The scope is set to :sip:ref:`~PyQt6.QtCore.QSettings.Scope.UserScope`, and the format is set to :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat` (i.e. calling :sip:ref:`~PyQt6.QtCore.QSettings.setDefaultFormat` before calling this constructor has no effect).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.setDefaultFormat`, :ref:`qsettings-fallback-mechanism`.
