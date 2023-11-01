.. sip:class-description::
    :status: todo
    :brief: Holds a native key used by QSystemSemaphore and QSharedMemory
    :digest: 539bdd7ba962cfd3cc887aa5e7704456

The :sip:ref:`~PyQt6.QtCore.QNativeIpcKey` class holds a native key used by :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` and :sip:ref:`~PyQt6.QtCore.QSharedMemory`.

The :sip:ref:`~PyQt6.QtCore.QSharedMemory` and :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` classes identify their resource using a system-wide identifier known as a "key". The low-level key value as well as the key type are encapsulated in Qt using the :sip:ref:`~PyQt6.QtCore.QNativeIpcKey` class.

Those two classes also provide the means to create native keys from a cross-platform identifier, using QSharedMemory::platformSafeKey() and QSystemSemaphore::platformSafeKey(). Applications should never share the input to those functions, as different versions of Qt may perform different transformations, resulting in different native keys. Instead, the application that created the IPC object should communicate the resulting native key using the methods described below.

For details on the key types, platform-specific limitations, and interoperability with older or non-Qt applications, see the `Native IPC Keys <https://doc.qt.io/qt-6/native-ipc-keys.html>`_ documentation. That includes important information for sandboxed applications on Apple platforms, including all apps obtained via the Apple App Store.

.. _qnativeipckey-communicating-keys-to-other-processes:

Communicating keys to other processes
-------------------------------------

.. _qnativeipckey-communicating-keys-to-other-qt-processes:

Communicating keys to other Qt processes
........................................

If the other process supports :sip:ref:`~PyQt6.QtCore.QNativeIpcKey`, the best way of communicating is via the string representation obtained from :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.toString` and parsing it using :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.fromString`. This representation can be stored on a file whose name is well-known or passed on the command-line to a child process using :sip:ref:`~PyQt6.QtCore.QProcess.setArguments`.

If the other process does not support :sip:ref:`~PyQt6.QtCore.QNativeIpcKey`, then the two processes can exchange the :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.nativeKey` but the older code is likely unable to adjust its key type. The :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.legacyDefaultTypeForOs` function returns the type that legacy code used, which may not match the DefaultTypeForOs constant. This is still true even if the old application is not using the same build as the new one (for example, it is a Qt 5 application), provided the options passed to the Qt configure script are the same.

.. _qnativeipckey-communicating-keys-to-non-qt-processes:

Communicating keys to non-Qt processes
......................................

When communicating with non-Qt processes, the application must arrange to obtain the key type the other process is using. This is important particularly on Unix systems, where both :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.Type.PosixRealtime` and :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.Type.SystemV` are common.

.. _qnativeipckey-string-representation-of-native-keys:

String representation of native keys
------------------------------------

The format of the string representation of a :sip:ref:`~PyQt6.QtCore.QNativeIpcKey` is meant to be stable and therefore backwards and forwards compatible, provided the key type is supported by the Qt version in question. That is to say, an older Qt will fail to parse the string representation of a key type introduced after it was released. However, successfully parsing a string representation does not imply the Qt classes can successfully create an object of that type; applications should verify support using QSharedMemory::isKeyTypeSupported() and QSystemSemaphore::isKeyTypeSupported().

The format of the string representation is formed by two components, separated by a colon (':'). The first component is the key type, described in the table below. The second component is a type-specific payload, using :sip:ref:`~PyQt6.QtCore.QByteArray.fromPercentEncoding`. For all currently supported key types, the decoded form is identical to the contents of the :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.nativeKey` field.

+------------------------------------------------------------------+---------------------------------------------+
| Key type                                                         | String representation                       |
+------------------------------------------------------------------+---------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.Type.PosixRealtime`        | ``"posix"``                                 |
+------------------------------------------------------------------+---------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.Type.SystemV`              | ``"systemv"``                               |
+------------------------------------------------------------------+---------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.Type.Windows`              | ``"windows"``                               |
+------------------------------------------------------------------+---------------------------------------------+
| Non-standard :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.Type.SystemV` | ``"systemv-"`` followed by a decimal number |
+------------------------------------------------------------------+---------------------------------------------+

This format resembles a URI and allows parsing using URI/URL-parsing functions, such as :sip:ref:`~PyQt6.QtCore.QUrl`. When parsed by such API, the key type will show up as the :sip:ref:`~PyQt6.QtCore.QUrl.scheme`, and the payload will be the :sip:ref:`~PyQt6.QtCore.QUrl.path`. Use of query or fragments is reserved.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory`, :sip:ref:`~PyQt6.QtCore.QSystemSemaphore`.
