from . import web
from flask import redirect, url_for, flash, render_template
from app.models.base import db
from app.models.wish import Wish
from flask_login import login_required, current_user
from app.view_models.wish import MyWishes


@web.route('/my/wish')
@login_required
def my_wish():
    uid = current_user.id
    wishes_of_mine = Wish.get_user_wishes(uid)
    isbn_list = [wish.isbn for wish in wishes_of_mine]
    gift_count_list = Wish.get_gift_counts(isbn_list)
    view_model = MyWishes(wishes_of_mine, gift_count_list)
    return render_template('my_wish.html', wishes=view_model.wishes)

@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash('请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))

@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass

@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
