from flask import current_app, redirect, flash, url_for
from app.models.base import db
from app.models.gift import Gift
from . import web
from flask_login import login_required, current_user


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
	if current_user.can_save_to_list(isbn):
		# try:
		with db.auto_commit():
		    gift = Gift()
		    gift.isbn = isbn
		    # 实例化后的UserModel
		    # UserModel中get_user 实现current_user为UserModel的实例
		    gift.uid = current_user.id
		    current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
		    db.session.add(gift)
		#     db.session.commit()
		# except Exception as e:
		# 	# flask('{}'.format(e))
		# 	db.session.rollback()
		# 	raise e
	else:
		flash('请不要重复添加')
	return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



