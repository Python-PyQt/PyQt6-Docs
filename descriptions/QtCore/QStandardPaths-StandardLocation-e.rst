.. sip:enum-description::
    :status: todo
    :digest: 88f4afd28ebb79beed5770cf95f66355

This enum describes the different locations that can be queried using methods such as :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation`, :sip:ref:`~PyQt6.QtCore.QStandardPaths.standardLocations`, and :sip:ref:`~PyQt6.QtCore.QStandardPaths.displayName`.

Some of the values in this enum represent a user configuration. Such enum values will return the same paths in different applications, so they could be used to share data with other applications. Other values are specific to this application. Each enum value in the table below describes whether it's application-specific or generic.

Application-specific directories should be assumed to be unreachable by other applications. Therefore, files placed there might not be readable by other applications, even if run by the same user. On the other hand, generic directories should be assumed to be accessible by all applications run by this user, but should still be assumed to be unreachable by applications by other users.

Data interchange with other users is out of the scope of :sip:ref:`~PyQt6.QtCore.QStandardPaths`.

The following table gives examples of paths on different operating systems. The first path is the writable path (unless noted). Other, additional paths, if any, represent non-writable locations.

+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Path type             | macOS                                                                                                        | Windows                                                                                                                         |
+=======================+==============================================================================================================+=================================================================================================================================+
| DesktopLocation       | "~/Desktop"                                                                                                  | "C:/Users/<USER>/Desktop"                                                                                                       |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| DocumentsLocation     | "~/Documents"                                                                                                | "C:/Users/<USER>/Documents"                                                                                                     |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| FontsLocation         | "/System/Library/Fonts" (not writable)                                                                       | "C:/Windows/Fonts" (not writable)                                                                                               |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ApplicationsLocation  | "/Applications" (not writable)                                                                               | "C:/Users/<USER>/AppData/Roaming/Microsoft/Windows/Start Menu/Programs"                                                         |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| MusicLocation         | "~/Music"                                                                                                    | "C:/Users/<USER>/Music"                                                                                                         |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| MoviesLocation        | "~/Movies"                                                                                                   | "C:/Users/<USER>/Videos"                                                                                                        |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| PicturesLocation      | "~/Pictures"                                                                                                 | "C:/Users/<USER>/Pictures"                                                                                                      |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| TempLocation          | randomly generated by the OS                                                                                 | "C:/Users/<USER>/AppData/Local/Temp"                                                                                            |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| HomeLocation          | "~"                                                                                                          | "C:/Users/<USER>"                                                                                                               |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| AppLocalDataLocation  | "~/Library/Application Support/<APPNAME>", "/Library/Application Support/<APPNAME>". "<APPDIR>/../Resources" | "C:/Users/<USER>/AppData/Local/<APPNAME>", "C:/ProgramData/<APPNAME>", "<APPDIR>", "<APPDIR>/data", "<APPDIR>/data/<APPNAME>"   |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| CacheLocation         | "~/Library/Caches/<APPNAME>", "/Library/Caches/<APPNAME>"                                                    | "C:/Users/<USER>/AppData/Local/<APPNAME>/cache"                                                                                 |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| GenericDataLocation   | "~/Library/Application Support", "/Library/Application Support"                                              | "C:/Users/<USER>/AppData/Local", "C:/ProgramData", "<APPDIR>", "<APPDIR>/data"                                                  |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| RuntimeLocation       | "~/Library/Application Support"                                                                              | "C:/Users/<USER>"                                                                                                               |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ConfigLocation        | "~/Library/Preferences"                                                                                      | "C:/Users/<USER>/AppData/Local/<APPNAME>", "C:/ProgramData/<APPNAME>"                                                           |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| GenericConfigLocation | "~/Library/Preferences"                                                                                      | "C:/Users/<USER>/AppData/Local", "C:/ProgramData"                                                                               |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| DownloadLocation      | "~/Downloads"                                                                                                | "C:/Users/<USER>/Downloads"                                                                                                     |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| GenericCacheLocation  | "~/Library/Caches", "/Library/Caches"                                                                        | "C:/Users/<USER>/AppData/Local/cache"                                                                                           |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| AppDataLocation       | "~/Library/Application Support/<APPNAME>", "/Library/Application Support/<APPNAME>". "<APPDIR>/../Resources" | "C:/Users/<USER>/AppData/Roaming/<APPNAME>", "C:/ProgramData/<APPNAME>", "<APPDIR>", "<APPDIR>/data", "<APPDIR>/data/<APPNAME>" |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| AppConfigLocation     | "~/Library/Preferences/<APPNAME>"                                                                            | "C:/Users/<USER>/AppData/Local/<APPNAME>", "C:/ProgramData/<APPNAME>"                                                           |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| PublicShareLocation   | "~/Public"                                                                                                   | "C:/Users/Public"                                                                                                               |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| TemplatesLocation     | "~/Templates"                                                                                                | "C:/Users/<USER>/AppData/Roaming/Microsoft/Windows/Templates"                                                                   |
+-----------------------+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

+-----------------------+-------------------------------------------------------------------------------------------+
| Path type             | Linux and other UNIX operating systems                                                    |
+=======================+===========================================================================================+
| DesktopLocation       | "~/Desktop"                                                                               |
+-----------------------+-------------------------------------------------------------------------------------------+
| DocumentsLocation     | "~/Documents"                                                                             |
+-----------------------+-------------------------------------------------------------------------------------------+
| FontsLocation         | "~/.fonts", "~/.local/share/fonts", "/usr/local/share/fonts", "/usr/share/fonts"          |
+-----------------------+-------------------------------------------------------------------------------------------+
| ApplicationsLocation  | "~/.local/share/applications", "/usr/local/share/applications", "/usr/share/applications" |
+-----------------------+-------------------------------------------------------------------------------------------+
| MusicLocation         | "~/Music"                                                                                 |
+-----------------------+-------------------------------------------------------------------------------------------+
| MoviesLocation        | "~/Videos"                                                                                |
+-----------------------+-------------------------------------------------------------------------------------------+
| PicturesLocation      | "~/Pictures"                                                                              |
+-----------------------+-------------------------------------------------------------------------------------------+
| TempLocation          | "/tmp"                                                                                    |
+-----------------------+-------------------------------------------------------------------------------------------+
| HomeLocation          | "~"                                                                                       |
+-----------------------+-------------------------------------------------------------------------------------------+
| AppLocalDataLocation  | "~/.local/share/<APPNAME>", "/usr/local/share/<APPNAME>", "/usr/share/<APPNAME>"          |
+-----------------------+-------------------------------------------------------------------------------------------+
| CacheLocation         | "~/.cache/<APPNAME>"                                                                      |
+-----------------------+-------------------------------------------------------------------------------------------+
| GenericDataLocation   | "~/.local/share", "/usr/local/share", "/usr/share"                                        |
+-----------------------+-------------------------------------------------------------------------------------------+
| RuntimeLocation       | "/run/user/<USER>"                                                                        |
+-----------------------+-------------------------------------------------------------------------------------------+
| ConfigLocation        | "~/.config", "/etc/xdg"                                                                   |
+-----------------------+-------------------------------------------------------------------------------------------+
| GenericConfigLocation | "~/.config", "/etc/xdg"                                                                   |
+-----------------------+-------------------------------------------------------------------------------------------+
| DownloadLocation      | "~/Downloads"                                                                             |
+-----------------------+-------------------------------------------------------------------------------------------+
| GenericCacheLocation  | "~/.cache"                                                                                |
+-----------------------+-------------------------------------------------------------------------------------------+
| AppDataLocation       | "~/.local/share/<APPNAME>", "/usr/local/share/<APPNAME>", "/usr/share/<APPNAME>"          |
+-----------------------+-------------------------------------------------------------------------------------------+
| AppConfigLocation     | "~/.config/<APPNAME>", "/etc/xdg/<APPNAME>"                                               |
+-----------------------+-------------------------------------------------------------------------------------------+
| PublicShareLocation   | "~/Public"                                                                                |
+-----------------------+-------------------------------------------------------------------------------------------+
| TemplatesLocation     | "~/Templates"                                                                             |
+-----------------------+-------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| Path type             | Android                                                  | iOS                                                 |
+=======================+==========================================================+=====================================================+
| DesktopLocation       | "<APPROOT>/files"                                        | "<APPROOT>/Documents/Desktop"                       |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| DocumentsLocation     | "<USER>/Documents" [\*], "<USER>/<APPNAME>/Documents"    | "<APPROOT>/Documents"                               |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| FontsLocation         | "/system/fonts" (not writable)                           | "<APPROOT>/Library/Fonts"                           |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| ApplicationsLocation  | not supported (directory not readable)                   | not supported                                       |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| MusicLocation         | "<USER>/Music" [\*], "<USER>/<APPNAME>/Music"            | "<APPROOT>/Documents/Music"                         |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| MoviesLocation        | "<USER>/Movies" [\*], "<USER>/<APPNAME>/Movies"          | "<APPROOT>/Documents/Movies"                        |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| PicturesLocation      | "<USER>/Pictures" [\*], "<USER>/<APPNAME>/Pictures"      | "<APPROOT>/Documents/Pictures", "assets-library://" |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| TempLocation          | "<APPROOT>/cache"                                        | "<APPROOT>/tmp"                                     |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| HomeLocation          | "<APPROOT>/files"                                        | system defined                                      |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| AppLocalDataLocation  | "<APPROOT>/files", "<USER>/<APPNAME>/files"              | "<APPROOT>/Library/Application Support"             |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| CacheLocation         | "<APPROOT>/cache", "<USER>/<APPNAME>/cache"              | "<APPROOT>/Library/Caches"                          |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| GenericDataLocation   | "<USER>" [\*] or "<USER>/<APPNAME>/files"                | "<APPROOT>/Library/Application Support"             |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| RuntimeLocation       | "<APPROOT>/cache"                                        | not supported                                       |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| ConfigLocation        | "<APPROOT>/files/settings"                               | "<APPROOT>/Library/Preferences"                     |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| GenericConfigLocation | "<APPROOT>/files/settings" (there is no shared settings) | "<APPROOT>/Library/Preferences"                     |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| DownloadLocation      | "<USER>/Downloads" [\*], "<USER>/<APPNAME>/Downloads"    | "<APPROOT>/Documents/Downloads"                     |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| GenericCacheLocation  | "<APPROOT>/cache" (there is no shared cache)             | "<APPROOT>/Library/Caches"                          |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| AppDataLocation       | "<APPROOT>/files", "<USER>/<APPNAME>/files"              | "<APPROOT>/Library/Application Support"             |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| AppConfigLocation     | "<APPROOT>/files/settings"                               | "<APPROOT>/Library/Preferences/<APPNAME>"           |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| PublicShareLocation   | not supported                                            | not supported                                       |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+
| TemplatesLocation     | not supported                                            | not supported                                       |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------+

In the table above, ``<APPNAME>`` is usually the organization name, the application name, or both, or a unique name generated at packaging. Similarly, <APPROOT> is the location where this application is installed (often a sandbox). <APPDIR> is the directory containing the application executable.

The paths above should not be relied upon, as they may change according to OS configuration, locale, or they may change in future Qt versions.

**Note:** On Android, applications with open files on the external storage (<USER> locations), will be killed if the external storage is unmounted.

**Note:** On Android 6.0 (API 23) or higher, the "WRITE_EXTERNAL_STORAGE" permission must be requested at runtime when using :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation` or :sip:ref:`~PyQt6.QtCore.QStandardPaths.standardLocations`.

**Note:** On Android, reading/writing to GenericDataLocation needs the READ_EXTERNAL_STORAGE/WRITE_EXTERNAL_STORAGE permission granted.

**Note:** [\*] On Android 11 and above, public directories are no longer directly accessible in scoped storage mode. Thus, paths of the form ``"<USER>/DirName"`` are not returned. Instead, you can use :sip:ref:`~PyQt6.QtWidgets.QFileDialog` which uses the Storage Access Framework (SAF) to access such directories.

**Note:** On iOS, if you do pass ``QStandardPaths::standardLocations(QStandardPaths::PicturesLocation).last()`` as argument to :sip:ref:`~PyQt6.QtWidgets.QFileDialog.setDirectory`, a native image picker dialog will be used for accessing the user's photo album. The filename returned can be loaded using :sip:ref:`~PyQt6.QtCore.QFile` and related APIs. This feature was added in Qt 5.5.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation`, :sip:ref:`~PyQt6.QtCore.QStandardPaths.standardLocations`, :sip:ref:`~PyQt6.QtCore.QStandardPaths.displayName`, :sip:ref:`~PyQt6.QtCore.QStandardPaths.locate`, :sip:ref:`~PyQt6.QtCore.QStandardPaths.locateAll`.
