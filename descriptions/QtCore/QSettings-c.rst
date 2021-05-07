.. sip:class-description::
    :status: todo
    :brief: Persistent platform-independent application settings
    :digest: 47248cf29dbcc29c0f50ded27fa292c8

The :sip:ref:`~PyQt6.QtCore.QSettings` class provides persistent platform-independent application settings.

Users normally expect an application to remember its settings (window sizes and positions, options, etc.) across sessions. This information is often stored in the system registry on Windows, and in property list files on macOS and iOS. On Unix systems, in the absence of a standard, many applications (including the KDE applications) use INI text files.

:sip:ref:`~PyQt6.QtCore.QSettings` is an abstraction around these technologies, enabling you to save and restore application settings in a portable manner. It also supports custom storage formats.

:sip:ref:`~PyQt6.QtCore.QSettings`'s API is based on :sip:ref:`~PyQt6.QtCore.QVariant`, allowing you to save most value-based types, such as QString, :sip:ref:`~PyQt6.QtCore.QRect`, and :sip:ref:`~PyQt6.QtGui.QImage`, with the minimum of effort.

If all you need is a non-persistent memory-based structure, consider using QMap<QString, :sip:ref:`~PyQt6.QtCore.QVariant`> instead.

.. _qsettings-basic-usage:

Basic Usage
-----------

When creating a :sip:ref:`~PyQt6.QtCore.QSettings` object, you must pass the name of your company or organization as well as the name of your application. For example, if your product is called Star Runner and your company is called MySoft, you would construct the :sip:ref:`~PyQt6.QtCore.QSettings` object as follows:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 61-61

:sip:ref:`~PyQt6.QtCore.QSettings` objects can be created either on the stack or on the heap (i.e. using ``new``). Constructing and destroying a :sip:ref:`~PyQt6.QtCore.QSettings` object is very fast.

If you use :sip:ref:`~PyQt6.QtCore.QSettings` from many places in your application, you might want to specify the organization name and the application name using :sip:ref:`~PyQt6.QtCore.QCoreApplication.setOrganizationName` and :sip:ref:`~PyQt6.QtCore.QCoreApplication.setApplicationName`, and then use the default :sip:ref:`~PyQt6.QtCore.QSettings` constructor:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 68-68

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 70-70

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 72-72

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 76-76

(Here, we also specify the organization's Internet domain. When the Internet domain is set, it is used on macOS and iOS instead of the organization name, since macOS and iOS applications conventionally use Internet domains to identify themselves. If no domain is set, a fake domain is derived from the organization name. See the :ref:`qsettings-platform-specific-notes` below for details.)

:sip:ref:`~PyQt6.QtCore.QSettings` stores settings. Each setting consists of a QString that specifies the setting's name (the *key*) and a :sip:ref:`~PyQt6.QtCore.QVariant` that stores the data associated with the key. To write a setting, use :sip:ref:`~PyQt6.QtCore.QSettings.setValue`. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 80-80

If there already exists a setting with the same key, the existing value is overwritten by the new value. For efficiency, the changes may not be saved to permanent storage immediately. (You can always call :sip:ref:`~PyQt6.QtCore.QSettings.sync` to commit your changes.)

You can get a setting's value back using :sip:ref:`~PyQt6.QtCore.QSettings.value`:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 82-82

If there is no setting with the specified name, :sip:ref:`~PyQt6.QtCore.QSettings` returns a null :sip:ref:`~PyQt6.QtCore.QVariant` (which can be converted to the integer 0). You can specify another default value by passing a second argument to :sip:ref:`~PyQt6.QtCore.QSettings.value`:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 86-86

To test whether a given key exists, call :sip:ref:`~PyQt6.QtCore.QSettings.contains`. To remove the setting associated with a key, call :sip:ref:`~PyQt6.QtCore.QSettings.remove`. To obtain the list of all keys, call :sip:ref:`~PyQt6.QtCore.QSettings.allKeys`. To remove all keys, call :sip:ref:`~PyQt6.QtCore.QSettings.clear`.

.. _qsettings-qvariant-and-gui-types:

QVariant and GUI Types
----------------------

Because :sip:ref:`~PyQt6.QtCore.QVariant` is part of the Qt Core module, it cannot provide conversion functions to data types such as :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtGui.QImage`, and :sip:ref:`~PyQt6.QtGui.QPixmap`, which are part of Qt GUI. In other words, there is no ``toColor()``, ``toImage()``, or ``toPixmap()`` functions in :sip:ref:`~PyQt6.QtCore.QVariant`.

Instead, you can use the :sip:ref:`~PyQt6.QtCore.QVariant.value` template function. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 54-55

The inverse conversion (e.g., from :sip:ref:`~PyQt6.QtGui.QColor` to :sip:ref:`~PyQt6.QtCore.QVariant`) is automatic for all data types supported by :sip:ref:`~PyQt6.QtCore.QVariant`, including GUI-related types:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 60-62

Custom types registered using qRegisterMetaType() that have operators for streaming to and from a :sip:ref:`~PyQt6.QtCore.QDataStream` can be stored using :sip:ref:`~PyQt6.QtCore.QSettings`.

.. _qsettings-section-and-key-syntax:

Section and Key Syntax
----------------------

Setting keys can contain any Unicode characters. The Windows registry and INI files use case-insensitive keys, whereas the CFPreferences API on macOS and iOS uses case-sensitive keys. To avoid portability problems, follow these simple rules:

#. Always refer to the same key using the same case. For example, if you refer to a key as "text fonts" in one place in your code, don't refer to it as "Text Fonts" somewhere else.

#. Avoid key names that are identical except for the case. For example, if you have a key called "MainWindow", don't try to save another key as "mainwindow".

#. Do not use slashes ('/' and '\\') in section or key names; the backslash character is used to separate sub keys (see below). On windows '\\' are converted by :sip:ref:`~PyQt6.QtCore.QSettings` to '/', which makes them identical.

You can form hierarchical keys using the '/' character as a separator, similar to Unix file paths. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 91-91

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 93-93

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 95-95

If you want to save or restore many settings with the same prefix, you can specify the prefix using :sip:ref:`~PyQt6.QtCore.QSettings.beginGroup` and call :sip:ref:`~PyQt6.QtCore.QSettings.endGroup` at the end. Here's the same example again, but this time using the group mechanism:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 99-102

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 106-108

If a group is set using :sip:ref:`~PyQt6.QtCore.QSettings.beginGroup`, the behavior of most functions changes consequently. Groups can be set recursively.

In addition to groups, :sip:ref:`~PyQt6.QtCore.QSettings` also supports an "array" concept. See :sip:ref:`~PyQt6.QtCore.QSettings.beginReadArray` and :sip:ref:`~PyQt6.QtCore.QSettings.beginWriteArray` for details.

.. _qsettings-fallback-mechanism:

Fallback Mechanism
------------------

Let's assume that you have created a :sip:ref:`~PyQt6.QtCore.QSettings` object with the organization name MySoft and the application name Star Runner. When you look up a value, up to four locations are searched in that order:

#. a user-specific location for the Star Runner application

#. a user-specific location for all applications by MySoft

#. a system-wide location for the Star Runner application

#. a system-wide location for all applications by MySoft

(See :ref:`qsettings-platform-specific-notes` below for information on what these locations are on the different platforms supported by Qt.)

If a key cannot be found in the first location, the search goes on in the second location, and so on. This enables you to store system-wide or organization-wide settings and to override them on a per-user or per-application basis. To turn off this mechanism, call :sip:ref:`~PyQt6.QtCore.QSettings.setFallbacksEnabled`\ (false).

Although keys from all four locations are available for reading, only the first file (the user-specific location for the application at hand) is accessible for writing. To write to any of the other files, omit the application name and/or specify :sip:ref:`~PyQt6.QtCore.QSettings.Scope.SystemScope` (as opposed to :sip:ref:`~PyQt6.QtCore.QSettings.Scope.UserScope`, the default).

Let's see with an example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 115-115

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 117-119

The table below summarizes which :sip:ref:`~PyQt6.QtCore.QSettings` objects access which location. "\ **X**" means that the location is the main location associated to the :sip:ref:`~PyQt6.QtCore.QSettings` object and is used both for reading and for writing; "o" means that the location is used as a fallback when reading.

+-------------------------+----------+----------+----------+----------+
| Locations               | ``obj1`` | ``obj2`` | ``obj3`` | ``obj4`` |
+=========================+==========+==========+==========+==========+
| 1. User, Application    | **X**    |          |          |          |
+-------------------------+----------+----------+----------+----------+
| 2. User, Organization   | o        | **X**    |          |          |
+-------------------------+----------+----------+----------+----------+
| 3. System, Application  | o        |          | **X**    |          |
+-------------------------+----------+----------+----------+----------+
| 4. System, Organization | o        | o        | o        | **X**    |
+-------------------------+----------+----------+----------+----------+

The beauty of this mechanism is that it works on all platforms supported by Qt and that it still gives you a lot of flexibility, without requiring you to specify any file names or registry paths.

If you want to use INI files on all platforms instead of the native API, you can pass :sip:ref:`~PyQt6.QtCore.QSettings.Format.IniFormat` as the first argument to the :sip:ref:`~PyQt6.QtCore.QSettings` constructor, followed by the scope, the organization name, and the application name:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 124-125

Note that type information is not preserved when reading settings from INI files; all values will be returned as QString.

The `Settings Editor <https://doc.qt.io/qt-6/qtwidgets-tools-settingseditor-example.html>`_ example lets you experiment with different settings location and with fallbacks turned on or off.

.. _qsettings-restoring-the-state-of-a-gui-application:

Restoring the State of a GUI Application
----------------------------------------

:sip:ref:`~PyQt6.QtCore.QSettings` is often used to store the state of a GUI application. The following example illustrates how to use :sip:ref:`~PyQt6.QtCore.QSettings` to save and restore the geometry of an application's main window.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 152-160

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 164-172

See `Window Geometry <https://doc.qt.io/qt-6/application-windows.html#window-geometry>`_ for a discussion on why it is better to call :sip:ref:`~PyQt6.QtWidgets.QWidget.resize` and :sip:ref:`~PyQt6.QtWidgets.QWidget.move` rather than :sip:ref:`~PyQt6.QtWidgets.QWidget.setGeometry` to restore a window's geometry.

The ``readSettings()`` and ``writeSettings()`` functions must be called from the main window's constructor and close event handler as follows:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 176-177

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 179-179

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 181-181

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-settings-settings.py
    :lines: 187-195

See the `Application <https://doc.qt.io/qt-6/qtwidgets-mainwindows-application-example.html>`_ example for a self-contained example that uses :sip:ref:`~PyQt6.QtCore.QSettings`.

.. _qsettings-accessing-settings-from-multiple-threads-or-processes-simultaneously:

Accessing Settings from Multiple Threads or Processes Simultaneously
--------------------------------------------------------------------

:sip:ref:`~PyQt6.QtCore.QSettings` is reentrant. This means that you can use distinct :sip:ref:`~PyQt6.QtCore.QSettings` object in different threads simultaneously. This guarantee stands even when the :sip:ref:`~PyQt6.QtCore.QSettings` objects refer to the same files on disk (or to the same entries in the system registry). If a setting is modified through one :sip:ref:`~PyQt6.QtCore.QSettings` object, the change will immediately be visible in any other :sip:ref:`~PyQt6.QtCore.QSettings` objects that operate on the same location and that live in the same process.

:sip:ref:`~PyQt6.QtCore.QSettings` can safely be used from different processes (which can be different instances of your application running at the same time or different applications altogether) to read and write to the same system locations, provided certain conditions are met. For :sip:ref:`~PyQt6.QtCore.QSettings.Format.IniFormat`, it uses advisory file locking and a smart merging algorithm to ensure data integrity. The condition for that to work is that the writeable configuration file must be a regular file and must reside in a directory that the current user can create new, temporary files in. If that is not the case, then one must use :sip:ref:`~PyQt6.QtCore.QSettings.setAtomicSyncRequired` to turn the safety off.

Note that :sip:ref:`~PyQt6.QtCore.QSettings.sync` imports changes made by other processes (in addition to writing the changes from this :sip:ref:`~PyQt6.QtCore.QSettings`).

.. _qsettings-platform-specific-notes:

Platform-Specific Notes
-----------------------

.. _qsettings-locations-where-application-settings-are-stored:

Locations Where Application Settings Are Stored
...............................................

As mentioned in the :ref:`qsettings-fallback-mechanism` section, :sip:ref:`~PyQt6.QtCore.QSettings` stores settings for an application in up to four locations, depending on whether the settings are user-specific or system-wide and whether the settings are application-specific or organization-wide. For simplicity, we're assuming the organization is called MySoft and the application is called Star Runner.

On Unix systems, if the file format is :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat`, the following files are used by default:

#. ``$HOME/.config/MySoft/Star Runner.conf`` (Qt for Embedded Linux: ``$HOME/Settings/MySoft/Star Runner.conf``)

#. ``$HOME/.config/MySoft.conf`` (Qt for Embedded Linux: ``$HOME/Settings/MySoft.conf``)

#. for each directory <dir> in $XDG_CONFIG_DIRS: ``<dir>/MySoft/Star Runner.conf``

#. for each directory <dir> in $XDG_CONFIG_DIRS: ``<dir>/MySoft.conf``

**Note:** If XDG_CONFIG_DIRS is unset, the default value of ``/etc/xdg`` is used.

On macOS and iOS, if the file format is :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat`, these files are used by default:

#. ``$HOME/Library/Preferences/com.MySoft.Star Runner.plist``

#. ``$HOME/Library/Preferences/com.MySoft.plist``

#. ``/Library/Preferences/com.MySoft.Star Runner.plist``

#. ``/Library/Preferences/com.MySoft.plist``

On Windows, :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat` settings are stored in the following registry paths:

#. ``HKEY_CURRENT_USER\Software\MySoft\Star Runner``

#. ``HKEY_CURRENT_USER\Software\MySoft\OrganizationDefaults``

#. ``HKEY_LOCAL_MACHINE\Software\MySoft\Star Runner``

#. ``HKEY_LOCAL_MACHINE\Software\MySoft\OrganizationDefaults``

**Note:** On Windows, for 32-bit programs running in WOW64 mode, settings are stored in the following registry path: ``HKEY_LOCAL_MACHINE\Software\WOW6432node``.

If the file format is :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat`, this is "Settings/MySoft/Star Runner.conf" in the application's home directory.

If the file format is :sip:ref:`~PyQt6.QtCore.QSettings.Format.IniFormat`, the following files are used on Unix, macOS, and iOS:

#. ``$HOME/.config/MySoft/Star Runner.ini`` (Qt for Embedded Linux: ``$HOME/Settings/MySoft/Star Runner.ini``)

#. ``$HOME/.config/MySoft.ini`` (Qt for Embedded Linux: ``$HOME/Settings/MySoft.ini``)

#. for each directory <dir> in $XDG_CONFIG_DIRS: ``<dir>/MySoft/Star Runner.ini``

#. for each directory <dir> in $XDG_CONFIG_DIRS: ``<dir>/MySoft.ini``

**Note:** If XDG_CONFIG_DIRS is unset, the default value of ``/etc/xdg`` is used.

On Windows, the following files are used:

#. ``FOLDERID_RoamingAppData\MySoft\Star Runner.ini``

#. ``FOLDERID_RoamingAppData\MySoft.ini``

#. ``FOLDERID_ProgramData\MySoft\Star Runner.ini``

#. ``FOLDERID_ProgramData\MySoft.ini``

The identifiers prefixed by ``FOLDERID_`` are special item ID lists to be passed to the Win32 API function ``SHGetKnownFolderPath()`` to obtain the corresponding path.

``FOLDERID_RoamingAppData`` usually points to ``C:\Users\\ *User Name*\\AppData\\Roaming``, also shown by the environment variable ``%APPDATA%``.

``FOLDERID_ProgramData`` usually points to ``C:\ProgramData``.

If the file format is :sip:ref:`~PyQt6.QtCore.QSettings.Format.IniFormat`, this is "Settings/MySoft/Star Runner.ini" in the application's home directory.

The paths for the ``.ini`` and ``.conf`` files can be changed using :sip:ref:`~PyQt6.QtCore.QSettings.setPath`. On Unix, macOS, and iOS the user can override them by setting the ``XDG_CONFIG_HOME`` environment variable; see :sip:ref:`~PyQt6.QtCore.QSettings.setPath` for details.

.. _qsettings-accessing-ini-and-plist-files-directly:

Accessing INI and .plist Files Directly
.......................................

Sometimes you do want to access settings stored in a specific file or registry path. On all platforms, if you want to read an INI file directly, you can use the :sip:ref:`~PyQt6.QtCore.QSettings` constructor that takes a file name as first argument and pass :sip:ref:`~PyQt6.QtCore.QSettings.Format.IniFormat` as second argument. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 67-68

You can then use the :sip:ref:`~PyQt6.QtCore.QSettings` object to read and write settings in the file.

On macOS and iOS, you can access property list ``.plist`` files by passing :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat` as second argument. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 73-74

.. _qsettings-accessing-the-windows-registry-directly:

Accessing the Windows Registry Directly
.......................................

On Windows, :sip:ref:`~PyQt6.QtCore.QSettings` lets you access settings that have been written with :sip:ref:`~PyQt6.QtCore.QSettings` (or settings in a supported format, e.g., string data) in the system registry. This is done by constructing a :sip:ref:`~PyQt6.QtCore.QSettings` object with a path in the registry and :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat`.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 79-80

All the registry entries that appear under the specified path can be read or written through the :sip:ref:`~PyQt6.QtCore.QSettings` object as usual (using forward slashes instead of backslashes). For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 85-85

Note that the backslash character is, as mentioned, used by :sip:ref:`~PyQt6.QtCore.QSettings` to separate subkeys. As a result, you cannot read or write windows registry entries that contain slashes or backslashes; you should use a native windows API if you need to do so.

.. _qsettings-accessing-common-registry-settings-on-windows:

Accessing Common Registry Settings on Windows
.............................................

On Windows, it is possible for a key to have both a value and subkeys. Its default value is accessed by using "Default" or "." in place of a subkey:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 90-92

On other platforms than Windows, "Default" and "." would be treated as regular subkeys.

.. _qsettings-platform-limitations:

Platform Limitations
....................

While :sip:ref:`~PyQt6.QtCore.QSettings` attempts to smooth over the differences between the different supported platforms, there are still a few differences that you should be aware of when porting your application:

* The Windows system registry has the following limitations: A subkey may not exceed 255 characters, an entry's value may not exceed 16,383 characters, and all the values of a key may not exceed 65,535 characters. One way to work around these limitations is to store the settings using the :sip:ref:`~PyQt6.QtCore.QSettings.Format.IniFormat` instead of the :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat`.

* On Windows, when the Windows system registry is used, :sip:ref:`~PyQt6.QtCore.QSettings` does not preserve the original type of the value. Therefore, the type of the value might change when a new value is set. For example, a value with type ``REG_EXPAND_SZ`` will change to ``REG_SZ``.

* On macOS and iOS, :sip:ref:`~PyQt6.QtCore.QSettings.allKeys` will return some extra keys for global settings that apply to all applications. These keys can be read using :sip:ref:`~PyQt6.QtCore.QSettings.value` but cannot be changed, only shadowed. Calling :sip:ref:`~PyQt6.QtCore.QSettings.setFallbacksEnabled`\ (false) will hide these global settings.

* On macOS and iOS, the CFPreferences API used by :sip:ref:`~PyQt6.QtCore.QSettings` expects Internet domain names rather than organization names. To provide a uniform API, :sip:ref:`~PyQt6.QtCore.QSettings` derives a fake domain name from the organization name (unless the organization name already is a domain name, e.g. OpenOffice.org). The algorithm appends ".com" to the company name and replaces spaces and other illegal characters with hyphens. If you want to specify a different domain name, call :sip:ref:`~PyQt6.QtCore.QCoreApplication.setOrganizationDomain`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.setOrganizationName`, and :sip:ref:`~PyQt6.QtCore.QCoreApplication.setApplicationName` in your ``main()`` function and then use the default :sip:ref:`~PyQt6.QtCore.QSettings` constructor. Another solution is to use preprocessor directives, for example:

  .. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
      :lines: 97-101

* On macOS, permissions to access settings not belonging to the current user (i.e. :sip:ref:`~PyQt6.QtCore.QSettings.Scope.SystemScope`) have changed with 10.7 (Lion). Prior to that version, users having admin rights could access these. For 10.7 and 10.8 (Mountain Lion), only root can. However, 10.9 (Mavericks) changes that rule again but only for the native format (plist files).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QVariant`, :sip:ref:`~PyQt6.QtGui.QSessionManager`, `Settings Editor Example <https://doc.qt.io/qt-6/qtwidgets-tools-settingseditor-example.html>`_, `Qt Widgets - Application Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-application-example.html>`_.
