from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from evr.models import Cook

bp = Blueprint('main', __name__, url_prefix='/')


# @bp.route('/')
# def home():
#     return redirect(url_for('cook._list'))

@bp.route('/')
def hm():
    return render_template('index.html')

@bp.route('/search')
def _list():
    cook_list = Cook.query.order_by(Cook.id)
    return render_template('cook/cooks.html', cooks=cook_list)

# @bp.route('/detail/<int:cook_id>/')
# def detail(cook_id):
#     cook = Cook.query.get_or_404(cook_id)
#     return render_template('cook/cook_detail.html', cook=cook)