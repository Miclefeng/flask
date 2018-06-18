from app.libs.email import send_mail
from app.models.gift import Gift
from app.view_models.trade import MyTrades
from . import web
from flask import redirect, url_for, flash, render_template
from app.models.base import db
from app.models.wish import Wish
from flask_login import login_required, current_user


@web.route('/my/wish')
@login_required
def my_wish():
    uid = current_user.id
    wishes_of_mine = Wish.get_user_wishes(uid)
    isbn_list = [wish.isbn for wish in wishes_of_mine]
    gift_count_list = Wish.get_gift_counts(isbn_list)
    view_model = MyTrades(wishes_of_mine, gift_count_list)
    return render_template('my_wish.html', wishes=view_model.trades)

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
@login_required
def satisfy_wish(wid):
    wish = Wish.query.get_or_404(wid)
    gift = Gift.query.filter_by(uid=current_user.id, isbn=wish.isbn).first()
    if not gift:
        flash('你还没有上传此书')
    else:
        send_mail(wish.user.email, '有人想赠送你一本书', 'email/satisify_wish.html', wis=wish, gift=gift)
        flash('已向他/她发送了一封邮件')
    return redirect(url_for('web.book_detail', isbn=wish.isbn))

@web.route('/wish/book/<isbn>/redraw')
@login_required
def redraw_from_wish(isbn):
    wish = Wish.query.filter_by(isbn=isbn, launched=False).first_or_404()
    with db.auto_commit():
        wish.delete()
    return redirect(url_for('web.my_wish'))
