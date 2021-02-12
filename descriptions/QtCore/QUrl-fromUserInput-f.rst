.. sip:method-description::
    :status: todo
    :pysig: cce37e9fd5f03ad8c8a83c9b1b86d661
    :realsig: (const QString&,const QString&,QUrl::UserInputResolutionOptions)
    :digest: e11a08441038e815c2ce14d1f764de35

Returns a valid URL from a user supplied *userInput* string if one can be deduced. In the case that is not possible, an invalid :sip:ref:`~PyQt6.QtCore.QUrl` is returned.

This allows the user to input a URL or a local file path in the form of a plain string. This string can be manually typed into a location bar, obtained from the clipboard, or passed in via command line arguments.

When the string is not already a valid URL, a best guess is performed, making various assumptions.

In the case the string corresponds to a valid file path on the system, a file:// URL is constructed, using :sip:ref:`~PyQt6.QtCore.QUrl.fromLocalFile`.

If that is not the case, an attempt is made to turn the string into a http:// or ftp:// URL. The latter in the case the string starts with 'ftp'. The result is then passed through :sip:ref:`~PyQt6.QtCore.QUrl`'s tolerant parser, and in the case or success, a valid :sip:ref:`~PyQt6.QtCore.QUrl` is returned, or else a :sip:ref:`~PyQt6.QtCore.QUrl`.

Examples:
---------

* qt-project.org becomes http://qt-project.org

* ftp.qt-project.org becomes ftp://ftp.qt-project.org

* hostname becomes http://hostname

* /home/user/test.html becomes file:///home/user/test.html

In order to be able to handle relative paths, this method takes an optional *workingDirectory* path. This is especially useful when handling command line arguments. If *workingDirectory* is empty, no handling of relative paths will be done.

By default, an input string that looks like a relative path will only be treated as such if the file actually exists in the given working directory. If the application can handle files that don't exist yet, it should pass the flag :sip:ref:`~PyQt6.QtCore.QUrl.UserInputResolutionOptions.AssumeLocalFile` in *options*.
