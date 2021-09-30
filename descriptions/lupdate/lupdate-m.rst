.. sip:module-description::
    :status:    done
    :brief:     Functions for handling translation files used by Qt Linguist

The :sip:ref:`~PyQt6.lupdate` module contains functions for creating and
updating the :file:`.ts` files used by Qt Linguist to implement human language
translations of messages in Python source (:file:`.py`) files and Qt Designer
source (:file:`.ui`) files.


.. py:function:: PyQt6.lupdate.lupdate(sources, translation_files, no_obsolete=False, no_summary=True, verbose=False, excludes=None)

    Create or update a sequence of translation files from a sequence of Python
    source files, Qt Designer Source files or directories containing source
    files.

    :param list[str] sources:
        the list of names of source files or directories from which
        translatable messages are extracted.  Directories are searched
        recursively for source files.
    :param list[str] translation_files:
        the list of names of translation files (usually one for each supported
        human language) that are created or updated with the translatable
        messages extracted from the source files.
    :param bool no_obsolete:
        specifies that all obsolete messages from the translation files should
        be discarded.  An obsolete message is one that was found by a previous
        call to :sip:ref:`~PyQt6.lupdate.lupdate` but has not been found by
        this call.  By default obsolete messages are retained and marked as
        such in the translation file.
    :param bool no_summary:
        specifies that a summary of updates to the translation files should not
        be displayed on :py:data:`~sys.stdout`.
    :param bool verbose:
        specifies that progress messages should be displayed to
        :py:data:`~sys.stdout`.
    :param list[str] excludes:
        a list of UNIX shell-style patterns that are matched against the source
        files found when recursively searching a directory.  If a source file
        matches then it is excluded.
