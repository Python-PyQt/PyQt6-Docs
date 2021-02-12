.. sip:method-description::
    :status: todo
    :pysig: 0281bb2a03f8f3624f862e1826a39fe8
    :realsig: (QObject*)
    :digest: f48556bfd48bd6fc374e9a730db78b83

Constructs a :sip:ref:`~PyQt6.QtCore.QSettings` object for accessing settings of the application and organization set previously with a call to :sip:ref:`~PyQt6.QtCore.QCoreApplication.setOrganizationName`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.setOrganizationDomain`, and :sip:ref:`~PyQt6.QtCore.QCoreApplication.setApplicationName`.

The scope is :sip:ref:`~PyQt6.QtCore.QSettings.Scope.UserScope` and the format is :sip:ref:`~PyQt6.QtCore.QSettings.defaultFormat` (\ :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat` by default). Use :sip:ref:`~PyQt6.QtCore.QSettings.setDefaultFormat` before calling this constructor to change the default format used by this constructor.

The code

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 121-121

is equivalent to

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 126-128

If :sip:ref:`~PyQt6.QtCore.QCoreApplication.setOrganizationName` and :sip:ref:`~PyQt6.QtCore.QCoreApplication.setApplicationName` has not been previously called, the :sip:ref:`~PyQt6.QtCore.QSettings` object will not be able to read or write any settings, and :sip:ref:`~PyQt6.QtCore.QSettings.status` will return :sip:ref:`~PyQt6.QtCore.QSettings.Status.AccessError`.

You should supply both the domain (used by default on macOS and iOS) and the name (used by default elsewhere), although the code will cope if you supply only one, which will then be used (on all platforms), at odds with the usual naming of the file on platforms for which it isn't the default.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.setOrganizationName`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.setOrganizationDomain`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.setApplicationName`, :sip:ref:`~PyQt6.QtCore.QSettings.setDefaultFormat`.
