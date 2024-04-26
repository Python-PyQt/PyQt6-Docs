.. sip:class-description::
    :status: todo
    :brief: Manages a three dimensional sound field
    :digest: 3397c796f9ef8e39c23be85aa773c538

:sip:ref:`~PyQt6.QtSpatialAudio.QAudioEngine` manages a three dimensional sound field.

You can use an instance of :sip:ref:`~PyQt6.QtSpatialAudio.QAudioEngine` to manage a sound field in three dimensions. A sound field is defined by several :sip:ref:`~PyQt6.QtSpatialAudio.QSpatialSound` objects that define a sound at a specified location in 3D space. You can also add stereo overlays using :sip:ref:`~PyQt6.QtSpatialAudio.QAmbientSound`.

You can use :sip:ref:`~PyQt6.QtSpatialAudio.QAudioListener` to define the position of the person listening to the sound field relative to the sound sources. Sound sources will be less audible if the listener is further away from source. They will also get mapped to the corresponding loudspeakers depending on the direction between listener and source.

:sip:ref:`~PyQt6.QtSpatialAudio.QAudioEngine` offers two output modes. The first mode renders the sound field to a set of speakers, either a stereo speaker pair or a surround configuration. The second mode provides an immersive 3D sound experience when using headphones.

Perception of sound localization is driven mainly by two factors. The first factor is timing differences of the sound waves between left and right ear. The second factor comes from various ways how sounds coming from different direcations create different types of reflections from our ears and heads. See https://en.wikipedia.org/wiki/Sound_localization for more details.

The spatial audio engine emulates those timing differences and reflections through Head related transfer functions (HRTF, see https://en.wikipedia.org/wiki/Head-related_transfer_function). The functions used emulates those effects for an average persons ears and head. It provides a good and immersive 3D sound localization experience for most persons when using headphones.

The engine is rather versatile allowing you to define room properties and reverb settings to emulate different types of rooms.

Sound sources can also be occluded dampening the sound coming from those sources.

The audio engine uses a coordinate system that is in centimeters by default. The axes are aligned with the typical coordinate system used in 3D. Positive x points to the right, positive y points up and positive z points backwards.
