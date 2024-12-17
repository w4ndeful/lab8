from flask import Blueprint, render_template, redirect, url_for, request
from app.models import db, User, Post, Tag
from app.forms import PostForm

bp = Blueprint('main', __name__)


@bp.route('/')
def post_list():
    posts = Post.query.all()
    return render_template('post_list.html', posts=posts)


@bp.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)


@bp.route('/post/create', methods=['GET', 'POST'])
def post_create():
    form = PostForm()

    # Завантажуємо авторів і теги для форми
    form.author.choices = [(user.id, user.username) for user in User.query.all()]
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.all()]

    if request.method == 'POST' and form.validate_on_submit():
        # Створюємо новий пост
        post = Post(
            title=form.title.data,
            content=form.content.data,
            user_id=form.author.data
        )

        # Додаємо теги до поста
        for tag_id in form.tags.data:
            tag = Tag.query.get(tag_id)
            if tag:
                post.tags.append(tag)

        # Зберігаємо пост у базу даних
        db.session.add(post)
        db.session.commit()

        # Перенаправляємо на список постів
        return redirect(url_for('main.post_list'))

    return render_template('post_create.html', form=form)
