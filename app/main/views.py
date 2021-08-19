from app.auth.forms import UpdateProfileForm
from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import CommentForm, PitchForm
from .. import db,photos
from .. models import Comment, Pitch, User
from flask_login import login_required, current_user

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    form_pitch = PitchForm()
    all_pitches = Pitch.query.order_by(Pitch.posted).all()
    return render_template('index.html', pitches = all_pitches)


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
        
        return redirect(url_for('main.index'))
    else:
        all_pitches = Pitch.query.order_by(Pitch.posted).all()
    
    return render_template('newpitch.html', pitches=all_pitches,form_pitch = form_pitch)

@main.route('/comment/<int:id>',methods= ['POST','GET'])
@login_required
def viewPitch(id):
    eachpitch = Pitch.getPitchId(id)
    comments = Comment.getComments(id)

    if request.args.get("like"):
        eachpitch=0;
        eachpitch.likes = eachpitch.likes + 1

        db.session.add(eachpitch)
        db.session.commit()

        return redirect(eachpitch)

    elif request.args.get("dislike"):
        eachpitch=0;

        db.session.add(eachpitch)
        db.session.commit()

        return redirect(eachpitch)

    commentForm = CommentForm()
    if commentForm.validate_on_submit():
        comment = commentForm.text.data

        newComment = Comment(comment = comment,user = current_user,pitch_id= id)

        newComment.saveComment()

    return render_template('comment.html',commentForm = commentForm,comments = comments,pitch = eachpitch)



@main.route('/category/product',methods= ['GET'])
def displayProductCategory():
    productPitches = Pitch.get_pitches('product')
    return render_template('category/product.html',productPitches = productPitches)
    
@main.route('/category/promotion',methods= ['POST','GET'])
def displaypromotionCategory():
    promotionPitches = Pitch.get_pitches('promotion')
    return render_template('category/promotion.html',promotionPitches = promotionPitches)

@main.route('/category/business',methods= ['POST','GET'])
def displaybusinessCategory():
    businessPitches = Pitch.get_pitches('business')
    return render_template('category/business.html',businessPitches = businessPitches)

@main.route('/category/pickup',methods= ['POST','GET'])
def displayPickupCategory():
    pickupPitches = Pitch.get_pitches('pickup')
    return render_template('category/pickup.html',pickupPitches = pickupPitches)