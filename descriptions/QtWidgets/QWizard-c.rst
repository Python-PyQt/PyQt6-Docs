.. sip:class-description::
    :status: todo
    :brief: Framework for wizards
    :digest: 26d724276f4d9be0aeccecf2e0cc9b31

The :sip:ref:`~PyQt6.QtWidgets.QWizard` class provides a framework for wizards.

A wizard (also called an assistant on macOS) is a special type of input dialog that consists of a sequence of pages. A wizard's purpose is to guide the user through a process step by step. Wizards are useful for complex or infrequent tasks that users may find difficult to learn.

:sip:ref:`~PyQt6.QtWidgets.QWizard` inherits :sip:ref:`~PyQt6.QtWidgets.QDialog` and represents a wizard. Each page is a :sip:ref:`~PyQt6.QtWidgets.QWizardPage` (a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ subclass). To create your own wizards, you can use these classes directly, or you can subclass them for more control.

Topics:

.. _qwizard-a-trivial-example:

A Trivial Example
-----------------

The following example illustrates how to create wizard pages and add them to a wizard. For more advanced examples, see `Class Wizard <https://doc.qt.io/qt-6/qtwidgets-dialogs-classwizard-example.html>`_ and `License Wizard <https://doc.qt.io/qt-6/qtwidgets-dialogs-licensewizard-example.html>`_.

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-trivialwizard-trivialwizard.py
    :lines: 59-77

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-trivialwizard-trivialwizard.py
    :lines: 79-79

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-trivialwizard-trivialwizard.py
    :lines: 100-100

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-trivialwizard-trivialwizard.py
    :lines: 104-104

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-trivialwizard-trivialwizard.py
    :lines: 106-106

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-trivialwizard-trivialwizard.py
    :lines: 121-121

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-trivialwizard-trivialwizard.py
    :lines: 125-147

.. _qwizard-wizard-look-and-feel:

Wizard Look and Feel
--------------------

:sip:ref:`~PyQt6.QtWidgets.QWizard` supports four wizard looks:

* :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.ClassicStyle`

* :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.ModernStyle`

* :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.MacStyle`

* :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.AeroStyle`

You can explicitly set the look to use using :sip:ref:`~PyQt6.QtWidgets.QWizard.setWizardStyle` (e.g., if you want the same look on all platforms).

+--------------------------------------------------------------+-------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.ClassicStyle` | :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.ModernStyle` | :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.MacStyle` | :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.AeroStyle` |
+==============================================================+=============================================================+==========================================================+===========================================================+
| |image-qtwizard-classic1-png|                                | |image-qtwizard-modern1-png|                                | |image-qtwizard-mac1-png|                                | |image-qtwizard-aero1-png|                                |
+--------------------------------------------------------------+-------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+
| |image-qtwizard-classic2-png|                                | |image-qtwizard-modern2-png|                                | |image-qtwizard-mac2-png|                                | |image-qtwizard-aero2-png|                                |
+--------------------------------------------------------------+-------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+

Note: :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.AeroStyle` has effect only on a Windows Vista system with alpha compositing enabled. :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.ModernStyle` is used as a fallback when this condition is not met.

In addition to the wizard style, there are several options that control the look and feel of the wizard. These can be set using :sip:ref:`~PyQt6.QtWidgets.QWizard.setOption` or :sip:ref:`~PyQt6.QtWidgets.QWizard.setOptions`. For example, :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveHelpButton` makes :sip:ref:`~PyQt6.QtWidgets.QWizard` show a Help button along with the other wizard buttons.

You can even change the order of the wizard buttons to any arbitrary order using :sip:ref:`~PyQt6.QtWidgets.QWizard.setButtonLayout`, and you can add up to three custom buttons (e.g., a Print button) to the button row. This is achieved by calling :sip:ref:`~PyQt6.QtWidgets.QWizard.setButton` or :sip:ref:`~PyQt6.QtWidgets.QWizard.setButtonText` with :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton1`, :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton2`, or :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton3` to set up the button, and by enabling the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveCustomButton1`, :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveCustomButton2`, or :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveCustomButton3` options. Whenever the user clicks a custom button, :sip:ref:`~PyQt6.QtWidgets.QWizard.customButtonClicked` is emitted. For example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-licensewizard-licensewizard.py
    :lines: 359-362

.. _qwizard-elements-of-a-wizard-page:

Elements of a Wizard Page
-------------------------

Wizards consist of a sequence of :sip:ref:`~PyQt6.QtWidgets.QWizardPage`\ s. At any time, only one page is shown. A page has the following attributes:

* A :sip:ref:`~PyQt6.QtWidgets.QWizardPage.title`.

* A :sip:ref:`~PyQt6.QtWidgets.QWizardPage.subTitle`.

* A set of pixmaps, which may or may not be honored, depending on the wizard's style:

  * :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardPixmap.WatermarkPixmap` (used by :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.ClassicStyle` and :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.ModernStyle`)

  * :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardPixmap.BannerPixmap` (used by :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.ModernStyle`)

  * :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardPixmap.LogoPixmap` (used by :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.ClassicStyle` and :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.ModernStyle`)

  * :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardPixmap.BackgroundPixmap` (used by :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.MacStyle`)

The diagram belows shows how :sip:ref:`~PyQt6.QtWidgets.QWizard` renders these attributes, assuming they are all present and :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.ModernStyle` is used:

.. image:: ../../../images/qtwizard-nonmacpage.png

When a :sip:ref:`~PyQt6.QtWidgets.QWizardPage.subTitle` is set, :sip:ref:`~PyQt6.QtWidgets.QWizard` displays it in a header, in which case it also uses the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardPixmap.BannerPixmap` and the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardPixmap.LogoPixmap` to decorate the header. The :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardPixmap.WatermarkPixmap` is displayed on the left side, below the header. At the bottom, there is a row of buttons allowing the user to navigate through the pages.

The page itself (the :sip:ref:`~PyQt6.QtWidgets.QWizardPage` widget) occupies the area between the header, the watermark, and the button row. Typically, the page is a :sip:ref:`~PyQt6.QtWidgets.QWizardPage` on which a :sip:ref:`~PyQt6.QtWidgets.QGridLayout` is installed, with standard child widgets (\ :sip:ref:`~PyQt6.QtWidgets.QLabel`\ s, :sip:ref:`~PyQt6.QtWidgets.QLineEdit`\ s, etc.).

If the wizard's style is :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.MacStyle`, the page looks radically different:

.. image:: ../../../images/qtwizard-macpage.png

The watermark, banner, and logo pixmaps are ignored by the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.MacStyle`. If the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardPixmap.BackgroundPixmap` is set, it is used as the background for the wizard; otherwise, a default "assistant" image is used.

The title and subtitle are set by calling :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setTitle` and :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setSubTitle` on the individual pages. They may be plain text or HTML (see :sip:ref:`~PyQt6.QtWidgets.QWizard.titleFormat` and :sip:ref:`~PyQt6.QtWidgets.QWizard.subTitleFormat`). The pixmaps can be set globally for the entire wizard using :sip:ref:`~PyQt6.QtWidgets.QWizard.setPixmap`, or on a per-page basis using :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setPixmap`.

.. _qwizard-field-mechanism:

.. _qwizard-registering-and-using-fields:

Registering and Using Fields
----------------------------

In many wizards, the contents of a page may affect the default values of the fields of a later page. To make it easy to communicate between pages, :sip:ref:`~PyQt6.QtWidgets.QWizard` supports a "field" mechanism that allows you to register a field (e.g., a :sip:ref:`~PyQt6.QtWidgets.QLineEdit`) on a page and to access its value from any page. It is also possible to specify mandatory fields (i.e., fields that must be filled before the user can advance to the next page).

To register a field, call :sip:ref:`~PyQt6.QtWidgets.QWizardPage.registerField` field. For example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-classwizard-classwizard.py
    :lines: 235-237

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-classwizard-classwizard.py
    :lines: 245-254

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-classwizard-classwizard.py
    :lines: 271-273

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-classwizard-classwizard.py
    :lines: 297-297

The above code registers three fields, ``className``, ``baseClass``, and ``qobjectMacro``, which are associated with three child widgets. The asterisk (``\*``) next to ``className`` denotes a mandatory field.

.. _qwizard-initialize-page:

The fields of any page are accessible from any other page. For example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-classwizard-classwizard.py
    :lines: 414-420

Here, we call :sip:ref:`~PyQt6.QtWidgets.QWizardPage.field` to access the contents of the ``className`` field (which was defined in the ``ClassInfoPage``) and use it to initialize the ``OutputFilePage``. The field's contents is returned as a `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_.

When we create a field using :sip:ref:`~PyQt6.QtWidgets.QWizardPage.registerField`, we pass a unique field name and a widget. We can also provide a Qt property name and a "changed" signal (a signal that is emitted when the property changes) as third and fourth arguments; however, this is not necessary for the most common Qt widgets, such as :sip:ref:`~PyQt6.QtWidgets.QLineEdit`, :sip:ref:`~PyQt6.QtWidgets.QCheckBox`, and `QComboBox <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qcombobox>`_, because :sip:ref:`~PyQt6.QtWidgets.QWizard` knows which properties to look for.

.. _qwizard-mandatory-fields:

If an asterisk (``\*``) is appended to the name when the property is registered, the field is a *mandatory field*. When a page has mandatory fields, the Next and/or Finish buttons are enabled only when all mandatory fields are filled.

To consider a field "filled", :sip:ref:`~PyQt6.QtWidgets.QWizard` simply checks that the field's current value doesn't equal the original value (the value it had when :sip:ref:`~PyQt6.QtWidgets.QWizard.initializePage` was called). For :sip:ref:`~PyQt6.QtWidgets.QLineEdit` and :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox` subclasses, :sip:ref:`~PyQt6.QtWidgets.QWizard` also checks that :sip:ref:`~PyQt6.QtWidgets.QLineEdit.hasAcceptableInput` returns true, to honor any validator or mask.

:sip:ref:`~PyQt6.QtWidgets.QWizard`'s mandatory field mechanism is provided for convenience. A more powerful (but also more cumbersome) alternative is to reimplement :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isComplete` and to emit the :sip:ref:`~PyQt6.QtWidgets.QWizardPage.completeChanged` signal whenever the page becomes complete or incomplete.

The enabled/disabled state of the Next and/or Finish buttons is one way to perform validation on the user input. Another way is to reimplement :sip:ref:`~PyQt6.QtWidgets.QWizard.validateCurrentPage` (or :sip:ref:`~PyQt6.QtWidgets.QWizardPage.validatePage`) to perform some last-minute validation (and show an error message if the user has entered incomplete or invalid information). If the function returns ``true``, the next page is shown (or the wizard finishes); otherwise, the current page stays up.

.. _qwizard-creating-linear-wizards:

Creating Linear Wizards
-----------------------

Most wizards have a linear structure, with page 1 followed by page 2 and so on until the last page. The `Class Wizard <https://doc.qt.io/qt-6/qtwidgets-dialogs-classwizard-example.html>`_ example is such a wizard. With :sip:ref:`~PyQt6.QtWidgets.QWizard`, linear wizards are created by instantiating the :sip:ref:`~PyQt6.QtWidgets.QWizardPage`\ s and inserting them using :sip:ref:`~PyQt6.QtWidgets.QWizard.addPage`. By default, the pages are shown in the order in which they were added. For example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-classwizard-classwizard.py
    :lines: 58-65

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-classwizard-classwizard.py
    :lines: 73-73

When a page is about to be shown, :sip:ref:`~PyQt6.QtWidgets.QWizard` calls :sip:ref:`~PyQt6.QtWidgets.QWizard.initializePage` (which in turn calls :sip:ref:`~PyQt6.QtWidgets.QWizardPage.initializePage`) to fill the page with default values. By default, this function does nothing, but it can be reimplemented to initialize the page's contents based on other pages' fields (see the :ref:`example above<qwizard-initialize-page>`).

If the user presses Back, :sip:ref:`~PyQt6.QtWidgets.QWizard.cleanupPage` is called (which in turn calls :sip:ref:`~PyQt6.QtWidgets.QWizardPage.cleanupPage`). The default implementation resets the page's fields to their original values (the values they had before :sip:ref:`~PyQt6.QtWidgets.QWizard.initializePage` was called). If you want the Back button to be non-destructive and keep the values entered by the user, simply enable the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.IndependentPages` option.

.. _qwizard-creating-non-linear-wizards:

Creating Non-Linear Wizards
---------------------------

Some wizards are more complex in that they allow different traversal paths based on the information provided by the user. The `License Wizard <https://doc.qt.io/qt-6/qtwidgets-dialogs-licensewizard-example.html>`_ example illustrates this. It provides five wizard pages; depending on which options are selected, the user can reach different pages.

.. image:: ../../../images/licensewizard-flow.png

In complex wizards, pages are identified by IDs. These IDs are typically defined using an enum. For example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-licensewizard-licensewizard.py
    :lines: 67-69

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-licensewizard-licensewizard.py
    :lines: 67-78

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-licensewizard-licensewizard.py
    :lines: 82-82

The pages are inserted using :sip:ref:`~PyQt6.QtWidgets.QWizard.setPage`, which takes an ID and an instance of :sip:ref:`~PyQt6.QtWidgets.QWizardPage` (or of a subclass):

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-licensewizard-licensewizard.py
    :lines: 67-75

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-licensewizard-licensewizard.py
    :lines: 97-97

By default, the pages are shown in increasing ID order. To provide a dynamic order that depends on the options chosen by the user, we must reimplement :sip:ref:`~PyQt6.QtWidgets.QWizardPage.nextId`. For example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-licensewizard-licensewizard.py
    :lines: 175-183

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-licensewizard-licensewizard.py
    :lines: 220-223

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-licensewizard-licensewizard.py
    :lines: 253-260

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-licensewizard-licensewizard.py
    :lines: 298-301

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-licensewizard-licensewizard.py
    :lines: 324-327

It would also be possible to put all the logic in one place, in a :sip:ref:`~PyQt6.QtWidgets.QWizard.nextId` reimplementation. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qwizard.py
    :lines: 54-77

To start at another page than the page with the lowest ID, call :sip:ref:`~PyQt6.QtWidgets.QWizard.setStartId`.

To test whether a page has been visited or not, call :sip:ref:`~PyQt6.QtWidgets.QWizard.hasVisitedPage`. For example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-licensewizard-licensewizard.py
    :lines: 331-349

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizardPage`, `Class Wizard Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-classwizard-example.html>`_, `License Wizard Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-licensewizard-example.html>`_.

.. |image-qtwizard-classic1-png| image:: ../../../images/qtwizard-classic1.png
.. |image-qtwizard-modern1-png| image:: ../../../images/qtwizard-modern1.png
.. |image-qtwizard-mac1-png| image:: ../../../images/qtwizard-mac1.png
.. |image-qtwizard-aero1-png| image:: ../../../images/qtwizard-aero1.png
.. |image-qtwizard-classic2-png| image:: ../../../images/qtwizard-classic2.png
.. |image-qtwizard-modern2-png| image:: ../../../images/qtwizard-modern2.png
.. |image-qtwizard-mac2-png| image:: ../../../images/qtwizard-mac2.png
.. |image-qtwizard-aero2-png| image:: ../../../images/qtwizard-aero2.png
