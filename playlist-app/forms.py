"""Forms for playlist app."""

from wtforms import SelectField, StringField
from wtforms.validators import InputRequired, Optional
from flask_wtf import FlaskForm



class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField(
        'Name',
        validators=[InputRequired()]
    )
    description = StringField(
        'Description',
        validators=[InputRequired(), Optional()]
    )


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField(
        'Ttite',
        validators=[InputRequired()]
    )
    artist =StringField(
        'Artist',
        validators=[InputRequired()]
    )


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
