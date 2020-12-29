from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sim.models import Tmahasiswa
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed


class mahasiswaF(FlaskForm):
    npm= StringField('NPM', validators=[DataRequired(),Length(min=10, max=15)])
    nama= StringField('Nama', validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired(), Email()])
    kelas= StringField('Kelas', validators=[DataRequired()])
    password= PasswordField('Password', validators=[DataRequired(),Length(min=6, max=20)])
    konf_pass= PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    alamat= TextAreaField('Alamat')
    submit= SubmitField('Daftar')

    #cek npm
    def validate_npm(self, npm):
        ceknpm=Tmahasiswa.query.filter_by(npm=npm.data).first()
        if ceknpm:
            raise ValidationError('NPM Sudah Terdaftar, Gunakan NPM yang lain')

    #cek email
    def validate_email(self, email):
        cekemail=Tmahasiswa.query.filter_by(email=email.data).first()
        if cekemail:
            raise ValidationError('Email Sudah Terdaftar, Gunakan Email yang lain')

class loginmahasiswaF(FlaskForm):
    npm= StringField('NPM', validators=[DataRequired()])
    password= PasswordField('Password', validators=[DataRequired()])
    submit= SubmitField('Login')

class editmahasiswaF(FlaskForm):
    npm= StringField('NPM', validators=[DataRequired(),Length(min=10, max=15)])
    nama= StringField('Nama', validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired(), Email()])
    kelas= StringField('Kelas', validators=[DataRequired()])
    password= PasswordField('Password', validators=[DataRequired(),Length(min=6, max=20)])
    konf_pass= PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    alamat= TextAreaField('Alamat')
    foto= FileField('Ubah Foto Profile', validators=[FileAllowed(['jpg', 'png'])])
    submit= SubmitField('Ubah Data')

    #cek npm
    def validate_npm(self, npm):
        if npm.data != current_user.npm:
            ceknpm=Tmahasiswa.query.filter_by(npm=npm.data).first()
            if ceknpm:
                raise ValidationError('NPM Sudah Terdaftar, Gunakan NPM yang lain')
            

    #cek email
    def validate_email(self, email):
        if email.data != current_user.email:
            cekemail=Tmahasiswa.query.filter_by(email=email.data).first()
            if cekemail:
                raise ValidationError('Email Sudah Terdaftar, Gunakan Email yang lain')

class pengaduanF(FlaskForm):
    subjek = StringField('Subjek', validators=[DataRequired()])
    kategori = SelectField(u'Kategori Pengaduan', choices=[('administrasi','Pelayanan Administrasi'),('fasilitas','Fasilitas'),('dosen','Dosen')], validators=[DataRequired()])
    detail_pengaduan = TextAreaField('Pengaduan', validators=[DataRequired()])
    submit = SubmitField('Kirim')

class editpengaduanF(FlaskForm):
    subjek = StringField('Subjek', validators=[DataRequired()])
    kategori = SelectField(u'Kategori Pengaduan', choices=[('administrasi','Pelayanan Administrasi'),('fasilitas','Fasilitas'),('dosen','Dosen')], validators=[DataRequired()])
    detail_pengaduan = TextAreaField('Pengaduan', validators=[DataRequired()])
    submit = SubmitField('Ubah')
