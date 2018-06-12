from app.view_models.book import BookViewModel
from . import web
from app.models.gift import Gift
from flask import render_template


__author__ = '七月'


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    # 处理BookViewModel都应该view func执行
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web.route('/personal')
def personal_center():
    pass
