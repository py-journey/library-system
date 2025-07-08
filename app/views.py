# 视图函数 + 路由
from flask import Blueprint,render_template,request,flash,redirect,url_for,session
from app.models import *

main = Blueprint('main',__name__)


# system_index
@main.route('/')
def home():
    return render_template('home.html')

# login
@main.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form.get('username')
        pwd = request.form.get('passwd')
        user = User.query.filter_by(username=name,passwd=pwd).first()
        if user:
            session['user'] = user.username
            return redirect(url_for('main.index'))
        flash('用户或密码错误！')
    return render_template('login.html')

# register
@main.route('/register',methods=['POST','GET'])
def register():
  if request.method == 'POST':
      # 获取前端数据
      uname = request.form.get('username')
      pwd = request.form.get('passwd')
      confirm_pwd = request.form.get('confirm_passwd')
      if not uname or not pwd:
          flash('用户名和密码不能为空！')
          return redirect(url_for('main.register'))
      elif confirm_pwd != pwd:
          flash('密码不一致，请重新输入！')
          return redirect(url_for('main.register'))

      # 检查用户是否存在
      if User.query.filter_by(username=uname).first():
          flash('用户已存在')
          return redirect(url_for('main.register'))
      # 创建用户对象
      new_user = User(username=uname, passwd=pwd)
      db.session.add(new_user)
      db.session.commit()
      flash('注册成功')
      return redirect(url_for('main.login'))
  return render_template('register.html')

# logout
@main.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('main.login'))

# books_list
@main.route('/books')
def index():
    if 'user' not in session:
        return redirect(url_for('main.login'))
    books = Book.query.all()
    return render_template('index.html',books=books)

# add_book
@main.route('/add', methods=['POST'])
def add():
    if 'user' not in session:
        return redirect(url_for('main.login'))

    title = request.form.get('title')
    author_name = request.form.get('author')  # 获取作者名字（不是ID）

    if not title or not author_name:
        flash('书名和作者不能为空！')
        return redirect(url_for('main.index'))

    # 检查作者是否存在，不存在则创建
    author = Author.query.filter_by(name=author_name).first()
    if not author:
        # 创建新作者（假设Author模型只需要name字段）
        author = Author(name=author_name)
        db.session.add(author)
        db.session.flush()  # 获取新作者的ID（但不提交事务）

    # 添加书籍（关联作者ID）
    new_book = Book(title=title, author_id=author.id)
    db.session.add(new_book)
    db.session.commit()

    flash('书籍添加成功！')
    return redirect(url_for('main.index'))

# delete_book
@main.route('/delete/<int:book_id>')
def delete(book_id):
    book =Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('main.index'))

# edit
@main.route('/edit/<int:book_id>',methods=['POST','GET'])
def edit(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')

        if not title or not author:
            flash('书籍和作者不能为空！')
            return redirect(url_for('main.edit',book_id=book_id))
        author_name = Author.query.filter_by(name=author).first()
        if not author_name:
            author = Author(name=author)
            db.session.add(author)
            db.session.commit()

        book.title = title
        book.author_id = author_name.id
        db.session.commit()
        flash('修改成功')
        return redirect(url_for('main.index'))
    return render_template('edit.html',book=book)

# select
@main.route('/select', methods=['POST'])
def select():
    bk_or_au = request.form.get('book_or_author', '').strip()

    # 获取原始书籍列表
    all_books = Book.query.all()

    # 获取搜索结果
    search_results = Book.query.filter(
        Book.title.contains(bk_or_au) |
        Book.author.has(Author.name.contains(bk_or_au))
    ).all()

    return render_template('index.html',
                           books=all_books,  # 始终传递完整书籍列表
                           search_results=search_results,  # 传递搜索结果
                           search_query=bk_or_au,  # 传递搜索关键词
                           user=session.get('user'))



