.. sip:class-description::
    :status: todo
    :brief: Generates log messages
    :digest: 4673ee050a8151502e1d921cdf16ab41

The :sip:ref:`~PyQt6.QtCore.QMessageLogger` class generates log messages.

:sip:ref:`~PyQt6.QtCore.QMessageLogger` is used to generate messages for the Qt logging framework. Usually one uses it through :sip:ref:`~PyQt6.QtCore.qDebug`, :sip:ref:`~PyQt6.QtCore.qInfo`, :sip:ref:`~PyQt6.QtCore.qWarning`, :sip:ref:`~PyQt6.QtCore.qCritical`, or :sip:ref:`~PyQt6.QtCore.qFatal` functions, which are actually macros: For example :sip:ref:`~PyQt6.QtCore.qDebug` expands to :sip:ref:`~PyQt6.QtCore.QMessageLogger`\ (__FILE__, __LINE__, Q_FUNC_INFO).\ :sip:ref:`~PyQt6.QtCore.QMessageLogger.debug` for debug builds, and :sip:ref:`~PyQt6.QtCore.QMessageLogger`\ (0, 0, 0).\ :sip:ref:`~PyQt6.QtCore.QMessageLogger.debug` for release builds.

One example of direct use is to forward errors that stem from a scripting language, e.g. QML:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-qlogging-qlogging.py
    :lines: 58-65

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMessageLogContext`, :sip:ref:`~PyQt6.QtCore.qDebug`, :sip:ref:`~PyQt6.QtCore.qInfo`, :sip:ref:`~PyQt6.QtCore.qWarning`, :sip:ref:`~PyQt6.QtCore.qCritical`, :sip:ref:`~PyQt6.QtCore.qFatal`.
