.. sip:method-description::
    :status: todo
    :pysig: b7efc3f359e5366eacb793e3cffdc2cf
    :realsig: (const QString&,const QString&,const QString&,const QString&)
    :digest: 0fb06749feae3cabae73f90306900ce7

Loads *filename* + *suffix* (".qm" if the *suffix* is not specified), which may be an absolute file name or relative to *directory*. Returns ``true`` if the translation is successfully loaded; otherwise returns ``false``.

If *directory* is not specified, the current directory is used (i.e., as :sip:ref:`~PyQt6.QtCore.QDir.currentPath`).

The previous contents of this translator object are discarded.

If the file name does not exist, other file names are tried in the following order:

#. File name without *suffix* appended.

#. File name with text after a character in *search_delimiters* stripped ("_." is the default for *search_delimiters* if it is an empty string) and *suffix*.

#. File name stripped without *suffix* appended.

#. File name stripped further, etc.

For example, an application running in the fr_CA locale (French-speaking Canada) might call load("foo.fr_ca", "/opt/foolib").  would then try to open the first existing readable file from this list:

#. ``/opt/foolib/foo.fr_ca.qm``

#. ``/opt/foolib/foo.fr_ca``

#. ``/opt/foolib/foo.fr.qm``

#. ``/opt/foolib/foo.fr``

#. ``/opt/foolib/foo.qm``

#. ``/opt/foolib/foo``

Usually, it is better to use the (const :sip:ref:`~PyQt6.QtCore.QLocale` &, const QString &, const QString &, const QString &, const QString &) function instead, because it uses :sip:ref:`~PyQt6.QtCore.QLocale.uiLanguages` and not simply the locale name, which refers to the formatting of dates and numbers and not necessarily the UI language.
