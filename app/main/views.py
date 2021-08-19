from app.auth.forms import UpdateProfileForm
from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm
from .. import db,photos
from .. models import Pitch, User
from flask_login import login_required, current_user

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    return render_template('index.html')


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)

@main.route('/pitch/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_review(id):
    return render_template('newcomment.html')


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfileForm()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

@main.route('/newpitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    form_pitch = PitchForm()
    if form_pitch.validate_on_submit():
        pitch_title = form_pitch.pitch_title.data
        pitch_category = form_pitch.pitch_category.data
        pitch_comment = form_pitch.pitch_comment.data
        
        new_pitch = Pitch(pitch_title=pitch_title, pitch_category=pitch_category,pitch_comment=pitch_comment, user=current_user)
        
        new_pitch.save_pitch()
        db.session.add(new_pitch)
        db.session.commit()
        
        return redirect(url_for('main.pitches'))
    else:
        all_pitches = Pitch.query.order_by(Pitch.posted).all()
    
    return render_template('newpitch.html', pitches=all_pitches,form_pitch = form_pitch)

@main.route('/pitches',methods=['GET'])
@login_required
def pitches():
    all_pitches = Pitch.query.order_by(Pitch.posted).all()
    return render_template('pitches.html',pitches=all_pitches)