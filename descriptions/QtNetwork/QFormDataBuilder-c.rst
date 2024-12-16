.. sip:class-description::
    :status: todo
    :brief: Convenience class to simplify the construction of QHttpMultiPart objects
    :digest: a690332084a52dea8a40c88917d9ec64

The :sip:ref:`~PyQt6.QtNetwork.QFormDataBuilder` class is a convenience class to simplify the construction of :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart` objects.

The :sip:ref:`~PyQt6.QtNetwork.QFormDataBuilder` class can be used to build a :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart` object with the content type set to be FormDataType by default.

The snippet below demonstrates how to build a multipart message with :sip:ref:`~PyQt6.QtNetwork.QFormDataBuilder`:

::

    QFormDataBuilder builder;
    QFile image(u"../../pic.png"_s); image.open(QFile::ReadOnly);
    QFile mask(u"../../mask.png"_s); mask.open(QFile::ReadOnly);

    builder.part("image"_L1).setBodyDevice(&image, "the actual image");
    builder.part("mask"_L1).setBodyDevice(&mask, "the mask image");
    builder.part("prompt"_L1).setBody("Lobster wearing a beret");
    builder.part("n"_L1).setBody("2");
    builder.part("size"_L1).setBody("512x512");

    std::unique_ptr<QHttpMultiPart> mp = builder.buildMultiPart();

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttpPart`, :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart`, :sip:ref:`~PyQt6.QtNetwork.QFormDataPartBuilder`.
